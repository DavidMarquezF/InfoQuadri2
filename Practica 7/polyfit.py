import numpy
from matplotlib.pyplot import *


def Polyfit():
    dades=raw_input("quin fitxer vols obrir?: ")
    f=open(dades)
    x = []
    y = []
    for linia in f:
        s = linia.split()
        x.append(float(s[0]))
        y.append(float(s[1]))
    f.close()

    coeficients=numpy.polyfit(x[:],y[:], 2)
    polynomial=numpy.poly1d(coeficients)
    ys=polynomial(x)
    print coeficients
    print polynomial

    plot(x,y,"o")
    plot(x,ys)
    ylabel('t(s)')
    xlabel('n')
    show()
if __name__ =="__main__":
    Polyfit()