#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
=================
Classe iTICApp
=================

"""
from User import *
from posts import *
class iTICApp(object):
    """
    La classe iTICApp serà la que se n'ocuparà de gestionar tots els usuaris, posts i tags de la xarxa social.

    ======================= ========= =========================================================================
    Atribut                  Tipus                       Significat
    ======================= ========= =========================================================================
    -usuaris                 dict     Diccionari de :class:`User.User` dins de la xarxa social (key = nick)
    -posts                   dict     Diccionari de :class:`Post.Post` penjats en la xarxa (key = info)
    -hashtags                dict     Diccionari de :class:`hastag` penjats en la xarxa (key = id)
    ======================= ========= =========================================================================

    """
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
        if(nick in self.getUsuaris()): #TODO: Cal mirar si aixo s'hauria de fer aixi
            print "El usuari",nick, "ja existeix"
            return

        self.getUsuaris()[nick] = User(nick, email, password)

    def afegeixHashtag(self, id):
        """
        Afegeix un hashtag de id *id* a la xarxaSocial. Si existia hashtag amb el mateix id es queixa.
        :param id: El id del hashtag
        """
        if (id in self.getHashtags()):
            print "El hashtag", id, "ja existeix"
            return

        self.getHashtags()[id] = Hashtag(id)

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
        if(idHashtag not in self.getHashtags()): #TODO: és aixo el que s'ha de fer?
            self.afegeixHashtag(idHashtag)

        post = Post(contingutPost)
        post.registra_usuari(nick)
        post.afegeix_hashtag(self.getHashtags()[idHashtag])
        self.getPosts()[contingutPost] = post
        self.getUsuaris()[nick].registra_post(post)


    def users(self):
        """
        Llista per pantalla la informació completa dels usuaris de l’aplicatiu, incloent la informació
        dels seus posts.
        """
        lst=[]
        for u in self.getUsuaris().values():
            lst.append(str(u))

        print "\n".join(lst)


    def posts(self):
        """
        Llista per pantalla la informació completa de tots els posts en ordre invers a com s’han
        realitzat.
        """
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
        for post in self.getUsuaris()[nick].posts:
            print post