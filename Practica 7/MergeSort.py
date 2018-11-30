#!/usr/bin/env python
#-*- coding: utf-8 -*-

def mergeSort(l):
    """
    retorna una nova llista ordenada segons el merge sort
    >>> mergeSort([10,5,25,1,4,3,5,68,2,9])
    [1, 2, 3, 4, 5, 5, 9, 10, 25, 68]
    >>> mergeSort([256,44,32,56,2,134])
    [2, 32, 44, 56, 134, 256]
    """
    list = l[:]
    if len(list)>1:
        mid=len(list)/2
        lefthalf=list[:mid]
        righthalf=list[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k]=lefthalf[i]
                i+=1
            else:
                list[k]=righthalf[j]
                j+=1
            k+=1
        while i<len(lefthalf):
            list[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            list[k]=righthalf[j]
            j+=1
            k+=1
    return list
if (__name__ == "__main__"):
    l=[54,26,93,17,77,31,44,55,20]
    print mergeSort(l)


