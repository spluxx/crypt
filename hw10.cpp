#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;

int idx(char s) { return s - 'a'; }
int max(int a, int b) { return a > b ? a : b; }
bool isAscii(char c) { return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'); }

int main() {
  freopen("input4.txt", "r", stdin);
  int T = 0;
  vector<string> text;

  string s = "";
  char c;
  bool flag = false;
  while(scanf("%c", &c) != EOF) {
    if(!isAscii(c)) {
      if(!flag) { 
	text.push_back(s);
	flag = true; 
	s = ""; 
      } continue;
    } else flag = false;
    s += c >= 'a' ? c : c + 'a'-'A'; 
  }

  T = 0;
  int freq1[26];
  for(int i = 0 ; i < 26 ; i ++) freq1[i] = 0;
  for(int i = 0 ; i < text.size() ; i ++) {
    for(int j = 0 ; j < text[i].size() ; j ++) {
      freq1[idx(text[i][j])] ++;
      T ++;
    }
  }

  double entropy1 = 0;
  for(int i = 0 ; i < 26 ; i ++) {
    double pi = freq1[i]/(double)T; 
    if(freq1[i] == 0) continue;
    entropy1 -= pi*log2(pi);
  }

  T = 0;
  int freq2[26*26];
  for(int i = 0 ; i < 26*26 ; i ++) freq2[i] = 0;
  for(int i = 0 ; i < text.size() ; i ++) {
    for(int j = 0 ; j < max(text[i].size()-1, 0) ; j ++) {
      freq2[idx(text[i][j])*26+idx(text[i][j+1])] ++;
      T ++;
    }
  }

  double entropy2 = 0;
  for(int i = 0 ; i < 26*26 ; i ++) {
    double pi = freq2[i]/(double)T; 
    if(freq2[i] == 0) continue;
    entropy2 -= pi*log2(pi);
  }

  T = 0;
  int freq3[26*26*26];
  for(int i = 0 ; i < 26*26*26 ; i ++) freq3[i] = 0;
  for(int i = 0 ; i < text.size() ; i ++) {
    for(int j = 0 ; j < max(text[i].size()-2,0) ; j ++) {
      freq3[idx(text[i][j])*26*26+idx(text[i][j+1])*26+idx(text[i][j+2])] ++;
      T ++;
    }
  }

  double entropy3 = 0;
  for(int i = 0 ; i < 26*26*26 ; i ++) {
    double pi = freq3[i]/(double)T; 
    if(freq3[i] == 0) continue;
    entropy3 -= pi*log2(pi);
  }

  printf("1-GRAM\n");
  vector<pair<int, int> > ft1;
  for(int i = 0 ; i < 26 ; i ++) {
    ft1.push_back(make_pair(freq1[i], i));
  } sort(ft1.begin(), ft1.end());
  for(int i = ft1.size()-1 ; i >= 0 ; i --) {
    int index = ft1[i].second;
    printf("%c -> %d\n", index + 'a', ft1[i].first);
  }

  printf("2-GRAM\n");
  vector<pair<int, int> > ft2;
  for(int i = 0 ; i < 26*26 ; i ++) {
    ft2.push_back(make_pair(freq2[i], i));
  } sort(ft2.begin(), ft2.end());
  for(int i = ft2.size()-1 ; i >= ft2.size()-25 ; i --) {
    int index = ft2[i].second;
    printf("%c%c -> %d\n", index/26 + 'a', index%26 + 'a', ft2[i].first);
  }

  printf("3-GRAM\n");
  vector<pair<int, int > > ft3;
  for(int i = 0 ; i < 26*26*26 ; i ++) {
    ft3.push_back(make_pair(freq3[i], i));
  } sort(ft3.begin(), ft3.end());
  for(int i = ft3.size()-1 ; i >= ft3.size()-25 ; i --) {
    int index = ft3[i].second;
    printf("%c%c%c -> %d\n", index/(26*26) + 'a', index%(26*26)/26 + 'a', index%26 + 'a', ft3[i].first);
  }

  printf("ENTROPY\n");
  printf("H(L) =\t\t%lf\nH(L^2) =\t%lf\nH(L^3) =\t%lf\n", entropy1, entropy2, entropy3);
  printf("H(L) =\t\t%lf\nH(L^2)/2 =\t%lf\nH(L^3)/3 =\t%lf\n", entropy1, entropy2/2, entropy3/3);

  return 0;
}
