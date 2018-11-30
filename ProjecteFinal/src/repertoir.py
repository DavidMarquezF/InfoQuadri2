#coding=UTF-8

"""
====================
Mòdul Repertoir
====================

Conté una classe que agrupa el repertori d'instruccions del simulador.

"""

import avrException, MainLib

class UnknownCodeError(avrException.AVRException):
    """
    És una excepció que s'aixeca quan cal executar una instrucció de llenguatge màquina i aquesta
    no és coneguda.
    """
    pass

class Repertoir(object):
    """
    Repertoir és una classe les instàncies de la qual són conjunt de InstRunner's. Representen el
    conjunt d'instruccions d'un MCU. La seva funcionalitat més característica és la que, donada una
    instrucció, retorna l'objecte InstRunner que és capaç d'executar-la.
    """
    def __init__(self, li):
        """
        li és una llista d'instàncies d'InstRunner que constitueixen un repertori d'instruccions.
        """
        self._li = li
        self._inst_l = ""

    def find(self, instr):
        """
        Instr és un Word que denota una instrucció. El mètode retorna un objecte InstRunner
        capaç d'executar la instrucció instr. En cas que no existeixi cap InstRunner capaç
        d'executar la instrucció, aixeca l'excepció UnknownCodeError.

        :param instr: Word que denota una instrucció
        """
        for instruction in self._li:
            if instruction.match(instr):
                self._inst_l += str(instruction)+"\n"
                return instruction
        raise UnknownCodeError("Aquesta intruccio no existeix")

    def dump_log(self):
        """
        Retorna un str que conté les instruccions que s'han trobat des de la creació de la instancia

        :return: String que conté les instruccions.
        """
        return self._inst_l
