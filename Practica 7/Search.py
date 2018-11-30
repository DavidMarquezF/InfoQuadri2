import random,Eines, MergeSort

def cercaBruta(l,n):
    for e in l:
        if e==n:
            return True
    return False

def cercaBinaria(llista,element):#la llista ha d'estar ordenada previament
    primer=0
    final=len(llista)
    trobat=False
    while primer<final and not trobat:
        index=(primer+final)/2
        if element==llista[index]:
            trobat=True
        elif element<llista[index]:
            final=index-1
        else:
            primer=index+1
    return trobat

def cercaBinariaRec(l, element):
    """

    >>> cercaBinariaRec([1,2,3,4,5,6,7,8,9,10], 1)
    True

    :param l:
    :param element:
    :return:
    """
    if(len(l) == 0):
        return False
    if(element == l[len(l)/2]):
        return True
    else:
        if(element < l[len(l)/2]):
            return cercaBinariaRec(l[:len(l)/2], element)
        else:
            return cercaBinariaRec(l[len(l)/2 + 1:], element)

def elementRandom(tamany):
    return random.randint(0,2*tamany)

def cerca(l,n):
    Eines.resetRellotge()
    elem = elementRandom(n)
    cercaBinariaRec(l,elem)
    return Eines.printRellotge()

def experiment(n, vegades = 1):
    print "Experiment {0} mostres".format(n)
    l = Eines.crearLlista(n)
    l = MergeSort.mergeSort(l)
    e = [cerca(l,n) for i in range(vegades)]
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

        tempsMitjana = experimentLlistesDiferents(n,k,10)


        f = open("dades.dat", "a")
        f.write("{0} {1}\n".format(n,tempsMitjana))
        f.close()

        print "Experiment de {0} vegades amb {1} mostres".format(k,n)
        n+=nSalt

        if(counter == 9):
            nSalt*=10
            counter=0
        counter +=1
if(__name__=="__main__"):
    experimentMVegades(100)