#!/usr/bin/env python
#-*- coding: utf-8 -*-



def llegirDades(fitxer):
    f = open(fitxer)
    for line in f:
        print line.split()[1]
    f.close()






if (__name__ == "__main__"):
    llegirDades(raw_input("Nom del fitxer: "))