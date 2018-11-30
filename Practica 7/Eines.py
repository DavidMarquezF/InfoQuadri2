#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random,time

def crearLlista(n):
    return [random.randint(0, 2*n) for i in range(n)]


Inici = 0

def resetRellotge():
    global Inici
    Inici = time.clock()

def printRellotge():
    t = time.clock() - Inici
    #print t
    return t


if (__name__ == "__main__"):
    resetRellotge()
    print crearLlista(20000)
    printRellotge()