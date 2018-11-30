#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Node import *
from Estat import *

class Entrada(Node):
    """

    Aquesta classe és una especialització de la classe Node.
    Representa un node com a entrada.
    """
    def up(self):
        """
        força el node a estat alt
        """
        self.say(Estat(1))

    def down(self):
        """
        força el node a estat baix
        """

        self.say(Estat(0))

    def undef(self):
        """
        modifica el node a indefinit

        """
        self.say(Estat(-1))
    def __repr__(self):
        return super(Entrada,self).__repr__()+ ", Tipus: Entrada"

class Sortida(Node):
    """
    
    Aquesta classe és una especialització de la classe Node.
    Representa un node com a sortida.
    """
    def __repr__(self):
        return super(Sortida,self).__repr__()+ ", Tipus: Sortida"



if(__name__ == "__main__"):
    a=Entrada(Estat(1),"gub")
    e=Sortida(Estat(1),"tpm")
    print a
    print e