import random
from iticBankAdvanced import *
from Usuari import *

def askNumberOption(question, numbers):
    while(True):
        answerUser = raw_input(question)
        while(not checkIfInt(answerUser)):
            answerUser = raw_input("Escriu una opcio valida: ")
        answerUser = int(answerUser)
        if(answerUser > 0 and answerUser <= numbers):
            return answerUser

def askYorNQuestion(question):
    while (True):
        answerUser = raw_input(question + "(Y/N) ")
        if (answerUser == "N" or answerUser == "n"):
            return False
        if (answerUser == "Y" or answerUser == "y"):
            return True


class Bank(object):

    def __init__(self, name):
        self.name = name
        self.__usuaris = {}

    def afegirUsuari(self):
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
        while True:
            print "MENU USUARI", usuari.name
            print "[1] Ingressar diners"
            print "[2] Treure diners"
            print "[3] Mostra info bancaria"
            print "[4] Borrar compta"
            print "[5] Exit"
            op = askNumberOption("Seleccioni una opcio: ", 5)
            if(op == 1):
                usuari.deposit()
            elif(op == 2):
                usuari.withdraw()
            elif(op == 3):
                usuari.comptaBancaria()
            elif(op == 4):
                if(askYorNQuestion("Esta segur que vol borrar la seva compta?")):
                    del self.__usuaris[usuari.name]
                    return
            else:
                break

    def entraUsuari(self):
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
        print "[4] Exit"

        op = askNumberOption("Seleccioni una opcio: ", 4)
        if (op == 1):
            bank.afegirUsuari()
        elif (op == 2):
            bank.entraUsuari()
        elif (op == 3):
            bank.monthlyProces()
        else:
            exit()