#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
==============
Mòdul State
==============
"""
from bitVector import *
from memory import *

class State(object):
    """
    Aquesta classe representa l’estat de la MCU. L’estat d’un computador està format pel conjunt
    de tots els registres i memòries. Cada vegada que s’executa una instrucció, l’estat acostuma a
    canviar.

    ======================= =================================== ===========================================================================================
    Atribut                  Tipus                               Significat
    ======================= =================================== ===========================================================================================
    +data                    Objecte de  classe DataMemory       És el banc de memòria de dades de l’AVR.
    +prog                    Objecte de  classe ProgramMemory    És el banc de memòria de programa de l’AVR.
    +pc                      Objecte de classe Word              És un Word que implementa el registre comptador de programa (Program Counter ).
    +flags                   Objecte de classe Byte              És un Byte que implementa el registre d’estat (status). Cada bit és un flag d’estat. En
                                                                 aquest simulador només s’usen els flags que es defineixen a la taula 1. S’hi accedeix a
                                                                 través d’unes constants que cal definir en el mòdul state de nom CARRY, ZERO i NEG
                                                                 que permeten indexar fàcilment aquest atribut públic.
    ======================= =================================== ===========================================================================================

    """


    def __init__(self,data=128,prog=128):
        """
        Inicialitza l’estat de la MCU. data és el nombre de cel·les de la memòria
        de dades i prog el nombre de cel·les de la memòria de programa.

        :param data:
        :param prog:
        """
        self.data=DataMemory(data)
        self.prog=ProgramMemory(prog)
        self.pc=Word(0)
        self.flags=Byte(0)


    def dump_Dat(self):
        """
        Retorna un str que representa el bolcat de la memòria de dades.

        :return: String del bolcat
        """
        return repr(self.data)

    def dump_prog(self):
        """
        Retorna un str que representa el bolcat de la memòria de programa.

        :return: String del bolcat
        """
        return repr(self.prog)

    def dump_reg(self):
        """
        Retorna un str que representa els registres continguts en l’estat. Això inclou també
        PC i flags. El format ha de ser similar a:

            R00: 00
            R01: 00
            ...
            R31: 00
            X(R27:R26): 0000
            Y(R29:R28): 0000
            Z(R31:R30): 0000
            PC: 0000
            CARRY: 0 ZERO: 0 NEG: 0

        :return: String del bolcat
        """
        x = self.data.dump_reg()

        return x+"\nPC: "+str(self.pc)+"\n"+"CARRY: "+str(int(self.flags[0]))+" ZERO: "+str(int(self.flags[1]))+" NEG: "+str(int(self.flags[2]))

if __name__=='__main__':
    c=State()
    #print c.dump_Dat()
    #print c.dump_prog()
    print c.dump_reg()

