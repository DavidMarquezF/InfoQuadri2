class Interpret(object):
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
        if(nomc in self.getDCom()):
            print "Aquesta clau ja existeix"
            return
        self.getDCom()[nomc] = ordre

    def run(self):
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