#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
======================
Classe Post
======================

"""
import datetime
from Hashtags import Hashtag

class Post(object):
    """
    Aquesta classe s'encarrega de crear un post i emmagatzemar-lo.

   ======================= ========= =========================================================================
   Atribut                  Tipus                       Significat
   ======================= ========= =========================================================================
   +id                      int       És l'identificador del post. S'incrementa en 1 per cada post.
   +contingut               string    És el contingut del post.
   -date                    Date      És la data en el moment de publicar un post
   +contenidor              list      Llista de posts
   +registra_usuari         string    És el nick de l'usuari
   ======================= ========= =========================================================================

   """
    idd=1
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
        """
        Afegeix un usuari
        :param nick: usuari a afegir
        """
        self.nick=nick

    def afegeix_hashtag(self,Hashtag):
        """
        Mètode que permet afegir un objecte Hashtag(id)
        :param Hashtag: hashtag a afegir
        """
        self.contenidor.append(Hashtag)


    def __str__(self):
        txt="Post id:" + " " + str(self.id) + " " + "info:" + " " + self.contingut + " " + "Date" + " " + self.getDate() + " " + "\n" + "Nick user:" + " " + self.nick + " " + "Hashtags available:" + " "
        for e in self.contenidor:
            txt+=str(e) + " "
        return txt





if __name__=='__main__':
    h1=Hashtag("adventure")
    h2=Hashtag("winter")
    print h1
    print h1==h2
    post1=Post("Cal realitzar el possible per assolir l'impossible.")
    post2=Post("Tota accio provoca reaccions.")
    print post1
    print post2
    post3=Post("Cal realitzar el possible per assolir l'impossible.")
    print post3.contingut
    print post1==post3