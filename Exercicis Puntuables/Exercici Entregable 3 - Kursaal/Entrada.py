class EntradaGeneral(object):
    def __init__(self, nom, preu = 10):
        self.galliner=True
        self.nom = nom
        self.__preu = preu

    def  __eq__(self, other):
        return False

    def __str__(self):
        print "Entrada KURSAAL"
        if(self.galliner):
            return "Galliner. " + str(self.getPreu()) + " EUR"
        else:
            return "Platea. "

    def getPreu(self):
        return self.__preu

class EntradaPlatea(EntradaGeneral):
    def __init__(self, nom, preu = 50, fila = 0, seient = 0):
        super(EntradaPlatea, self).__init__(nom,preu)
        self.galliner = False
        self.fila = fila
        self.seient = seient

    def __str__(self):
        return super(EntradaPlatea, self).__str__() + " Fila: "+ str(self.fila) + " Seient: " + str(self.seient) +" "+ str(self.getPreu()) +" EUR"

    def __eq__(self, other):
        if(isinstance(other, EntradaGeneral)):
            return False
        return  self.seient == other.seient and self.fila == other.fila and self.nom == other.nom

if(__name__ == "__main__"):
    e1 = EntradaGeneral("Trio Guarnieri", preu=23)
    print e1
    e2 = EntradaPlatea("The Dubliners", preu=40, fila=3, seient=24)
    print e2
    print e1.getPreu()
    print e2.getPreu()
    print EntradaPlatea("The Dubliners", fila=3, seient=24) == e2
    print e1 == e2
    print e1 == EntradaGeneral("dasda")