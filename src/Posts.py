#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
======================
Classe Post
======================

"""
import datetime
from Hashtags import Hashtag
import Exceptions
class Post(object):
    """
    Aquesta classe s'encarrega de crear un post i emmagatzemar-lo.

    Els id dels posts es gestionen amb una variable estàtica que es va incrementat cada vegada que es crea un post

    ======================= ========= =========================================================================
    Atribut                  Tipus                       Significat
    ======================= ========= =========================================================================
    +id                      int       És l'identificador del post. S'incrementa en 1 per cada post.
    +contingut               string    És el contingut del post.
    -date                    Date      És la data en el moment de publicar un post
    +contenidorHashtags      list      Llista de posts
    +nick                    string    És el nick de l'usuari
    ======================= ========= =========================================================================

   """
    idd=1
    def __init__(self,contingut =""):
        now = datetime.datetime.now()
        self.id=Post.idd
        self.contingut=contingut
        self.__date= now.strftime("%d-%m-%Y %H:%M")
        self.contenidorHashtags=[]
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


    def desa(self):
        separador="\t"
        txt=str(self.id)+separador+self.contingut+separador+self.nick+separador
        for hashtag in self.contenidorHashtags:
            txt+=hashtag.id + ":::"
        txt = txt.rstrip(":::")
        txt+=separador+repr(self.__date)
        return txt


    def recupera(self, s, hashtags):
        """
        Recupera el post a partir de la string amb la que s'ha guardat

        :param s: la string on hi ha tota la informació
        :param hashtags: llista de hashtags de la xarxa social
        :return: Retorna True si la recuperació s'ha fet amb èxit. Si no, retorna False
        """
        try:
            s = s.split("\t")
            id = int(s[0])
            contingut = s[1]
            nick = s[2]
            hashs = s[3].split(":::")
            date = s[4]
        except Exception as e:
            print "Error al recuperar el post:", e.message
            return False

        try:
            date = eval(date)
        except Exception as e:
            print "La data no s'ha pogut convertir correctament: " +e.message
            return False

        self.id = id
        self.contingut= contingut
        self.registra_usuari(nick)
        self.__date = date

        try:

            for hashtag in hashs:
                if(hashtag in hashtags):
                    self.afegeix_hashtag(hashtags[hashtag])
                else:
                    raise Exceptions.NoHashtagException(hashtag)
        except Exceptions.NoHashtagException as er:
            print "El hashtag associat a aquest post no existeix en la llista de Hashtags de la web. Hashtag:",er.message
            return False
        except AttributeError as at:
            print "La conversió de hashtags no s'ha fet correctament: ",at.message
            return False
        except Exception as e:
            print "No s'ha pogut convertir el hashtag:", e.message
            return False

        return True


    def registra_usuari(self,nick):
        """
        Afegeix un usuari

        :param nick: usuari a afegir
        """
        self.nick=nick

    def afegeix_hashtag(self,Hashtag):
        """
        Mètode que permet afegir un objecte :class:`Hashtags.Hashtag`

        :param Hashtag: hashtag a afegir
        """
        self.contenidorHashtags.append(Hashtag)


    def __str__(self):
        txt="Post id:" + " " + str(self.id) + " " + "info:" + " " + self.contingut + " " + "Date" + " " + self.getDate() + " " + "\n" + "Nick user:" + " " + self.nick + " " + "Hashtags available:" + " "
        for e in self.contenidorHashtags:
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