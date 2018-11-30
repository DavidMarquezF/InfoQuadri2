import random
class Cotxe (object):
    def __init__(self, mat, color, model):
        self.setMat(mat)
        self.setColor(color)
        self.setModel(model)
    def __str__(self):
        return self.getMat() + " " + self.getColor() + " " + self.getModel()

    def __eq__(self, other):
        return self.getMat() == other.getMat()

    def getMat(self):
        return  self.__mat

    def getColor(self):
        return self.__color

    def getModel(self):
        return self.__model

    def setMat(self,value):
        self.__mat = value

    def setColor(self, value):
        self.__color = value

    def setModel(self, value):
        self.__model = value

    def toString(self):
        return self.getMat()+"/#"+self.getColor()+"/#"+self.getModel()

    def fromString(self, stri):
        """
        Actualitza els atributs a partir d'una string

        >>> c = Cotxe("2331 DXC", "vermell", "VW Polo")
        >>> cString = c.toString()
        >>> b = Cotxe("", "", "")
        >>> b.fromString(cString)
        >>> c == b
        True
        """
        c = stri.split("/#")
        self.setMat(c[0])
        self.setColor(c[1])
        self.setModel(c[2])

    def desa(self,f):
        """
        >>> c = Cotxe("2331 DXC", "VW Polo", "vermell")
        >>> f = open("cotxe.dat", "w")
        >>> c.desa(f)
        >>> f.close()
        >>> d = Cotxe("", "", "")
        >>> f = open("cotxe.dat", "r")
        >>> d.recupera(f)
        >>> f.close()
        >>> c == d
        True
        """
        f.write(self.toString())
    def recupera(self, f):
        self.fromString(f.read())


class Garatge(object):
    CotxeBuit = Cotxe("lliure", "", "")
    def __init__(self, places, cotxes = []):
        self.__places = places
        self.__garatge = dict((i, Garatge.CotxeBuit) for i in range(self.getPlaces()))
        if(cotxes != []):
            for cotxe in cotxes:
                self.afegirCotxe(cotxe)

    def __str__(self):
        return str([str(cot) for cot in self.getGaratge().values()])

    def __eq__(self, other):
        if(self.getPlaces() != other.getPlaces()):
            return False
        for key, cotxe in self.getGaratge().items():
            if(not cotxe.__eq__(other.getGaratge()[key])):
                return False
        return True

    def getPlaces(self):
        return self.__places

    def getGaratge(self):
        return self.__garatge

    def setPlaces(self,value):
        self.__places = value


    def afegirCotxe(self, cotxe, askWhere = False):
        g = self.getGaratge()
        if(self.placesLliures()<= 0):
            print "Garatge ple"
            return [False, "Garatge ple"]
        if(cotxe in g.values()):
            print "Cotxe ja existeix"
            return [False, "Cotxe ja existeix"]

        if(askWhere):
            placesLliures = [str(key) for key,value in g.items() if(value == Garatge.CotxeBuit)]
            print "\nPlaces lliures:"
            print ", ".join(placesLliures)
            print "\n"
            while True:
                x = raw_input("A quina de les places vol aparcar? ")
                if(x in placesLliures):
                    break
                print "Aquesta placa no es valida, introduexne una que existeixi si us plau."
            g[int(x)] = cotxe
            return [True, x]
        else:
            for key,value in g.items():
                if(value == Garatge.CotxeBuit):
                    g[key] = cotxe
                    return [True, key]

    def treureCotxe(self, cotxe):
        g = self.getGaratge()
        if(cotxe not in g.values()):
            return False

        for key, value in g.items():
            if(value == cotxe):
                g[key] = Garatge.CotxeBuit
                return True

    def placesLliures(self):
        return len([cot for cot in self.getGaratge().values() if (cot == Garatge.CotxeBuit)])

    def treureAleatori(self):
        self.treureCotxe(random.choice([cot for cot in self.getGaratge().values() if (cot != Garatge.CotxeBuit)]))

    def desaGaratge(self, fName):
        g = self.getGaratge()
        open(fName, "w").close() #netejar fitxer
        f = open(fName, "a")
        for value in g.values():
            value.desa(f)
            f.write("\n")

    def recuperaGaratge(self, fName):
        """
        >>> gar =Garatge(3,[Cotxe("123", "Blanc", "G5"), Cotxe("542", "Negre", "G12"), Cotxe("1321", "Negre", "G12")])
        >>> gar.desaGaratge("garatge.dat")
        >>> gar2 = Garatge(0)
        >>> gar2.recuperaGaratge("garatge.dat")
        >>> gar == gar2
        True

        """
        self.__garatge = {}
        f = open(fName)
        l = f.readlines()
        for i, cot in enumerate(l):
            cotxe = Cotxe("","","")
            cot = cot.rstrip()
            cotxe.fromString(cot)
            self.getGaratge()[i] = cotxe
        self.setPlaces(len(l))



if(__name__  == "__main__"):
    c1 = Cotxe("123", "Blanc", "G5")
    gar = Garatge(3,[c1])
    print gar
    c2 = Cotxe("542", "Negre", "G12")
    gar.afegirCotxe(c2)
    print gar
    c3 = Cotxe("1321", "Negre", "G12")
    gar.afegirCotxe(c3)
    print gar
    print gar.afegirCotxe(Cotxe("dsads", "da", "dasda"))
    gar.treureCotxe(c1)
    print gar
    gar.treureCotxe(c2)
    print gar
    gar.afegirCotxe(c1,True)
    print gar

    gar = Garatge(3, [Cotxe("123", "Blanc", "G5"), Cotxe("542", "Negre", "G12"), Cotxe("1321", "Negre", "G12")])
    gar.desaGaratge("garatge.dat")
    gar2 = Garatge(0)
    gar2.recuperaGaratge("garatge.dat")
    print gar
    print gar2
    print gar == gar2






