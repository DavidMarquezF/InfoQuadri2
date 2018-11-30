class Missatge(object):
    def __init__(self, emailOrigen, textMessage, viewed = False):
        self.setEmailOrigen(emailOrigen)
        self.setTextMessage(textMessage)
        self.setViewed(viewed)

    def __str__(self):
        return "Message information " + self.getEmailOrigen() + " " + self.getTextMessage()

    def __eq__(self, other):
        return self.getTextMessage() == other.getTextMessage() and self.getEmailOrigen() == other.getEmailOrigen()

    def getEmailOrigen(self):
        return self.__emailOrigen

    def getTextMessage(self):
        return self.__textMessage

    def getViewed(self):
        return self.__viewed

    def setEmailOrigen(self, value):
        self.__emailOrigen = value

    def setTextMessage(self, value):
        self.__textMessage = value

    def setViewed(self, value):
        self.__viewed = value


class Mailbox(object):
    def __init__(self, missatges = []):
        self.missatges = missatges

    def addNewArrival(self, emailOrigen, textMessage):
        self.missatges.append(Missatge(emailOrigen, textMessage))

    def getMessage(self, pos):
        if(pos >= len(self.missatges)):
            print "Missatge no existent, posicio no correcta"
        missat = self.missatges[pos]
        print missat
        missat.setViewed(True)

    def sortByMail(self):
        for miss in sorted(self.missatges, key=lambda x: x.getEmailOrigen().split("@")[0]):
            miss.setViewed(True)
            print miss

if(__name__ == "__main__"):
    m1 = Missatge("joan@gmail.cat", "avui arribo tard")
    m2 = Missatge("anna@gmail.com", "hem aconseguit la beca!!")
    m3 = Missatge("joan@gmail.cat", "avui arribo tard")
    print m1
    print "m1 == m2 ??", m1 == m2
    print "m1 == m3 ??", m1 == m3
    bustia = Mailbox()
    bustia.addNewArrival("joan@gmail.cat", "avui arribo tard")
    bustia.addNewArrival("anna@gmail.com", "hem aconseguit la beca!!")
    bustia.addNewArrival("jordi@ucp.edu","quin es l'horari de consultes rebut?")
    bustia.getMessage(2)
    print "Sort by email"
    bustia.sortByMail()