class Referendum(object):
    def __init__ (self):
        self.regions=["r1","r2","r3"]
        self.candidats=["A","B","C"]
        self.votsRegions={}

    def __str__(self):
        txt=""
        for regio in self.votsRegions:
            txt += regio + " " + str(self.votsRegions[regio]) +"\n"
        return txt

    def afegirVots(self,c,v,r):
        if not r in self.votsRegions:
            self.votsRegions[r]={c:v}
        else:
            if not c in self.votsRegions[r]:
                self.votsRegions[r][c]=v
            else:
                self.votsRegions[r][c]+=v
    def votsCandidatRegions(self,c):
        """
        retorna el nombre total de vots pel candidat c, en totes les regions
        """
        totalVots=0
        for regio, candidatR in self.votsRegions.items():
            for candidatVot, vots in candidatR.items():
                if(candidatVot == c):
                    totalVots +=vots
        return totalVots


    def mesVotatRegio(self,r):
        """
        retorna el candidat mes votat d'una regio
        """
        dictR = self.votsRegions[r]
        mesVotat="-1"
        maxVots=0
        for candidat, vots in dictR.items():
            if(vots > maxVots):
                maxVots = vots
                mesVotat = candidat
        return mesVotat

    def llistaRegions(self,c):
        """
        retorna un llistat amb les regions on ha guanyat el candidat
        """
        llistaRegions=[]
        for regio in self.votsRegions:
            if(self.mesVotatRegio(regio) == c):
                llistaRegions.append(regio)
        return llistaRegions

if(__name__ == "__main__"):
    v = Referendum()
    v.afegirVots("A", 100,"r1")
    v.afegirVots("A", 55,"r2")
    v.afegirVots("A", 150,"r3")
    v.afegirVots("C", 200,"r1")
    v.afegirVots("B", 50,"r2")
    v.afegirVots("C", 120,"r3")
    print v
    print v.votsCandidatRegions("A")
    print v.mesVotatRegio("r3")
    print v.llistaRegions("A")