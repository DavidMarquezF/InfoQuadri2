#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
=================
Classe iTICApp
=================

"""
from User import *
from Posts import *
from Hashtags import *
from MainLib import *
class iTICApp(object):
    """
    La classe iTICApp serà la que se n'ocuparà de gestionar tots els usuaris, posts i tags de la xarxa social.

    ======================= ========= =========================================================================
    Atribut                  Tipus                       Significat
    ======================= ========= =========================================================================
    -usuaris                 dict     Diccionari de :class:`User.User` dins de la xarxa social (key = nick)
    -posts                   dict     Diccionari de :class:`Posts.Post` penjats en la xarxa (key = info)
    -hashtags                dict     Diccionari de :class:`Hashtags.Hashtag` penjats en la xarxa (key = id)
    ======================= ========= =========================================================================

    """
    def __init__(self, usuaris = dict(), posts = dict(), hashtags = dict()):
        self.__usuaris=usuaris
        self.__posts=posts
        self.__hastags=hashtags


    def getUsuaris(self):
        return self.__usuaris

    def getPosts(self):
        return self.__posts

    def getHashtags(self):
        return self.__hastags

    def afegirUsuari(self, nick, email, password):
        """
        Afegeix un nou usuari a la xarxa social. Si el nick ja existeix, s'evita la creació d'aquest usuari

        :param nick: És el nick de l'usuari
        :param email: És el email de l'usuari
        :param password: És el password de l'usuari

        >>> i = iTICApp()
        >>> i.afegirUsuari("pere","pere@gmail.com","gilisticoexpia")
        >>> i.afegirUsuari("pere","pere@gmail.com","gilisticoexpia")
        El usuari pere ja existeix
        """
        if(nick in self.getUsuaris()):
            print "El usuari",nick, "ja existeix"
            return

        self.getUsuaris()[nick] = User(nick, email, password)

    def afegeixHashtag(self, id):
        """
        Afegeix un hashtag de id *id* a la xarxaSocial. Si no existia un hashtag amb el mateix avisa que s'ha creat.

        :param id: El id del hashtag
        """
        if (id in self.getHashtags()):
            return
        print "S'ha creat el hashtag", id
        h = Hashtag(id)
        self.getHashtags()[id] = h
        return h

    def publicarPost(self, nick, idHashtag, contingutPost):
        """
        Comprova si el nick d’usuari existeix a l’aplicació. Si és el cas, crea el Post, guarda el
        nick d’usuari al Post, afegeix l’objecte Hashtag al Post, afegeix l’objecte Post a l’usuari
        corresponent i afegeix el Post al contenidor de posts.

        :param nick: El nick de l'usuari al qual s'associa el post.
        :param idHashtag: El id del hashtag
        :param contingutPost: El contingut del post
        """

        if(nick not in self.getUsuaris()):
            print "El usuari",nick,"no existeix"
            return

        self.afegeixHashtag(idHashtag)

        post = Post(contingutPost)
        post.registra_usuari(nick)
        post.afegeix_hashtag(self.getHashtags()[idHashtag])
        self.afegeixHashtag(idHashtag)
        self.getPosts()[post.id] = post
        self.getUsuaris()[nick].registra_post(post)
        print "El post s'ha penjat correctament"

    def afegirHastagAlPost(self, idPost, hashthagId):
        """
        Afegeix un hashtag al post de id idPost

        :param idPost: El id del post al qual es vol afegir el hashtag
        :param hashthagId: El id del hashtag a afegir al post
        """
        if(not checkIfInt(idPost)):
            print "El id del post és un nombre"
            return
        if(int(idPost) not in self.getPosts()):
            print "Aquest id de post no existeix"
            return
        h = self.afegeixHashtag(hashthagId)
        if(h is None):
            print "El post ja té aquest hashtag associat"
            return
        self.getPosts()[int(idPost)].afegeix_hashtag(h)

    def users(self):
        """
        Llista per pantalla la informació completa dels usuaris de l’aplicatiu, incloent la informació
        dels seus posts.
        """
        if(len(self.getUsuaris()) <= 0):
            print "No hi ha cap usuari"
            return
        lst=[]
        for u in self.getUsuaris().values():
            lst.append(str(u))

        print "\n".join(lst)


    def posts(self):
        """
        Llista per pantalla la informació completa de tots els posts en ordre invers a com s’han
        realitzat.
        """
        if(len(self.getPosts()) <= 0):
            print "No hi ha cap post"
            return

        for post in self.getPosts().values():
            print post
            print

    def postsUser(self, nick):
        """
        Obté el llistat d’informació dels posts (contingut) d’un Usuari amb el nick proporcionat
        A continuació segueix uns exemples de funcionament.

        :param nick: Nom de l'usuari del qual volem mostrar els posts
        """
        if(nick not in self.getUsuaris()):
            print "El usuari",nick,"no exiteix"
            return
        if(len(self.getUsuaris()[nick].posts) <= 0):
            print "El usuari no té cap post penjat"
            return
        for post in self.getUsuaris()[nick].posts:
            print post

    def follow(self, followerNick, followingNick):
        """
        Fa que un usuari en segueixi a un altre

        :param followerNick: El nick del usuari que seguirà.
        :param followingNick: El nick de l'usuari que serà seguit
        """
        if(followerNick not in self.getUsuaris() or followingNick not in self.getUsuaris()):
            print "Algun usuari no existeix"
            return

        follower = self.getUsuaris()[followerNick]
        following = self.getUsuaris()[followingNick]
        if (follower in self.getUsuaris()[followingNick].followers):
            print followerNick, "ja segueix a", followingNick
            return

        following.addFollower(follower)
        follower.addFollowing(following)
        print followerNick, "ha començat a seguir a", followingNick, "!"

    def userFollow(self, nick):
        """
        Printeja el nombre de seguidors i el nombre de persones que segueix un usuari

        :param nick: El nick del qual volem saber el nombre de followers i following
        """
        if (nick not in self.getUsuaris()):
            print "El nick no existeix"
            return
        print nick+":"
        print "\tFollowers:", len(self.getUsuaris()[nick].followers)
        print "\tFollowing:", len(self.getUsuaris()[nick].following)

    def printFollowers(self, nick):
        """
        Printeja els nicks dels followers d'un usuari

        :param nick: Nick de l'usuari del qual vols saber l'informació
        """
        if (nick not in self.getUsuaris()):
            print "El nick no existeix"
            return
        if (len(self.getUsuaris()[nick].followers) <= 0):
            print nick, "no és seguit per a ningú"
        for follower in self.getUsuaris()[nick].followers:
            print follower.nick+",",
        print

    def printFollowing(self, nick):
        """
        Printeja els nicks dels seguits d'un usuari

        :param nick: Nick de l'usuari del qual vols saber l'informació
        """
        if (nick not in self.getUsuaris()):
            print "El nick no existeix"
            return
        if(len(self.getUsuaris()[nick].following) <= 0):
            print nick, "no segueix a ningú"
        for following in self.getUsuaris()[nick].following:
            print following.nick+",",
        print

    def printFollowingPosts(self, nick):
        """
        Printeja els posts penjats per els usuaris que el usuari de nick *nick* segueix cronològicament

        :param nick: El nick de l'usuari
        """
        if (nick not in self.getUsuaris()):
            print "El nick no existeix"
            return
        if (len(self.getUsuaris()[nick].following) <= 0):
            print nick, "no segueix a ningú"

        following = self.getUsuaris()[nick].following
        postsCount=0
        for post in self.getPosts().values().__reversed__():
            try:
                post.nick
            except AttributeError:
                continue

            for followingNick in following:
                if(post.nick == followingNick.nick):
                    print post
                    postsCount+=1
        if(postsCount <= 0):
            print "No hi ha cap post penjat"
