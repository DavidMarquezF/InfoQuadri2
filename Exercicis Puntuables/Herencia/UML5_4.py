import math

class Plotter(object):
    maxY = 1000
    maxX = 1000
    origenX = 0
    origenY = 0
    def __init__(self, nom):
        self.__nom = nom
        self.x = Plotter.origenX
        self.y = Plotter.origenY
        self.tocaPapaer = False
        self.__punt=False

    def getNom(self):
        return self.__nom

    def puja(self):
        if(not self.tocaPapaer):
            return
        self.tocaPapaer = False
        if(self.__punt):
            print self.__nom+": punt a ({0}, {1})".format(self.x, self.y)

    def baixa(self):
        if (self.tocaPapaer):
            return
        self.tocaPapaer = True
        self.__punt = True

    def origen(self):
        self.x = Plotter.origenX
        self.y = Plotter.origenY

    def __printLinia(self, startX, startY):
        print self.__nom+": linia de ({0}, {1}) a ({2}, {3})".format(startX, startY, self.x, self.y)



    def moua(self, x, y):
        startX = self.x
        startY = self.y
        self.x = x
        self.y  = y
        if(self.tocaPapaer):
            self.__printLinia(startX, startY)
            self.__punt = False

    def mour(self, despX, despY):
        startX = self.x
        startY = self.y
        self.x += despX
        self.y += despY
        if (self.tocaPapaer):
            self.__printLinia(startX, startY)
            self.__punt = False



class Poligonal(object):
    def __init__(self):
        self.__punts = []

    def afegeix(self, punt):
        self.__punts.append(punt)

    def __len__(self):
        return len(self.__punts)

    def __getitem__(self, item):
        return self.__punts[item]

    def __iter__(self):
        return iter(self.__punts)

    def getPunts(self):
        return self.__punts
    def distanceTwoPoints(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def longitud(self):
        dist=0.0
        for i in range(len(self)):
            p1 = self[i]
            if(i >= len(self)-1):
                p2 = self[0]
            else:
                p2 = self[i+1]

            dist+=self.distanceTwoPoints(p1,p2)

        return dist

    def dibuixa(self, plotter):
        plotter.puja()
        plotter.moua(self[0][0], self[0][1])
        plotter.baixa()
        exclude = True
        for point in self:
            if(not exclude):
                plotter.moua(point[0], point[1])

            exclude = False
        plotter.moua(self[0][0], self[0][1])
        plotter.puja()


class PolReg(Poligonal):
    def __init__(self, centre, vertex, costats):
        super(PolReg,self).__init__()
        self.__costats = costats
        self.__centre = centre
        r = self.distanceTwoPoints(centre, vertex)
        vectorDir = (vertex[0] - centre[0], vertex[1] - centre[1])
        angleInicial = math.atan2(vectorDir[1], vectorDir[0])
        x = [r * math.cos(2*math.pi * n / costats + angleInicial) + centre[0] for n in range(costats)]
        y = [r * math.sin(2*math.pi * n / costats + angleInicial) + centre[1] for n in range(costats)]
        for punt in range(costats):
            self.afegeix((round(x[punt],2), round(y[punt],2)))



if(__name__ == "__main__"):
    p = Plotter("P1")
    p.moua(10,10)
    p.baixa()
    p.mour(5,0)
    p.moua(15,5)
    p.puja()
    p.origen()
    p.baixa()
    p.puja()

    pol = Poligonal()
    pol.afegeix((0,0))
    pol.afegeix((1, 0))
    print len(pol)
    pol.afegeix((1, 1))
    print pol.longitud()
    pol.dibuixa(p)

    print "-----PoliReg"
    p = PolReg((0, 0), (2, 0), 4)
    print len(p)
    plot = Plotter("P2")
    p.dibuixa(plot)