#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
.. _usuari-link:

==============
Classe Usuari
==============

Gestiona un usuari utilitzant el banc avançat, nom i contrasenya.

    ======================= ============================================== ===============================
    Atribut                  Tipus                                           Significat
    ======================= ============================================== ===============================
    -bankAccount             :class:`iticBankAdvanced.BankAccountAmpliada`   BankAccountAmpliada de l'usuari
    +name                    string                                          Nom de l'usuari
    -passw                   string                                          Contrasenya de l'usuari
    ======================= ============================================== ===============================

Funcionament
------------

"""
from iticBankAdvanced import *
from getpass import getpass


def checkIfFloat(number):
    """
    Mira si un numero és float o no
    :param number: número donat
    :return: retorna true si és float i false si no
    """
    try:
        float(number)
        return True
    except ValueError:
        return False


class UsuariBank(object):
    """
    Aquesta classe gestiona un usuari d'un banc. Té funcions per autentificar, printejar la compta, depositar,retirar i
    aplicar el procés mensual.

    Per què un usuari entri s'autentifica amb un màxim de 3 intents i podrà depositar o retirar segons l'estat del seu
    compte.
    """
    def __init__(self, bankAdvanced, name, passw):
        self.__bankAccount = bankAdvanced
        self.name = name
        self.__passw = passw

    def __str__(self):
        return "Nom: " + self.name + " BankAccount: " + str(self.__bankAccount)
    def authentificate(self):
        """
        En aquesta funció t'autentifiques escrivint el nom i la contrasenya en 3 intents com a límit.
        :return: retorna true si accedeixes a la compta i false si no.
        """
        print "Per poder realitzar aquesta operacio, necessitem la teva contrassenya"
        i=0
        while i < 4:
            passw = getpass("Escriu la contrassenya: ")
            if(passw == self.__passw):
                return True
            i+=1
            if(i >= 3):
                break
            print "Contrassenya erronia, et queden {0} intents".format(3-i)
        print "Se t'han acabat els intents."
        return False

    def comptaBancaria(self):
        """
        Printeja les dades de la compta.
        """
        print self.__bankAccount

    def deposit(self):
        """
        Funció per ingressar diners al compte.

        """
        print "\nINGRESSAR DINERS A:",self.name,"\n"
        if(self.authentificate()):
            while True:
                x = raw_input("Quants diners vols ingressar? ")
                if(not checkIfFloat(x)):
                    print "Introdueixi un valor valid"
                else:
                    break
            self.__bankAccount.deposit(float(x))
            print "Diners:", self.__bankAccount.balance
        else:
            print "No t'has pogut autentificar correctament."

    def withdraw(self):
        """
        Funció per retirar diners. Si la teva compta està inactiva no pots retirar diners.

        """
        if(self.__bankAccount.status == False):
            print "La teva compta esta inactiva, no pots retirar diners."
            return
        print "\nRETIRAR DINERS DE:",self.name,"\n"
        if(self.authentificate()):
            while True:
                x = raw_input("Quants diners vols retirar? ")
                if(not checkIfFloat(x)):
                    print "Introdueixi un valor valid"
                else:
                    break
            self.__bankAccount.withdraw(float(x))
            print "Diners:", self.__bankAccount.balance
            if(self.__bankAccount.status):
                status = "Activa"
            else:
                status = "Inactiva"
            print "La teva compta esta:", status
        else:
            print "No t'has pogut autentificar correctament."
    def monthlyProcess(self):
        """
        Funció que aplica el procés mensual al compte.
        """
        self.__bankAccount.monthlyProcess()



if(__name__ == "__main__"):
    d ={}
    c1 = BankAccountAmpliada("ES6621000418401234567891", 100.0, 0.03, 2.5)
    u = UsuariBank(c1, "Ferran", "123")
    d[u.name] = u
    u.withdraw()
    u.comptaBancaria()
