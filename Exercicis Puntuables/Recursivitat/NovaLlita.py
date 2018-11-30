def novaLlista(llista, k):
    if(llista == []):
        return []
    if(len(llista) < k):
        return [sum(llista)/len(llista)]
    return [sum(llista[:k])/k] + novaLlista(llista[k:],k)

def OrderminToMax(list):
    if(list == []):
        return []
    if(len(list) == 1):
        return list
    k = min(list)
    list.remove(k)
    return [k] + list


def sumaElementsLlistes(llista):
    """

    >>> sumaElementsLlistes([[1,4],[2,8], [3,1,1]])
    20
    >>> sumaElementsLlistes([[[2],[1]], [2,4], [[3,4], [1,0,-1]]])
    16
    """
    s = 0
    if(isinstance(llista,int)):
        return llista
    for i in range(len(llista)):
        s += sumaElementsLlistes(llista[i])
    return s
