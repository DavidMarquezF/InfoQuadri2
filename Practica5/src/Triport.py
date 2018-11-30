#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Entrada import *
from Estat import *
from Tickable import Tickable
class Triport (Tickable):
    """

    Un triport és un component de lògica combinacional que consta de dos entrades i una sortida.

    La classe triport deriva de la classe Tickable, la qual cosa implica que haurà d'implementar la funció self._tick.

    ======================= =============================== ===========================================================================================
    Atribut                  Tipus                              Significat
    ======================= =============================== ===========================================================================================
    -in1                        :class:`Entrada.Entrada`        És l'entrada 1 del component
    -in2                        :class:`Entrada.Entrada`        És l'entrada 2 del component
    -out                        :class:`Entrada.Sortida`        És la sortida del circuit
    ======================= =============================== ===========================================================================================

    """
    def __init__(self, in1, in2,out):
        self.__in1 = in1
        self.__in2 = in2
        self.__out = out

    def _tick(self):
        """
        Funció obligada per la classe mare Tickable. Calcula la sortida a partir de les entrades del triport

        Obliga a que les classes filles d'aquesta implementin _doFunction (funció abstracte), que a partir de dos estats
        de les entrades calcula la sortida
        """
        self.__out.say(self._doFunction(self.__in1.ask(), self.__in2.ask()))

    def __repr__(self):
        return "Entrada 1: Nom:{0} Estat: {1}, Entrada 2: Nom:{2} Estat: {3}, Sortida: Nom:{4} Estat: {5}".format(self.__in1.getName(),self.__in1.ask(),self.__in2.getName(),self.__in2.ask(),self.__out.getName(),self.__out.ask())

class And(Triport):
    """
    Classe encarregada de fer l'operació AND. Té les mateixes variables que la seva classe mare (Triport).
    """
    def _doFunction(self,e1,e2):
        """
        Calcula la sortida a partir de dos estats

        :param e1: Estat 1
        :param e2: Estat 2
        :return: retorna el resultat de fer la operació AND a dues entrades
        """
        return e1&e2
    def get_Name(self):
        return "And"

    def __repr__(self):
        return "Type: " + self.get_Name() + " " + super(And, self).__repr__()

class XOR(Triport):
    """
    

    Classe encarregada de fer l'operació XOR. Té les mateixes variables que la seva classe mare (Triport).
    """
    def _doFunction(self, e1,e2):
        """
        Calcula la sortida a partir de dos estats

        :param e1: Estat 1
        :param e2: Estat 2
        :return: retorna el resultat de la XOR
        """
        return (~(e1&e2) & (e1|e2))

    def get_Name(self):
        return "XOR"

    def __repr__(self):
        return "Type: " + self.get_Name() + " " + super(XOR, self).__repr__()


class Or(Triport):
    """

    Classe encarregada de fer una OR. Té les mateixes variables que la seva classe mare (Triport).
    """

    def _doFunction(self,e1,e2):
        """
        Calcula la sortida a partir de dos estats

        :param e1: Estat 1
        :param e2: Estat 2
        :return: retorna el resultat de fer una OR
        """
        return e1|e2
    def get_Name(self):
        return "Or"

    def __repr__(self):
        return super(Or, self).__repr__() + " Type: " + self.get_Name()





if __name__=='__main__':
    a=And(Entrada("in1", Estat(1)),Entrada("in2", Estat(0)),Sortida("out", Estat(-1)))
    a.tick()
    print a

    b=And(Entrada("in1",Estat(1)),Entrada("in2",Estat(1)),Sortida("out",Estat(-1)))
    b.tick()
    print b

    c=And(Entrada("in1", Estat(0)),Entrada("in2", Estat(0)),Entrada("out", Estat(-1)))
    c.tick()
    print c


    d=Or(Entrada("in1",Estat(0)),Entrada("in2", Estat(0)),Entrada("out",Estat(-1)))
    d.tick()
    print d

    e=Or(Entrada("in1",Estat(1)),Entrada("in2", Estat(0)),Entrada("out", Estat(-1)))
    e.tick()
    print e

    print "XOR"
    d = XOR(Entrada("in1", Estat(0)), Entrada("in2", Estat(0)), Entrada("out", Estat(-1)))
    d.tick()
    print d

    d = XOR(Entrada("in1", Estat(1)), Entrada("in2", Estat(0)), Entrada("out", Estat(-1)))
    d.tick()
    print d

    d = XOR(Entrada("in1", Estat(0)), Entrada("in2",Estat(1)), Entrada("out",Estat(-1)))
    d.tick()
    print d


    d = XOR(Entrada("in1",Estat(1)), Entrada("in2",Estat(1)), Entrada("out",Estat(-1)))
    d.tick()
    print d

