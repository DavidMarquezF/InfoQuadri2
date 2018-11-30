#!/usr/bin/env python
#-*- coding: utf-8 -*-
import BubleSort,Eines, HeapSort, MergeSort


def generaLlista(n):
    return Eines.crearLlista(n)

def ordenar(llista):
    Eines.resetRellotge()
    #BubleSort.bubbleSort(llista)
    #HeapSort.heapSort(llista)
    #MergeSort.mergeSort(llista)
    BubleSort.selectionSort(llista)
    return Eines.printRellotge()

def experiment(n, vegades = 1):
    print "Experiment {0} mostres".format(n)
    l = generaLlista(n)
    e = [ordenar(l) for i in range(vegades)]
    return sum(e)/len(e)

def experimentLlistesDiferents(n, vegades = 1, repeticioExperiment=1):
    e = [experiment(n,repeticioExperiment) for i in range(vegades)]
    return sum(e)/len(e)


def experimentMVegades(k): #k numero de vegades
    n=100
    nSalt=100
    counter = 1
    open("dades.dat","w").close()
    while n<=500000:

        tempsMitjana = experimentLlistesDiferents(n,k,5)


        f = open("dades.dat", "a")
        f.write("{0} {1}\n".format(n,tempsMitjana))
        f.close()

        print "Experiment de {0} vegades amb {1} mostres".format(k,n)
        n+=nSalt

        if(counter == 9):
            nSalt*=10
            counter=0
        counter +=1


if (__name__ == "__main__"):
    x = experiment(100,10)
    #print "--------------------------------------------------------------------",sum(x)/len(x)
    #y = experimentNVegades(100,100)

    #y =  experiment(1000,1000)
    #print sum(y)/len(y)

    experimentMVegades(100)