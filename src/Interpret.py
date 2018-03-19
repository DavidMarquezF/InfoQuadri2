#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
=======================================
Classe Intèrpret i Excepció d'interpret
=======================================

"""
class NoParam (Exception):
    pass



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
        self.__alpha = self.defaultStart
        self.__omega = self.defaultStop


    def defaultStart(self):
        print "Interpret started"
    def defaultStop(self):
        print "Interpret stopped"
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

    def setCustomHelp(self, c):
        self.customHelp = c



    def setBegin(self,f):
        """
        Fixa la funció f com l'inicialitzador que es cridarà just abans d'arrencar l'interpret. F és una funció sense
        paràmetres.

        :param f: La funció que es cridarà quan es comenci el interpret
        """
        self.__alpha = f

    def setEnd(self, f):
        """
        Fixa la funció f com el finalitzador que es cridarà just abans d'acabar l'execució l'interpret. F és una funció sense
        paràmetres.

        :param f: La funció que es cridarà quan es comenci el interpret
        """
        self.__omega = f


    def help(self):
        """
        Mostra per pantalla ajuda (si s'ha posat ajuda customitzada es mostrarà aquesta i si no una llista de les claus)
        """
        if(hasattr(self, "customHelp") and self.customHelp != None):
            try:
                self.customHelp()
            except:
                print "Interpret: Custom help must be a function with no parameters"
        else:
            keys = sorted(self.getDCom().keys())
            for key in keys:
                print key


    def run(self):
        """
        Arrenca l’execució d’aquest intèrpret d’ordres. L’intèrpret s’executa indefinidament fins
        que l’usuari escriu l’ordre surt.

        A cada cicle d’interpretació, l’intèrpret escriu el prompt, llegeix un string del teclat, l’anal-
        itza separant els mots que el formen. El primer mot considera que és un nom d’ordre i la
        resta de mots els paràmetres d’aquesta ordre. Finalment executa la funció corresponent a
        l’ordre i li passa com a paràmetre la resta de mots en una llista.
        """
        try:
            self.__alpha()
        except TypeError:
            print "Error: Alpha ha de ser una funció sense paràmetres"

        print "Per ajuda escriu - help"

        while True:
            x = raw_input(self.__prompt + " ")
            if(x == "surt" or x == "exit"):
                break
            if(x == "ajuda" or x == "help"):
                self.help()
            par = x.split()
            try:
                key = par[0]
                self.getDCom()[key]
                if(len(par) <= 1):
                    raise NoParam

            except IndexError:
                print "Has d'incloure una clau"
                continue
            except NoParam:
                print "Has d'incloure com a mínim un  paràmetre"
                continue
            except KeyError as e:
                print "La comanda " + e.message + " no existeix"

            else:
                param = [parameter for parameter in par[1:]]
                self.getDCom()[key](param)

        try:
            self.__omega()
        except TypeError as e:
            print "Error: Omega ha de ser una funció sense paràmetres",e.message