#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Classe BankAccount
===================

Gesiona una compte bancari d'un usuari. Cada compte té els següents atributs:

    ============== =========== =================================
    Atribut        Tipus       Significat
    ============== =========== =================================
    id             string      Identificador del compte
    balance        float       Saldo del compte
    status         boolean     Estat del compte: actiu o inactiu
    numDeposits    int         Nombre d'ingressos mensuals
    numWithdrawals int         Nombre de reintegraments mensuals
    ============== =========== =================================

Representació
-------------

Quan el *balance* és menor al mínim saldo permès, la compta entrarà en mode
 inactiu, que impedirà que es treguin diners en la funció :func: 'BanckAccount.withdraw'.


Funcionament
------------

"""
import datetime

class BankAccount(object):

    MinBalanceActive = 25

    def __init__(self, id,balance, interestRate, monthlyServiceCharges):
        self.id = id
        self.interestRate = interestRate
        self.balance = balance
        self.monthlyServiceCharges = monthlyServiceCharges
        self.status = balance > BankAccount.MinBalanceActive
        self.numDeposits = 0
        self.numWithdrawals = 0

    def __str__(self):
        iban = self.id[0:5]
        entitat = self.id[5:9]
        oficina = self.id[9:13]
        numCompte = self.id[13:]
        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M")
        if(self.status):
            end = "Deposits # = {0} Withdrawals # = {1}".format(str(self.numDeposits), str(self.numWithdrawals))
        else:
            end = "  INACTIVE"
        text = "Data: {0} CompteBancari: Codi IBAN: {1} Entitat: {2} Oficina: {3} Num Compte: {4}: {5} {6}".format(date, iban, entitat, oficina, numCompte, str(self.balance), end)

    def withdraw(self, amount):
        """
        Realitza un reintegrament d’una quantitat amount d’ euros. Només és factible el reintegra-
        ment si el compte és actiu. En aquest cas el mètode retorna el valor True. Si no és possible
        realitzar el reintegrament perquè el compte és inactiu, el mètode ha de retornar el valor
        False

        :param amount: El nombre de diners que es volen treure
        :return: Retorna False si la compta és inactiva i True si no ho és

        >>> b = BankAccount("ES6621000418401234567891",100.0,0.03,2.5)
        >>> b.withdraw(100)
        True
        >>> print b.balance
        0.0
        >>> b.withdraw(50)
        False
        >>> print b.balance
        0.0
        """
        if(not self.status):
            return False

        self.balance -= amount
        if(self.balance < BankAccount.MinBalanceActive):
            self.status = False
        return True

    def deposit(self, amount):
        """
        Realiza un ingrés d’una quantitat amount d’ euros en el compte. Si el saldo supera els 25
        euros, el compte passa a estat actiu.

        :param amount: El nombre de diners que es volen ingressar.

        >>> b = BankAccount("ES6621000418401234567891",100.0,0.03,2.5)
        >>> b.deposit(50)
        >>> print b.balance
        150.0
        >>> b = BankAccount("ES6621000418401234567891",10.0,0.03,2.5)
        >>> print b.status
        False
        >>> b.deposit(50)
        >>> print b.status
        True
        """
        self.balance += amount
        if(self.balance > BankAccount.MinBalanceActive):
            self.status = True

