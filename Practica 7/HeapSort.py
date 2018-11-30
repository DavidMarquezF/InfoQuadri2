def heapify(llista,count, i):
    """
    S'encarrega de crear la heap d'una llista en O(n) operacions

    :param llista:
    :param count:
    :return:
    """
    major = i
    left = 2*i + 1
    right = 2*i + 2

    #Si el de l'esquerra es mes gra
    if(left < count and llista[left] > llista[major]):
        major = left

    #Si el de la dreta es mes gran
    if (right < count and llista[right] > llista[major]):
        major = right

    if(major != i):
        llista[i],llista[major] = llista[major],llista[i]
        heapify(llista, count,major)

def heapSort(llista):
    llistaCop = llista[:]
    count = len(llistaCop)
    i = count/2 - 1
    while i >=0:
        heapify(llistaCop, count, i)
        i-=1

    for i in range(count-1, 0, -1):
        llistaCop[0],llistaCop[i] = llistaCop[i], llistaCop[0]
        heapify(llistaCop, i, 0)


if __name__ == "__main__":
    x = [4,1,2,512,5,6,7,7,2,24,55]
    heapSort(x)
    print x
