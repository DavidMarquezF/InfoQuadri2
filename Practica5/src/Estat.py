#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Estat(object):
    """

    Aquesta classe defineix els diferents estats possibles, baix, alt o indefinit.

    ======================= =============================== ============================
    Atribut                  Tipus                              Significat
    ======================= =============================== ============================
    -e                        int                             És l'estat (0, 1 o -1)
    ======================= =============================== ============================

    """

    def __init__(self, e = -1):
        self.__e=e

    def __nonzero__(self):
        return not self.__e==-1

    def getEstat(self):
        return self.__e

    def __eq__(self, other):
        return self.__e == other.getEstat()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __and__(self, other):
        """

        :param other: estat amb el que fer la operació
        :return: retorna el resultat de fer una AND entre 2 estats
        """
        if(self.undef()):
            return Estat(-1)
        return Estat(self.__e and other.getEstat())

    def __or__(self, other):
        """

        :param other: estat amb el que fer la operació
        :return: retorna el resultat de fer una OR entre 2 estats
        """
        if(self.undef()):
            return Estat(-1)
        return Estat(self.__e or other.getEstat())

    def __repr__(self):
        return "State value " + str(self.__e)

    def __invert__(self):
        """

        :return: inverteix l'estat
        """
        if (self.undef()):
            return Estat(-1)
        return Estat(1 - self.__e)

    def undef(self):
        return not self

if __name__ == "__main__":
    print ~Estat(0)
    print ~Estat()
    e = Estat(1)
    e1 = Estat(0)
    print e|e1
    print e&e1
    print Estat()&e1
    print Estat()|e
