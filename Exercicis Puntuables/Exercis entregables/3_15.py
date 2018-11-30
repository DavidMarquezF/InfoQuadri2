class Contacte(object):
    def __init__(self, nick ="", email="", telefons = []):
        self.nick = nick
        self.email = email
        self.__telefons = telefons

    def __eq__(self, other):
        return self.nick == other.nick

    def __str__(self):
        if(len(self.__telefons) <= 0):
            tel = "No phones yet"
        else:
            tel = " ".join(self.__telefons)
        return "Nick: " + self.nick + " Email: " + self.email + " Telefons: " + tel

    def addTelefon(self, telefon):
        if(telefon in self.__telefons):
            print "Phone already added"
            return
        self.__telefons.append(telefon)

class Agenda(object):
    def __init__(self):
        self.contactes = []

    def __iter__(self):
        return self.contactes

    def __len__(self):
        return  len(self.contactes)

    def add(self,c):
        self.contactes.append(c)

    def __getitem__(self, item):
        return self.contactes[item]

    def __setitem__(self, key, value):
        self.contactes[key] = value

    def __delitem__(self, key):
        del self.contactes[key]

    def __str__(self):
        txt="Contacts list\n"
        for contacte in self.contactes:
            txt+=str(contacte)+"\n"
        return txt.rstrip()

    def ordena(self):
        print "Ordered contactsList"
        for contacte in sorted(self.contactes, key=lambda x: x.nick.lower()):
            print contacte


if(__name__ == "__main__"):
    p = Contacte("juliaR", "juliaRoberts@gmail.com")
    p.addTelefon("938888888")
    p.addTelefon("937777777")
    r = Contacte("bradP", "bradPitt@gmail.com")
    r.addTelefon("666666666")
    r.addTelefon("666666666")
    s = Contacte("bonJ", "bonJovi@gmail.com")
    print p == r
    print p
    print s

    a = Agenda()
    for i in range(3):
        a.add(Contacte(nick=raw_input("Entri nick: "), email = raw_input("Entri email: ")))
    print a
    print a.ordena()
    print len(a)
    a[0].addTelefon("666666666")
    a[0].addTelefon("666666667")
    print a[0]
    a[1] = Contacte(nick="Perfecto")
    del a[0]
    print a