from User import *
class iTICApp(object):
    def __init__(self):
        self.__usuaris=dict()
        self.__posts=dict()
        self.__hastags=dict()


    def getUsuaris(self):
        return self.__usuaris

    def getPosts(self):
        return self.__posts

    def getHashtags(self):
        return self.__hastags

    def afegirUsuari(self, nick, email, password):
        if(nick in self.getUsuaris()): #TODO: Cal mirar si aixo s'hauria de fer aixi
            print "El usuari",nick, "ja existeix"
            return

        self.getUsuaris()[nick] = User(nick, email, password)

    def afegeixHashtag(self, id):
        if (id in self.getHashtags()):
            print "El hashtag", id, "ja existeix"
            return

        self.getHashtags()[id] = Hashtag()

    def publicarPost(self, nick, idHashtag, contingutPost):
        if(nick not in self.getUsuaris()):
            print "El usuari",nick,"no existeix"


    def users(self):
        txt=""
        lst=[]
        for u in self.getUsuaris().values():
            lst.append(str(u))

        return "\n".join(lst)


