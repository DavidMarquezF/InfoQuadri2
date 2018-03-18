#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
=================
Classe User
=================

"""
from MainLib import encode
import Exceptions

class User(object):
    """
    Aquesta classe és la que defineix l'usuari i com funcionarà.

    Un usuari té una llista de posts associat amb ell.

    ======================= ========= =========================================================================
    Atribut                  Tipus                       Significat
    ======================= ========= =========================================================================
    +nick                    string    És el nick de l'usuari
    -email                   string    És l'email de l'usuari
    -password                string    És el password de l'usuari. Quan es mostri per pantalla serà encriptat.
    +posts                   list      Llista de posts de l'usuari (:class:`Post.Post`)
    +followers               list       Llista de usuaris que segueixen a aquest usuari
    +following               list       Llista de usuaris que segueix aquest usuari.
    ======================= ========= =========================================================================

    La string de l'usuari serà::

        Usuari: Ferran Email: ferran@exemple.com Encripted password: xN_F1sc=

    """
    def __init__(self, nick ="", email="", password=""):
        self.nick=nick
        self.__email=email
        self.__password=password
        self.posts = []
        self.followers = []
        self.following = []

    def __eq__(self, other):
        return self.nick == other.nick

    def __str__(self):
        txt = "Usuari: "+self.nick + " Email: " + self.getEmail() + " Encripted password: " + encode("clau", self.__password) + "\n\n" + "Published posts: "
        if(len(self.posts) <= 0):
            txt+="No posts available"
        txt+="\n"
        for post in self.posts:
            txt+=str(post) + "\n\n"
        return txt

    def getEmail(self):
        return self.__email

    def registra_post(self, post):
        """
        Afegeig un post a la llista de posts associats a aquest usuari

        :param post: El post a afegir (del tipus :class:`Posts.Post`)
        """
        self.posts.append(post)

    def addFollower(self, follower):
        """
        Afegeix un usuari a la llista de followers d'aquest usuari

        :param follower: Usuari a afegir a la llista dels seguidors (:class:User.User`).
        """
        self.followers.append(follower)

    def addFollowing(self, following):
        """
        Afegeix un usuari a la llista de following d'aquest usuari

        :param following: Usuari a seguir (:class:User.User`).
        """
        self.following.append(following)
    def desa(self):
        separador="\t"
        txt = self.nick+separador+self.__password+separador+self.__email+separador
        txt += ":::".join([str(post.id) for post in self.posts]) + separador
        txt += ":::".join([follower.nick for follower in self.followers]) + separador
        txt += ":::".join([following.nick for following in self.following]) + separador
        return txt

    def recupera(self,s, posts):
        try:
            s = s.split("\t")
            nick = s[0]
            password = s[1]
            email = s[2]
            postsS = s[3].split(":::")
            followers = s[4].split(":::")
            following = s[5].split(":::")
        except Exception as e:
            print "Error al recuperar l'usuari: ", e.message
            return False


        self.nick = nick
        self.__email = email
        self.__password = password
        if(followers != [""]):
            self.followers = followers
        if(following != [""]):
            self.following = following
        try:

            for post in postsS:
                post = int(post)
                if(post in posts):
                    self.registra_post(posts[post])
                else:
                    raise Exceptions.NoPostException(post)
        except Exceptions.NoHashtagException as er:
            print "Error. El post",er.message, "no existeix en la xarxa social"
            return False
        except AttributeError as at:
            print "La conversió de post no s'ha fet correctament: ",at.message
            return False
        except Exception as e:
            print "No s'ha pogut convertir el post:", e.message
            return False

        return True

if(__name__ == "__main__"):
    p1 = User("john24", "john24@gmail.com", "abracadabra")
    p2 = User("johh24", "john244@gmail.com", "patadecabra")
    print p1
    print p2
    p3 = User("john24", "john2444@gmail.com", "supercalifra")
    print p3.nick
    print p1 == p3