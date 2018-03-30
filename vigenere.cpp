#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>
#include <vector>
#include <map>
using namespace std;

int main() {
  freopen("input.txt", "r", stdin);

  string text;
  string s;
  while(cin >> s) text += s;

  // keyword length
  vector<pair<double, int> > possibilities;
  for(int i = 2 ; i < 100 ; i ++) { // guess length = i // shouldn't be higher than 100??
    double avgIndCo = 0;
    for(int j = 0 ; j < i ; j ++) { // offset j
      double indCo = 0;
      int freq[26];
      int tests = 0;
      for(int k = 0 ; k < 26 ; k ++) freq[k] = 0;
      for(int k = j ; k < text.length() ; k += i) {
	freq[text[k]-'A'] ++;
	tests ++;
      }
      for(int k = 0 ; k < 26 ; k ++) indCo += freq[k]*(freq[k]-1);
      indCo /= tests*(tests-1);
      avgIndCo += indCo;
    }
    avgIndCo /= i;
    possibilities.push_back(make_pair(abs(avgIndCo-0.0685), i));
  }
  sort(possibilities.begin(), possibilities.end());
  // TOP 20
  for(int index = 0 ; index < 20 ; index ++) {
    int ksize = possibilities[index].second;
    // for all pairs b_i b_j get sigma with highest mutual conincidence
    map<pair<int, int>, vector<pair<double, int> > > mp;
    for(int i = 0 ; i < ksize ; i ++) {
      for(int j = i+1 ; j < ksize ; j ++) {
	//mutual coincidences
	int n = (text.size() - i)/ksize;
	int m = (text.size() - j)/ksize;

	int freqi[26];
	vector<pair<double, int> > v;
	for(int k = 0 ; k < 26 ; k ++) freqi[k] = 0;
	for(int k = i ; k < text.size() ; k += ksize) freqi[text[k]-'A'] ++;

	for(int sigma = 0 ; sigma < 26 ; sigma ++) {
	  int freqj[26];
	  double mutco = 0;

	  for(int k = 0 ; k < 26 ; k ++) freqj[k] = 0;
	  for(int k = j ; k < text.size() ; k += ksize) {
	    freqj[(text[k]-'A'+sigma)%26] ++;
	  }

	  for(int k = 0 ; k < 26 ; k ++) {
	    mutco += freqi[k]*freqj[k];
	  } mutco /= n*m;
	  v.push_back(make_pair(mutco, sigma));
	}
	sort(v.begin(), v.end());
	mp.insert(make_pair(make_pair(i, j), v));
      }
    }
    // try to find "the" sigmas
    int bests[100][100];
    for(int i = 0 ; i < ksize ; i ++) {
      for(int j = 0 ; j < ksize ; j ++) {
	bests[i][j] = -1;
      }
    }
    for(int i = 0 ; i < ksize ; i ++) {
      for(int j = i+1 ; j < ksize ; j ++) {
	vector<pair<double, int> > v = mp[make_pair(i, j)];
	pair<double, int> best = v[v.size()-1];
	if(best.first > 0.05) bests[i][j] = best.second;
      }
    }

    int w[100];
    for(int i = 0 ; i < 100 ; i ++) w[i] = -1; w[0] = 0;

    for(int reps = 0 ; reps < 100 ; reps ++) {
      for(int i = 0 ; i < ksize ; i ++) { // find the ones that satisfy "triangular" equalities d_ab + d_bc = d_ac
        for(int j = i+1 ; j < min(i+10, ksize) ; j ++) {
          for(int k = i+1 ; k < j ; k ++) {
            if(bests[i][j] >= 0 && 
                bests[i][k] >= 0 &&
                bests[k][j] >= 0 && 
                (bests[i][k] + bests[k][j]) % 26 == bests[i][j]) {
	      w[k] = (w[i] + bests[i][k])%26;	     	
	      w[j] = (w[k] + bests[k][j])%26;
	    }
          }
        }
      }
    }

    for(int i = 0 ; i < 26 ; i ++) {
      string trial = "";
      for(int j = 0 ; j < text.size() ; j ++) {
	if(w[j%ksize] == -1) trial += '_';
	else trial += (text[j]-'A'+i+w[j%ksize])%26+'A';
      }
      // check for 10 "the"s, 5 "ands"
      int thes = 0;
      int ands = 0;
      for(int k = 0 ; k < trial.size()-3 ; k ++) {
	if(trial[k] == 'T' && trial[k+1] == 'H' && trial[k+2] == 'E') thes ++;
	if(trial[k] == 'A' && trial[k+1] == 'N' && trial[k+2] == 'D') ands ++;
      }
      string key = "";
      if(thes >= 10 && ands >= 5) {
	for(int j = 0 ; j < ksize ; j ++) key += (- i - w[j] + 52) % 26 + 'A';
	printf("key = %s\n%s\n", key.c_str(), trial.c_str());
      }
    }
  }

  // OUTPUT
  // key = MATHS
  // ITWASABRIGHTCOLDDAYINAPRILANDTHECLOCKSWERESTRIKINGTHIRTEENWINSTONSMITHHISCHINNUZZLEDINTOHISBREASTINANEFFORTTOESCAPETHEVILEWINDSLIPPEDQUICKLYTHROUGHTHEGLASSDOORSOFVICTORYMANSIONSTHOUGHNOTQUICKLYENOUGHTOPREVENTASWIRLOFGRITTYDUSTFROMENTERINGALONGWITHHIMTHEHALLWAYSMELTOFBOILEDCABBAGEANDOLDRAGMATSATONEENDOFITACOLOUREDPOSTERTOOLARGEFORINDOORDISPLAYHADBEENTACKEDTOTHEWALLITDEPICTEDSIMPLYANENORMOUSFACEMORETHANAMETREWIDETHEFACEOFAMANOFABOUTFORTYFIVEWITHAHEAVYBLACKMOUSTACHEANDRUGGEDLYHANDSOMEFEATURESWINSTONMADEFORTHESTAIRSITWASNOUSETRYINGTHELIFTEVENATTHEBESTOFTIMESITWASSELDOMWORKINGANDATPRESENTTHEELECTRICCURRENTWASCUTOFFDURINGDAYLIGHTHOURSITWASPARTOFTHEECONOMYDRIVEINPREPARATIONFORHATEWEEKTHEFLATWASSEVENFLIGHTSUPANDWINSTONWHOWASTHIRTYNINEANDHADAVARICOSEULCERABOVEHISRIGHTANKLEWENTSLOWLYRESTINGSEVERALTIMESONTHEWAYONEACHLANDINGOPPOSITETHELIFTSHAFTTHEPOSTERWITHTHEENORMOUSFACEGAZEDFROMTHEWALLITWASONEOFTHOSEPICTURESWHICHARESOCONTRIVEDTHATTHEEYESFOLLOWYOUABOUTWHENYOUMOVEBIGBROTHERISWATCHINGYOUTHECAPTIONBENEATHITRAN
// key = MATHSMATHS
// ITWASABRIGHTCOLDDAYINAPRILANDTHECLOCKSWERESTRIKINGTHIRTEENWINSTONSMITHHISCHINNUZZLEDINTOHISBREASTINANEFFORTTOESCAPETHEVILEWINDSLIPPEDQUICKLYTHROUGHTHEGLASSDOORSOFVICTORYMANSIONSTHOUGHNOTQUICKLYENOUGHTOPREVENTASWIRLOFGRITTYDUSTFROMENTERINGALONGWITHHIMTHEHALLWAYSMELTOFBOILEDCABBAGEANDOLDRAGMATSATONEENDOFITACOLOUREDPOSTERTOOLARGEFORINDOORDISPLAYHADBEENTACKEDTOTHEWALLITDEPICTEDSIMPLYANENORMOUSFACEMORETHANAMETREWIDETHEFACEOFAMANOFABOUTFORTYFIVEWITHAHEAVYBLACKMOUSTACHEANDRUGGEDLYHANDSOMEFEATURESWINSTONMADEFORTHESTAIRSITWASNOUSETRYINGTHELIFTEVENATTHEBESTOFTIMESITWASSELDOMWORKINGANDATPRESENTTHEELECTRICCURRENTWASCUTOFFDURINGDAYLIGHTHOURSITWASPARTOFTHEECONOMYDRIVEINPREPARATIONFORHATEWEEKTHEFLATWASSEVENFLIGHTSUPANDWINSTONWHOWASTHIRTYNINEANDHADAVARICOSEULCERABOVEHISRIGHTANKLEWENTSLOWLYRESTINGSEVERALTIMESONTHEWAYONEACHLANDINGOPPOSITETHELIFTSHAFTTHEPOSTERWITHTHEENORMOUSFACEGAZEDFROMTHEWALLITWASONEOFTHOSEPICTURESWHICHARESOCONTRIVEDTHATTHEEYESFOLLOWYOUABOUTWHENYOUMOVEBIGBROTHERISWATCHINGYOUTHECAPTIONBENEATHITRAN
// key = MATHSMATHSMATHSMATHS
//ITWASABRIGHTCOLDDAYINAPRILANDTHECLOCKSWERESTRIKINGTHIRTEENWINSTONSMITHHISCHINNUZZLEDINTOHISBREASTINANEFFORTTOESCAPETHEVILEWINDSLIPPEDQUICKLYTHROUGHTHEGLASSDOORSOFVICTORYMANSIONSTHOUGHNOTQUICKLYENOUGHTOPREVENTASWIRLOFGRITTYDUSTFROMENTERINGALONGWITHHIMTHEHALLWAYSMELTOFBOILEDCABBAGEANDOLDRAGMATSATONEENDOFITACOLOUREDPOSTERTOOLARGEFORINDOORDISPLAYHADBEENTACKEDTOTHEWALLITDEPICTEDSIMPLYANENORMOUSFACEMORETHANAMETREWIDETHEFACEOFAMANOFABOUTFORTYFIVEWITHAHEAVYBLACKMOUSTACHEANDRUGGEDLYHANDSOMEFEATURESWINSTONMADEFORTHESTAIRSITWASNOUSETRYINGTHELIFTEVENATTHEBESTOFTIMESITWASSELDOMWORKINGANDATPRESENTTHEELECTRICCURRENTWASCUTOFFDURINGDAYLIGHTHOURSITWASPARTOFTHEECONOMYDRIVEINPREPARATIONFORHATEWEEKTHEFLATWASSEVENFLIGHTSUPANDWINSTONWHOWASTHIRTYNINEANDHADAVARICOSEULCERABOVEHISRIGHTANKLEWENTSLOWLYRESTINGSEVERALTIMESONTHEWAYONEACHLANDINGOPPOSITETHELIFTSHAFTTHEPOSTERWITHTHEENORMOUSFACEGAZEDFROMTHEWALLITWASONEOFTHOSEPICTURESWHICHARESOCONTRIVEDTHATTHEEYESFOLLOWYOUABOUTWHENYOUMOVEBIGBROTHERISWATCHINGYOUTHECAPTIONBENEATHITRAN
  return 0;
}
