# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Triport import *
from Tickable import Tickable
import copy


class Component(Tickable):
    """

    Un component és, com al VHDL una entitat amb unes entrades i sortides que gestiona internament.

    Com que deriva de :class:`Tickable.Tickable` ha d'implementar la funció tick

    Cada component actua com un circuit: té un supervisor que es fa anar continuament fins que no varien els nodes.
    Si quan s'ha acabat el run del component, les sortides han canviat, s'avisarà als supervisors de tot el circuit que
    el circuit ha variat.

    ======================= =============================== ===========================================================================================
    Atribut                  Tipus                              Significat
    ======================= =============================== ===========================================================================================
    +name                    string                         Nom del component
    -entrades                dict                           Diccionari amb les entrades del component (key = nom, value = :class:`Entrada.Entrada`)
    -sortides                dict                           Diccionari amb les sortides del component (key = nom, value = :class:`Entrada.Sortida`)
    -architecure               list                         Llista dels  nodes i triports que formen aquest component
    -supervisor              :class:`Supervisor.Supervisor` El supervisor privat d'aquest component
    ======================= =============================== ===========================================================================================

    """
    def __init__(self, entrades, sortides, name):
        self.name = name
        self.__entrades = entrades
        self.__sortides=sortides
        self.__architecture = []
        self.__supervisor = None

    def AddArchitecture(self, circuit, supervisor):
        """
        S'utilitza per afegir l'arquitecura del component (el circuit intern)

        :param circuit: llista de nodes i triports
        :param supervisor: El supervisor que es farà anar al component
        """
        self.__architecture = circuit
        self.__supervisor = supervisor

    def __repr__(self):
        txtEntrades =""
        txtSortides=""
        for entrada in self.__entrades:
            txtEntrades += str(self.__entrades[entrada]) + "; "
        for sortida in self.__sortides:
            txtSortides += sortida+": " + str(self.__sortides[sortida])
        return "Component {0}, Entrades: {1}, Sortides: {2}".format(self.name, txtEntrades, txtSortides)

    def _tick(self):
        """
        Funció que calcula a partir de les entrades les sortides del component utilitzant el supervisor privat.

        Si quan s'ha calculat les sortides aquestes no són iguals que anteriorment s'avisa a tots els supervisors que
        hi ha hagut un canvi (d'aquesta manera els supervisors a menys profunditat del circuit ho podran saber i actuar
        consequentment).

        """
        sortides = copy.deepcopy(self.__sortides)
        self.__supervisor.run()
        try:
            for key, prevValue in sortides.items():
                for key2, val in self.__sortides.items():
                    if(key == key2):
                        if(prevValue.ask() !=val.ask()):
                            Supervisor.Changed = True
        except:
            print "Error while actualizing values in component"
            exit()


    def Entrades(self):
        return self.__entrades

    def GetNameOuts(self):
        """
        :return: Retorna els noms de les sortides
        """
        return self.__sortides.keys

    def GetNameIns(self):
        """
        :return: Retorna els noms de les entrades
        """
        return self.__entrades.keys

    def GetEntrada(self, key):
        """
        A partir del nom de l'entrada retorna aquesta. Si la clau no existeix el programa es pararà

        :param key: L'identificador de l'entrada (nom)
        :return: retorna l'entrada corresponent a aquella clau.
        """
        try:
            return self.__entrades[key]
        except:
            print "Error - No hi ha cap entrada amb aquesta clau:",key
            exit()

    def GetSortida(self, key):
        """
        A partir del nom de la sortida retorna aquesta. Si la clau no existeix el programa es pararà

        :param key: L'identificador de la sortida (nom)
        :return: retorna l'entrada corresponent a aquella clau.
        """
        try:
            return self.__sortides[key]
        except:
            print "Error - No hi ha cap sortida amb aquesta clau:",key
            exit()