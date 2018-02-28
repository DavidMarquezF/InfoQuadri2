#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
=================
Classe Intèrpret
=================

"""
class Interpret(object):
    """
    Aquesta classe fa que de forma interactiva, es llegeixin ordres de l’usuari que haurà preparat previament
    i les vagi executant una a una.
    És un intèrpret d'ordres configurable.Això significa que per
    usar-lo primer cal configurar-lo. Configurar-lo consisteix a dir-li quines ordres ha de conèixer i
    què han de fer.

    .. code-block:: python

        >>> def c1(l): print "executo l’ordre 1: {0}".format(l[0])
        >>>
        >>> def c2(l): print "executo l’ordre 2: {0}".format(l[0])
        >>>
        >>> i = Interpret()
        >>> i.setPrompt("∗∗")
        >>> i.afegeixOrdre("llista", c1)
        >>> i.afegeixOrdre("bloqueja", c2)
        >>>
        >>> i.run()
        ∗∗ llista usuaris
        executo l’ordre 1: usuaris
        ∗∗ bloqueja pere
        executo l’ordre 2: pere
        ∗∗ surt
        >>>

    ======================= ========= =========================================================================
    Atribut                  Tipus                       Significat
    ======================= ========= =========================================================================
    -prompt                  string    Emmagatzema el prompt que usarà l’intèrpret.
    -dcom                    dict      És  el diccionari que emmagatzema les ordres conegudes per el intèrpret.
    ======================= ========= =========================================================================

    """
    def __init__(self):
        self.__prompt="Prompt Default"
        self.__dcom = dict()

    def getPrompt(self):
        return self.__prompt

    def getDCom(self):
        return self.__dcom

    def setPrompt(self, prompt):
        self.__prompt = prompt

    def afegeixOrdre(self, nomc, ordre):
        """
        Afegeix una ordre al diccionari d'ordres amb una clau
        :param nomc: La clau que s'utilitzarà per invocar la ordre
        :param ordre: La funció que s'emmagatzemarà amb la clau nomc (el paràmetre de la funció serà una llista de strings)
        """
        if(nomc in self.getDCom()):
            print "Aquesta clau ja existeix"
            return
        self.getDCom()[nomc] = ordre

    def run(self):
        """
        Arrenca l’execució d’aquest intèrpret d’ordres. L’intèrpret s’executa indefinidament fins
        que l’usuari escriu l’ordre surt.

        A cada cicle d’interpretació, l’intèrpret escriu el prompt, llegeix un string del teclat, l’anal-
        itza separant els mots que el formen. El primer mot considera que és un nom d’ordre i la
        resta de mots els paràmetres d’aquesta ordre. Finalment executa la funció corresponent a
        l’ordre i li passa com a paràmetre la resta de mots en una llista.
        """
        while True:
            x = raw_input(self.__prompt + " ")
            if(x == "surt" or x == "exit"):
                break
            par = x.split()
            if (len(par) <= 1):
                print "Has d'incloure parametres"
                continue
            key = par[0]
            if(key not in self.getDCom()):
                print "L'accio",key,"no existeix"
                continue

            param = [parameter for parameter in par[1:]]
            self.getDCom()[key](param)