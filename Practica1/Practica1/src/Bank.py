#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
.. _bank-link:

===========
Classe Bank
===========

Gesiona una banc utilitzant una llista d'usuaris:

    ======================= ========= =========================================
    Atribut                  Tipus                       Significat
    ======================= ========= =========================================
    +name                    string    Nom del banc
    -usuaris                 dict      Diccionari de :class:`Usuari.UsuariBank`
    ======================= ========= =========================================

Funcionament
------------

"""
import random
from iticBankAdvanced import *
from Usuari import *

def askNumberOption(question, numbers):
    """
    Fa que l'usuari trii una opcio de les proposades en un menu printejat previament a la crida de la funció

    :param question: La pregunta que es vol fer a l'usuari
    :param numbers: Quantes opcions hi ha
    :return: La opcio vàlida triada per l'usuari
    """
    while(True):
        answerUser = raw_input(question)
        while(not checkIfFloat(answerUser)):
            answerUser = raw_input("Escriu una opcio vàlida: ")
        answerUser = int(answerUser)
        if(answerUser > 0 and answerUser <= numbers):
            return answerUser

def askYorNQuestion(question):
    """
    Pregunta una pregunta de sí o no.

    :param question: La pregunta que es vol fer a l'usuari
    :return: True o False depenent del que ha triat l'usuari
    """
    while (True):
        answerUser = raw_input(question + "(Y/N) ")
        if (answerUser == "N" or answerUser == "n"):
            return False
        if (answerUser == "Y" or answerUser == "y"):
            return True

class Bank(object):

    """

    Aquesta és la classe que se'n encarrega de gestionar els usuaris d'un banc. Té funcions
    per afergir, treure, accedir, printejar el bank, etc.

    Per accedir a un usuari primer se't demana el nom. Si aquest és vàlid, et mostra una llista d'opcions que es poden fer.
    En el cas de voler eliminar la compta no se't demana la contrassenya de l'usuari (per si és el bank que la vol borrar).
    Però per ingressar o treure diners si que se't demana el password per poder fer les accions.

    Per mostrar la string es fara lo següent::

        Nom: Ferran BankAccount: Data: 23-02-2018 17:27 CompteBancari: Codi IBAN: ES23 Entitat: 6442 Oficina: 5258 Num Compte: 107580686908: 0.0   INACTIVE

    """
    def __init__(self, name):
        self.name = name
        self.__usuaris = {}

    def __str__(self):
        txtFinal=""
        for usuari in self.__usuaris.values():
            txtFinal+= str(usuari) +"\n"
        return txtFinal

    def afegirUsuari(self):
        """
        S'encarrega d'afegir un usuari al bank. Crea un id aleatori i un interestRate i monthlyServiceCharge també aleatoris.
        El que fa és crear un :class:`BankAccount.BankAccount` amb un nom i contrassenya assignats pel usuari amb un balance inicial de 0€.
        Aquest usuari és afegit a la llista d'usuaris del banc.
        """
        while True:
            nom = raw_input("Escriu el teu nom: ")
            if(nom in self.__usuaris):
                print "Aquest nom ja existeix."
            else:
                break
        passw = raw_input("Escriu el teu password: ")
        monthlyServiceCharge = round(random.uniform(2.0, 5.0), 2)
        interestRate = round(random.uniform(0.1, 0.4), 2)
        i=0
        id="ES"
        while i < 22:
            id+=str(random.randint(0,9))
            i+=1
        bankAccount = BankAccountAmpliada(id, 0.0,interestRate,monthlyServiceCharge)
        usuari = UsuariBank(bankAccount,nom, passw)
        self.__usuaris[usuari.name] = usuari

    def __menuUsuari(self, usuari):
        """
        S'encarrega de mostrar una llista d'opcions per l'usuari:

        1. Ingressar diners - Per poder ingressar diners al seu compte
        2. Treure diners - Per poder retirar diners del seu compte (si la compta està inactiva ja no et deixarà entrar-hi)
        #. Mostra info bancaria - Mostra la informacio bancaria de l'usuari
        #. Borrar compta - Mostrarà un missatge de confirmació i si es confirma la compta serà eliminada del banc.
        #. Exit - Per sortir del menú d'usuari i tornar al menú del banc.


        :param usuari: El usuari al qual s'haurà de referenciar a l'hora d'ingressar, treure diners, borrar, etc.
        """
        while True:
            print "MENU USUARI", usuari.name
            print "[1] Ingressar diners"
            print "[2] Treure diners"
            print "[3] Mostra info bancaria"
            print "[4] Borrar compta"
            print "[5] Exit"
            op = askNumberOption("Seleccioni una opció: ", 5)
            if(op == 1):
                usuari.deposit()
            elif(op == 2):
                usuari.withdraw()
            elif(op == 3):
                usuari.comptaBancaria()
            elif(op == 4):
                if(askYorNQuestion("Està segur que vol borrar la seva compta?")):
                    del self.__usuaris[usuari.name]
                    return
            else:
                break

    def entraUsuari(self):
        """
        Per accedir al menú d'usuari d'un usuari dels usuaris existents.

        """
        if(len(self.__usuaris) <= 0):
            print "No hi ha cap usuari registrat"
            return
        for usu in self.__usuaris.values():
            print usu.name + ", ",
        print
        while True:
            nom = raw_input("Escriu el nom de l'usuari: ")
            if(nom in self.__usuaris):
                break
            print "Aquest usuari no existeix"
        self.__menuUsuari(self.__usuaris[nom])

    def monthlyProces(self):
        for usuari in self.__usuaris.values():
            usuari.monthlyProcess()


if(__name__ =="__main__"):
    bank = Bank("TICBANK")
    while True:
        print "MENU BANK", bank.name
        print "[1] Afegir usuari"
        print "[2] Accedir usuari"
        print "[3] Cobrar interessos mensuals"
        print "[4] Printeja bank"
        print "[5] Exit"

        op = askNumberOption("Seleccioni una opció: ", 5)
        if (op == 1):
            bank.afegirUsuari()
        elif (op == 2):
            bank.entraUsuari()
        elif (op == 3):
            bank.monthlyProces()
        elif (op == 4):
            print bank
        else:
            exit()