#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
============
Mòdul Memory
============
"""

from bitVector import *
import MainLib
from avrException import AVRException

class OutOfMemError(AVRException):
    pass

class _Memory(object):
    """
    Aquesta classe representa un banc de memòria. La classe és abstracta i, per tant, no poden haver-
    hi objectes instanciats de la classe sinó que sempre ho són de les seves subclasses DataMemory i
    ProgramMemory.

    ======================= =============================== ===========================================================================================
    Atribut                  Tipus                              Significat
    ======================= =============================== ===========================================================================================
    -trace                      boolean                      Un bool que indica si la funcionalitat de traça està activada.
    -architecure               list                          Una llista de Word o Byte que representa el banc de memòria.
    ======================= =============================== ===========================================================================================

    """
    def __init__(self):
        self._m = []
        self._trace=False

    def getMem(self):
        return self._m

    def setMem(self, val):
        try:
            if(not isinstance(val, list)):
                raise TypeError()
            if(not isinstance(val[0], Byte) and not isinstance(val[0], Word)):
                raise TypeError()
        except TypeError:
            MainLib.exception("setMem(self, val) el valor ha de ser una llista de Bytes o Word", place="Memory (setMem)")
        self._m = val

    def traceOn(self):
        """
        Activa la funcionalitat trace. Aquesta funcionalitat permet traçar els accessos al banc de memoria
        """
        self._trace=True

    def traceOff(self):
        """
        Desactiva la funcionalitat trace. Aquesta funcionalitat permet traçar els accessos al banc de memoria
        """
        self._trace=False

    def __len__(self):
        return len(self.getMem())

    def __repr__(self):
        return self.dump(0,len(self.getMem()))

    def dump(self, f = 0, t = 5):
        """
        Retorna un str que conté un bolcat del banc de memòria exactament com en el cas de
        __repr__ però únicament de les cel.les que estan en l’interval d’adreces [f, t).

        :param f:From, a partir d'on es farà el bolcat
        :param t:To, fins a on es farà el bolcat
        :return: La string del bolcat
        """
        try:
            if(f > t or f < 0 or t < 0):
                raise ValueError("From ha de ser més gran que to")
        except ValueError as e:
            MainLib.exception(e.message, place="Memory (dump)")

        txt = []

        for i in range(f, t):
            txt.append("{0}: {1}".format(str(i).zfill(4), repr(self.getMem()[i]))) #TODO:Repassar que sigui tot correcte
        return "\n".join(txt)

    def __getSetTrace(self, write, value, memory):
        """
        Fa un Log de la informacio de quan trace està activat

        :param write: Si està en mode escriptura o lectura
        :param value: El valor llegit o escrit
        :param memory: D'on s'ha tret el valor (de quina memòria, registre)
        """
        if(self._trace):
            MainLib.logInfo("Memory", "{0} value {1} {2} memory {3}".format("Write" if write else "Read", value, "to" if write else "from",memory))

    def __checkIfAddrCorrect(self, addr, write):
        """
        Chequeja si l'addr és vàlid

        :param addr:
        :param write:
        """
        try:
            if(isinstance(addr, int)):
                if addr < 0 or addr > len(self.getMem()):
                    raise OutOfMemError()
            else:
                if  addr.__index__() < 0 or addr.__index__() > len(self.getMem()):
                    raise OutOfMemError()
        except OutOfMemError:
            MainLib.exception("{0} {1} out of range".format("Write to" if write else "Read from", str(addr.__index__()) if not isinstance(addr, int) else str(addr)), place="Memory ( __checkIfAddrCorrect)")

    def __getitem__(self, addr):
        self.__checkIfAddrCorrect(addr, False)
        val = self.getMem()[addr]
        self.__getSetTrace(False, val, str(addr)) #TODO:Comprobar que classes implementin __index__ i __str__
        return val

    def __setitem__(self, addr, value): #TODO: Gestionar excecions amb k???
        self.__checkIfAddrCorrect(addr, True)
        try:
            if(not isinstance(value, Byte) and not isinstance(value, Word)):
                raise TypeError()
        except TypeError:
            MainLib.exception("__setitem__, value ha de ser un Bitvector", place="Memory (__setitem__)")
        self.getMem()[addr.__index__()] = value
        self.__getSetTrace(True, value, str(addr))  # TODO:Comprobar que classes implementin __index__ i __str__




class ProgramMemory(_Memory):
    """
    Program memory: Hereta de Memory
    """

    def __init__(self, nCells=1024):
        super(ProgramMemory, self).__init__()
        self.setMem([Word() for i in range(nCells)])


class DataMemory(_Memory):
    """
    Data memory: Hereta de Memory


    """
    X = [27, 26]
    Y = [29, 28]
    Z = [31, 30]
    def __init__(self, nCells=1024):
        super(DataMemory, self).__init__()
        if nCells < 32:
            nCells = 32
        self.setMem([Byte() for i in range(nCells)])

    def dump_reg(self):
        """
        Retorna un str que representa els registres continguts en el banc de memòria en un
        format com el següent:

            R00: 00
            R01: 00
            ...
            R31: 00
            X(R27:R26): 0000
            Y(R29:R28): 0000
            Z(R31:R30): 0000

        :return: Una string amb tots els continguts dels registres
        """
        txt = []
        for reg in range(len(self)):
            txt.append("R{0}: {1}".format(str(reg).zfill(2), repr(self.getMem()[reg]))) #TODO:Repassar que sigui tot correcte
        txt.append("X(R{0}:R{1}): {2}".format(DataMemory.X[0], DataMemory.X[1], repr(self.getMem()[DataMemory.X[0]]) + repr(self.getMem()[DataMemory.X[1]])))
        txt.append("Y(R{0}:R{1}): {2}".format(DataMemory.Y[0], DataMemory.Y[1], repr(self.getMem()[DataMemory.Y[0]]) + repr(self.getMem()[DataMemory.Y[1]])))
        txt.append("Z(R{0}:R{1}): {2}".format(DataMemory.Z[0], DataMemory.Z[1], repr(self.getMem()[DataMemory.Z[0]]) + repr(self.getMem()[DataMemory.Z[1]])))

        return "\n".join(txt)



if(__name__ =="__main__"):
    a = DataMemory(32)
    a[35]