#!/usr/bin/env python
#-*- coding: utf-8 -*-

def selectionSort(llista):
    """
    retorna una nova llista ordenada segons el selection sort
    >>> selectionSort([2,5,4,7,22])
    [2, 4, 5, 7, 22]
    >>> selectionSort([10,9,8,10,4,3,5])
    [3, 4, 5, 8, 9, 10, 10]

    """
    b=llista[:]#o list(llista)
    for i in range(len(b)):
        pmin=i
        for j in range(i+1,len(b),1):
            if b[j]<b[pmin]:
                pmin=j
        b[i],b[pmin]=b[pmin],b[i]
    return b


def bubbleSort(llista):
    """

    >>> bubbleSort([2,5,4,7,22])
    [2, 4, 5, 7, 22]
    >>> bubbleSort([10,9,8,10,4,3,5])
    [3, 4, 5, 8, 9, 10, 10]

    :param lis:
    :return:
    """
    lis = list(llista)
    repeat = True
    while repeat:
        repeat=False
        for i in range(len(lis)-1):
            if(lis[i] > lis[i+1]):
                lis[i], lis[i+1] = lis[i+1],lis[i]
                repeat = True

    return lis







if (__name__ == "__main__"):
    a = [3,51,2,3,12,]
    b = bubbleSort(a)
