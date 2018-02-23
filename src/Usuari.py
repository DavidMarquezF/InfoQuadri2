from iticBankAdvanced import *
from getpass import getpass


def checkIfInt(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


class UsuariBank(object):
    def __init__(self, bankAdvanced, name, passw):
        self.__bankAccount = bankAdvanced
        self.name = name
        self.__passw = passw

    def authentificate(self):
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
        print self.__bankAccount

    def deposit(self):
        print "\nINGRESSAR DINERS A:",self.name,"\n"
        if(self.authentificate()):
            while True:
                x = raw_input("Quants diners vols ingressar? ")
                if(not checkIfInt(x)):
                    print "Introdueixi un valor valid"
                else:
                    break
            self.__bankAccount.deposit(float(x))
            print "Diners:", self.__bankAccount.balance
        else:
            print "No t'has pogut autentificar correctament."

    def withdraw(self):
        if(self.__bankAccount.status == False):
            print "La teva compta esta inactiva, no pots retirar diners."
            return
        print "\nRETIRAR DINERS DE:",self.name,"\n"
        if(self.authentificate()):
            while True:
                x = raw_input("Quants diners vols retirar? ")
                if(not checkIfInt(x)):
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
        self.__bankAccount.monthlyProcess()



if(__name__ == "__main__"):
    d ={}
    c1 = BankAccountAmpliada("ES6621000418401234567891", 100.0, 0.03, 2.5)
    u = UsuariBank(c1, "Ferran", "123")
    d[u.name] = u
    u.withdraw()
    u.comptaBancaria()
