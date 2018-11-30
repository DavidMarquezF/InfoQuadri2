# −∗− coding: utf−8 −∗−
"""
=============
Mòdul fracció
=============
"""
class NotFractionException(Exception):
    pass

class Fraccio(object):
    def __init__ (self, n, d=1):
        try:
            int(n)
            int(d)
        except ValueError:
            print "El numerador i denominador han de ser ints"
            exit()


        self.__num = n
        self.__den = d
        self.__simplifica()


    def getNum(self):
        return self.__num
    def getDen(self):
        return self.__den

    def __simplifica(self):
        a = abs(self.__num)
        b = abs(self.__den)
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        self.__num = self.__num / a
        self.__den = self.__den / a

    def __sub__ (self,a):
        try:
            nd = self.__den*a.getDen()
            nn = self.__num*a.getDen() - a.getNum()*self.__den
            return Fraccio(nn, nd)
        except AttributeError:
            print "Només pots restar dos objectes Fraccio"
            return None
        except Exception as e:
            print "Excepció no gestionada: " + e.message
            return None


    def __neg__(self):
        return Fraccio(-self.__num, self.__den)
    def __add__(self, a):
        try:
            nd = self.__den*a.getDen()
            nn = self.__num*a.getDen() + a.getNum() *self.__den
            return Fraccio(nn, nd)
        except AttributeError:
            print "Només pots sumar dos objectes Fraccio"
            return None
        except Exception as e:
            print "Excepció no gestionada: " + e.message
            return None

    def __mul__(self, other):
        try:
            return  Fraccio (self.__num * other.getNum(), self.__den * other.getDen())
        except AttributeError:
            print "Només pots multiplicar dos objectes Fraccio"
            return None
        except Exception as e:
            print "Excepció no gestionada: " + e.message
            return None
    def __div__(self, other):
        try:
            return Fraccio(self.__num * other.getDen(), self.__den * other.getNum())
        except AttributeError:
            print "Només pots dividir dos objectes Fraccio"
            return None
        except Exception as e:
            print "Excepció no gestionada: " + e.message
            return None

    def __repr__(self):
        if self.__num==self.__den:
            return '1'
        elif self.__den==1:
            return('{0}'.format(self.__num))
        else:
            return str(('{0}/{1}'.format(self.__num, self.__den)))



if(__name__ == "__main__"):
    f = Fraccio(2,4)
    print repr(f)
    f1 = Fraccio(3,4)
    print repr(f1)
    f2 = f * f1
    print repr(f2)
    f3 = f / f1
    print repr(f3)
    f4 = f + f1
    print repr(f4)
    f5= f -f1
    print repr(f5)
    print repr(-f)