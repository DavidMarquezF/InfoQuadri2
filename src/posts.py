import datetime
class Post(object):
    idd=0
    def __init__(self,contingut):
        now = datetime.datetime.now()
        self.id=Post.idd
        self.contingut=contingut
        self.__date= now.strftime("%d-%m-%Y %H:%M")
        self.contenidor=[]
        self.registra_usuari("ningu")
        Post.idd+=1

    def __eq__(self, other):
        return self.contingut==other.contingut

    def setDate(self,d):
        self.__date=d
    def getDate(self):
        return self.__date

    def __iter__(self):
        return iter(str(self.id))

    def registra_usuari(self,nick):
        self.nick=nick

    def afegeix_hashtag(self,id):
        self.contenidor.append(id)


    def __str__(self):
        txt="Post id:" + " " + str(self.id+1) + " " + "info:" + " " + self.contingut + " " + "Date" + " " + self.getDate() + " " + "\n" + "Nick user:" + " " + self.nick + " " + "Hashtags available:"
        for e in self.contenidor:
            txt+=str(e)
        return txt


class Hashtag(object):
    def __init__(self,id):
        self.id=id

    def __eq__(self, other):
        return self.id==other.id

    def __str__(self):
        return self.id





if __name__=='__main__':
    h1=Hashtag("#adventure")
    h2=Hashtag("#winter")
    print h1
    print h1==h2
    post1=Post("Cal realitzar el possible per assolir l'impossible.")
    post2=Post("Tota accio provoca reaccions.")
    print post1
    print post2
    post3=Post("Cal realitzar el possible per assolir l'impossible.")
    print post3.contingut
    print post1==post3