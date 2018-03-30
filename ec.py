from gcdex import gcdex

class E:
    """Elliptic curve arithmetic.
    y^2 = x^3 + Ax + B mod p. Define A,B,p with E.params(A,B,p).
    Initialize with E(0) (for pt at infinity) or E(x,y).
    """

    A,B,p = 1,0,3 # some default initial values, class variables

    @classmethod
    def params(cls,A0,B0,p0):
        cls.A,cls.B,cls.p = A0,B0,p0
    
    def __init__(self, x, y=None):
        if y==None:
            if x!=0:
                raise TypeError
            self.P = 0
        else:
            self.P = (x,y)
    def __repr__(self):
        return(str(self.P))
    def __add__(self, b):
        if self.P==0:
            return b
        if b.P==0:
            return self

        p = E.p
        (Px,Py) = self.P
        (Qx,Qy) = b.P
        if Px==Qx and (Py+Qy)%p==0:
            return E(0)

        if Px==Qx and Py==Qy:
            (g,d,_) = gcdex(2*Py,p) # d is the inverse of 2*Py mod p
            if g!=1: 
                raise ArithmeticError(g)
            lam = ((3*Px*Px + E.A)*d) % p
        else:
            (g,d,_) = gcdex(Qx - Px,p)
            if g!=1: 
                raise ArithmeticError(g)
            lam = ((Qy - Py)*d) % p
                        
        x3 = (lam*lam - Px - Qx) % p
        return E(x3, (lam*(Px - x3) - Py) % p)
    def __neg__(self):
        if self.P==0:
            return self
        return(E(self.P[0], (-self.P[1])%E.p))
    def __sub__(self,b):
        return(self+(-b))
    def __rmul__(self,n):
        if not isinstance(n,int) and not isinstance(n,long):
            raise NotImplementedError
        if n<0:
            return((-n)*(-self))
        Q = self
        R = E(0)
        while(n != 0):
            if n&1:
                R = R+Q
            Q = Q+Q
            n >>= 1
        return R
    def __eq__(self, b):
        if b==0:
            return(self.P==0)
        if self.P==0:
            return(b.P==0)
        return(self.P[0]==b.P[0] and self.P[1]==b.P[1])
