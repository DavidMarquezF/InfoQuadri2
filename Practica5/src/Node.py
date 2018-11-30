#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Estat import Estat
from Supervisor import Supervisor


class Node(object):
    """
    Aquesta classe s'encarrega de rebre les entrades i sortides dels nodes i modificarlos i informar al supervisor.
    Un node sempre té un estat.

    ======================= =============================== ===========================================================================================
    Atribut                  Tipus                              Significat
    ======================= =============================== ===========================================================================================
    -e                        :class:`Estat.Estat`              És l'estat del node
    -n                        string                             És el nom del node
    -s                       :class:`Supervisor.Supervisor`        És el supervisor del node
    ======================= =============================== ===========================================================================================


    """
    def __init__(self, name, e = Estat()):
        self.__e = e
        self.__n = name
        self.__s = None

    def getName(self):
        return self.__n

    def say(self, e):
        """
        La funció serveix per modificar el node self. Si el nou estat e és diferent a l'estat que hi havia, n'informa al
        supervisor.

        :param e: És l'estat del node que vols
        """
        if(self.__e != e):
            try:
                self.__s.notifyChange()
            except AttributeError:
                print "El node no te cap supervisor",self.__n
        self.__e = e

    def ask(self):
        """

        :return: retorna l'Estat del node
        """
        return self.__e

    def setSupervisor(self, s):
        self.__s = s

    def hasSup(self):
        return self.__s != None

    def __repr__(self):
        return "Node: {0}, Estat: {1}, Supervisor: {2}".format(self.__n, self.__e, self.hasSup())


if __name__ == "__main__":
    n = Node("4232")
    n.setSupervisor(Supervisor())
    print n
    print n.ask()
    print "---"
    n.say(Estat())
