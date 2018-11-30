#!/usr/bin/env python
#-*- coding: utf-8 -*-
import datetime, copy
class OutOfOrderException(Exception):
    pass
class Dataset(object):
    """

    ======================= =============================== ===========================================================================================
    Atribut                  Tipus                            Significat
    ======================= =============================== ===========================================================================================
    -name                    string                           És el nom del dataset. Cada objecte té un nom que l’identifica.
    -ds                      list                             És una llista de tuples (t,v) on t és un temps i v el valor d’un sensor en aquest
                                                               temps. t és un objecte de tipus datetime
    ======================= =============================== ===========================================================================================


    """
    def __init__(self,n=''):
        self.__name=n
        self.__ds=[]       #(Data,valor)

    def getDs(self):
        return self.__ds
    def getName(self):
        return self.__name

    def __len__(self):
        return len(self.__ds)

    def __str__(self):
        text="\033[1;32mDataset: {0}\033[1;m\n".format(self.__name)
        if(len(self.__ds) <= 0):
            text+="\tNo hi ha cap dada"
        else:
            for e in self.__ds:
                 text+="\t\033[1;35mTemps:\033[1;m " +str(e[0]) +"  \033[1;33mValor:\033[1;m " + str(e[1]) + "\n"
        return text.rstrip()

    def add(self,t,v):
        """
        Afegeix una nova dada (datetime, valor) al dataset. Si el temps d'aquesta dada es menor a l'ultim que hi ha en la llista de dades
        es disparara una OutOfOrderException

        :param t: El temps de la dada :class:`datetime.datetime`
        :param v: El valor registrat

        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 100)
        >>> d.add(datetime.datetime(2,1,1), 200)
        >>> d.add(datetime.datetime(2,1,1), 300)
        L'observacio no esta feta en un temps posterior a l'ultima dada del dataset
        """
        try:
            if(len(self.__ds) > 0):
                if self.__ds[-1][0] >= t:
                    raise OutOfOrderException()

            self.__ds.append((t,v))
        except OutOfOrderException:
            print "\033[93mWarning\033[1;m - L'observacio no esta feta en un temps posterior a l'ultima dada del dataset:\n\tLast: {0}\n\tCurrent: {1}".format((str(self.__ds[-1][0]), self.__ds[-1][1]), (str(t),v))




    def timeVector(self):
        """

        :return: Retorna una llista de tots els temps ordenats de menor a major

        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 100)
        >>> d.add(datetime.datetime(2,1,1), 200)
        >>> d.timeVector()
        [datetime.datetime(1, 1, 1, 0, 0), datetime.datetime(2, 1, 1, 0, 0)]
        """
        return  [dataset[0] for dataset in self.__ds]

    def valueVector(self):
        """

        :return: Retorna una llsita de tots els valors ordenats cronologicament

        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 200)
        >>> d.add(datetime.datetime(2,1,1), 100)
        >>> d.valueVector()
        [200, 100]
        """
        return [dataset[1] for dataset in self.__ds]


    def decimate(self, k=10):
        """
        Crida la funcio protegida decimate per obtenir una llista de dades i les afegeix a un nou dataset.

        :param k: El nombre amb el que haura d'anar agrupant
        :return: Un nou :class:`dataset.Dataset`

        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 100)
        >>> d.add(datetime.datetime(2,1,1), 200)
        >>> print d.decimate()
        Dataset:
        Temps: 0002-01-01 00:00:00  Valor: 150
        """
        d = Dataset(self.__name)
        for data in self._decimate(k):
            d.add(data[0], data[1])
        return d

    def _decimate(self, k=10, llista=None):
        """
        A partir de la llista de dades dins de self retorna una llista on cada element resulta d'agrupar els elements originals de self
        agafats de k en k i representar-los per un nou element que te per valor la mitjana dels
        originals i per temps el mes gran dels originals.

        :param k: De quant en quant agafem les dades
        :param llista: Utilitzat per a fer la recursivitat
        :return: Llista de dades


        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 100)
        >>> d.add(datetime.datetime(2,1,1), 200)
        >>> print d._decimate()
        [(datetime.datetime(2, 1, 1, 0, 0), 150)]
        """
        if (llista == None):
            llista = self.__ds

        if llista == []:
            return []
        elif len(llista) < k:
            return [(llista[-1][0], sum([val[1] for val in llista]) / len(llista))]
        else:
            return [(llista[k - 1][0], sum([val[1] for val in llista[:k]]) / k)] + self._decimate(k, llista[k:])

    def movingAverage(self, k = 50):
        """
        Crida la funcio protegida moviningAverage per obtenir una llista de dades i les afegeix a un nou dataset.

        :param k: El nombre amb el que haura d'anar agrupant per fer les mitjanes
        :return: Un nou :class:`dataset.Dataset`

        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 100)
        >>> d.add(datetime.datetime(2,1,1), 200)
        >>> d.add(datetime.datetime(3,1,1), 200)
        >>> print d.movingAverage()
        """
        d = Dataset(self.__name)
        for data in self._movingAverage(k):
            d.add(data[0], data[1])
        return d

    def _movingAverage(self, k=50, llista = None):
        """
        Calcula un nou DataSet on cada element resulta de calcular la mitjana mobil. Es a dir
        substituim cada element per la mitjana dels k elements anteriors.

        :param k: Nombre de quants en quants t'haura d'agafar els valors per fer la mitjana
        :param llista: Utilitzat per a fer la recursivitat
        :return: Llista de dades

        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 100)
        >>> d.add(datetime.datetime(2,1,1), 200)
        >>> print d._movingAverage()
        [(datetime.datetime(1, 1, 1, 0, 0), 150), (datetime.datetime(2, 1, 1, 0, 0), 150)]
        """
        if (llista == None):
            llista = copy.deepcopy(self.__ds)

        if llista == []:
            return []
        elif len(llista) < k:
            return []
        else:
            return [(llista[0][0], sum([val[1] for val in llista[:k]]) / k)] + self._movingAverage(k, llista[1:])

    def concat(self,ds2):
        """
        Afegeix a self el DataSet ds2. La primera observacio de ds2 ha de ser posterior a la darrera
        de self. Altrament s'aixeca l'excepcio OutOfOrderException.

        :param ds2: El segon dataset a afegir


        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 100)
        >>> d.add(datetime.datetime(2,1,1), 200)
        >>> d2 = Dataset("test2")
        >>> d2.add(datetime.datetime(3,1,1), 100)
        >>> d2.add(datetime.datetime(4,1,1), 200)
        >>> d.concat(d2)
        >>> print d
        Dataset:
        Temps: 0001-01-01 00:00:00  Valor: 100
        Temps: 0002-01-01 00:00:00  Valor: 200
        Temps: 0003-01-01 00:00:00  Valor: 100
        Temps: 0004-01-01 00:00:00  Valor: 200
        """
        l = ds2.getDs()
        if(len(ds2) == 0):
            return
        try:
            if(l[0][0] <= self.__ds[-1][0] ):
                raise OutOfOrderException()

            for d in l:
                self.add(d[0], d[1])
        except OutOfOrderException:
            print "La observacio no esta feta en un temps posterior a l'ultima observacio del dataset"
            exit()
        return self

    def transform(self, a =1.0, b=0.0):
        """
        Modifica self tot aplicant al valor v de cada observacio la transformacio lineal a*v + b.

        :param a: Valor a
        :param b: Valor b

        >>> d = Dataset("test")
        >>> d.add(datetime.datetime(1,1,1), 100)
        >>> d.add(datetime.datetime(2,1,1), 200)
        >>> d.transform(2)
        >>> print d
        Dataset:
        Temps: 0001-01-01 00:00:00  Valor: 200.0
        Temps: 0002-01-01 00:00:00  Valor: 400.0
        """
        newDs =[]
        for val in self.__ds:
            newDs.append((val[0],a * val[1] + b))
        self.__ds = newDs




if(__name__=="__main__"):
    d = Dataset("hola")
    print d.decimate()

