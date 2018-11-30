#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
AVRMCU
=========

Aquest mòdul conté les següents classes:

Avrmcu():
-----------

Aquesta classe representa el simulador del Avr s'encerraga d'executar el programar i retornar les dades respectives segons es vagi demanant

    ======================== =========== ====================================================================
    Atributs                  Tipus       Significat
    ======================== =========== ====================================================================
    d                         int         Conté el tamany de la memoria de dades
    lp                        int         Conté el tamany de la memoria de programa
    _s                        State       Objecte de la classe State ja documentada al seu mòdul
    _rep                      Repertoir   Objecte de la classe Repertoir ja documentat al seu respectiu mòdul
    ======================== =========== ====================================================================
    

Funcions
---------

"""

import bitVector
from memory import*
from state import *
from repertoir import *
from instruction import *
class Avrmcu(object):
    
    def __init__(self, data=128, prog=128):
        self.d=data
        self.lp=prog
        self._s=State(data,prog)
        self._rep=Repertoir([ADD(),ADC(),AND(),OR(),MOV(),SUBI(),SUB(),EOR(),LSR(),LDI(),RJMP(),BRBS(),BRBC(),NOP(),BREAK(),IN(),OUT(),LDS(),STS()])
        
    def reset(self):
        self._s=State(self.d,self.lp)
    
    def set_prog(self,p):
        m=[]
        try:
            if len(p) > len(self._s.prog):
                raise OutOfMemError("El programa es massa llarg")
            else:
                for i in range(len(p)):
                    m+=[bitVector.Word(p[i])]
                self._s.prog.setMem(m)
        except OutOfMemError as e:
            MainLib.exception(e.message, place="AVRMcu (set_prog)")
    
    def dump_dat(self):
        return self._s.dump_Dat()
    
    def dump_prog(self):
        return self._s.dump_prog()
    
    def dump_reg(self):
        return self._s.dump_reg()
    
    def run(self):
        try:
            while True:
                instruction = self._rep.find(self._s.prog[self._s.pc])
                instruction.execute(self._s.prog[self._s.pc],self._s)
        except UnknownCodeError as e:
            MainLib.exception(e.message, place="AVR MCU (run)")
        except BreakException as e:
            MainLib.logInfo("Break", e.message)

    def set_trace(self,t):
        if not t:
            self._s.data.traceOff()
        else:
            self._s.data.traceOn()

if __name__=="__main__":
    avr = Avrmcu(prog=8)
    avr.set_prog([0b1110111101100011,0b1110011100010001,0b00001100100010001,0x2e01,0x2200,0x9598])
    print avr.dump_prog()
    avr.set_trace(True)
    avr.run()
    print avr.dump_reg()
