class User(object):
    def __init__(self, nom):
        self.name = nom
        self.friends = []
        self.photos=[]

    def ShowPhotos(self):
        print "Photos user", self.name
        for p in self.photos:
            print "Name of image",p.image,"list of tags"
            for t in p.tags:
                print t

    def addPhoto(self, p):
        if(p not  in self.photos):
            self.photos.append(p)

    def addFriend(self,f):
        self.friends.append(f)

    def myTags(self, nom = None):
        if(nom == None):
            nom = self.name
        s = []
        for photo in self.photos:
            for tag in photo.tags:
                if(nom in tag):
                    s.append(tag)
        return s
    def tagsAmics(self, nom = None):
        if(nom == None):
            nom = self.name
        s = []
        s.append(self.myTags(nom))
        for amic in self.friends:
            s.append(amic.myTags(nom))
        return s

    def totSobreMi(self, nom = None, s=[]):
        if(nom == None):
            nom = self.name
        tags = self.myTags(nom)
        for tag in tags:
            if(tag not in s):
                s.append(tag)
            else:
                return

        for amic in self.friends:
            amic.totSobreMi(nom,s)

        return s

class Photo(object):
    def __init__(self, imatge):
        self.imatge = imatge
        self.tags = []
    def addTag(self, t):
        self.tags.append(t)

    def __eq__(self, other):
        return self.imatge == other.imatge

if(__name__ == "__main__"):
    g= User("pere")
    i = User("irene")
    p = Photo("a.jpg")
    p.addTag("pere que guai")
    p1 = Photo("b.jpg")
    p.addTag("super interessant pere")
    g.addPhoto(p)
    g.addPhoto(p1)

    p2 = Photo("c.jpg")
    p2.addTag("irene mola")
    p3 = Photo("d.jas")
    p3.addTag("pere mola")
    i.addPhoto(p2)
    i.addPhoto(p3)
    d = User("david")
    p4 = Photo("asdasd")
    p4.addTag("irene guai")
    p4.addTag("pere guapo")
    d.addPhoto(p4)
    d.addFriend(g)
    e = User("enric")
    p5 = Photo("ada")
    p5.addTag("que divertit pere ")
    e.addPhoto(p5)

    g.addFriend(d)
    g.addFriend(i)
    i.addFriend(d)
    i.addFriend(e)

    print g.totSobreMi()



