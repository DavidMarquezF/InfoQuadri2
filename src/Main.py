#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
=============
Main
=============

Aquest mòdul és el que s'haurà d'inicialitzar per obtenir tota la funcionalitat.
Per començar es crearà una instancia de la :class:`iTICApp.iTICApp` i de :class:`Interpret.Interpret`. Al inicialitzar
l'intèrpret se li passarà unes quantes funcions predefinides. L'usuari podrà saber quines són escribint la commanda
help me, que li explicarà que fa cada funció i quins paràmetres requereix. A partir d'aquí, el que s'encarregarà
d'organitzar-ho tot serà l'intèrpret

Per guardar la xarxa social i que sigui accessible per totes les funcions hem inicialitzat :class:`iTICApp.iTICApp` a fora de
__name__ == "__main__" com a una variable global:

.. code-block:: python

    i = iTICApp()
"""
from Interpret import  *
from iTICApp import *
from getpass import getpass
import Exceptions
import ReadWriteFiles
import MainLib

i = iTICApp()

def usuari(nick):
    """
    Funció per afegir usuari a la xarca social

    :param nick: El nick del usuari que es vol registrar
    """
    if(len(nick) > 1):
        print "El nick no pot tenir espais"
        return
    nick = nick[0]
    if(nick in i.getUsuaris()):
        print "El usuari", nick, "ja existeix"
        return
    email = raw_input("Email: ")
    password = getpass("Password: ")

    i.afegirUsuari(nick,email,password)

def hashtag(id):
    """
    Afegeix un Hashtag a la xarxa social

    :param id: el id del hashtag a afegir
    """
    if (len(id) > 1):
        print "El hashtag no pot tenir espais"
        return

    id = id[0]
    if (id in i.getHashtags()):
        print "Aquest hashtag ja existeix"

    i.afegeixHashtag(id)

def publicar (info):
    """
    Publicarà un post a l'usuari

    :param info: Llista de strings que contindrà en primer lloc el nick de l'usuari, en segon lloc *un* hashtag i
        en tercer lloc el contingut del post. Per afegir més hashtags ja es podrà fer amb :func:`Main.afegirHashtags`

    """
    if(len(info) < 3):
        print "Has d'incloure com a mínim tres paràmetres: nick, id i post"

    nick = info[0]

    id = info[1]

    post=" ".join(info[2:])

    i.publicarPost(nick, id, post)

def printT(info):
    """
    Printeja la info demanada. Hi ha varis modes:
        1. Users: Printeja els usuaris
        2. Posts: Printeja els posts creats en la xarxa
        #. Posts-user: Printeja els posts d'un usuari
        #. Followers-user: Printeja els followers d'un usuari
        #. Following-user: Printeja a qui està seguint l'usuari
        #. Following-posts: Printeja els posts de les persones que segueix un usuari ordenats cronològicament (invers)

    :param info: Llista de strings on el primer serà el mode de printeig descrit anteriorment
    """
    ent = info[0]
    if(ent == "users"):
        i.users()
    elif ent == "posts":
        i.posts()
    elif ent == "posts-user":
        if(len(info) <= 1):
            print "No has introduit el nick de l'usuari"
            return
        for nick in info[1:]:
            i.postsUser(nick)
    elif ent == "followers-user":
        if (len(info) != 2):
            print "No has introduit el nick d'un usuari"
            return
        i.printFollowers(info[1])
    elif ent == "following-user":
        if (len(info) != 2):
            print "No has introduit el nick d'un usuari"
            return
        i.printFollowing(info[1])
    elif(ent == "following-posts"):
        if (len(info) != 2):
            print "No has introduit el nick d'un usuari"
            return
        i.printFollowingPosts(info[1])
    else:
        print "El primer paràmetre ha de ser users, posts, posts-user, followers-user, following-user o following-posts"

def afegirHashtags(info):
    """
    S'utilitza per afegir varis hashtags en un post ja creat

    :param info: Llista de strings on el primer serà el id del post i la resta seran els nous hashtags a afegir
    """
    if (len(info) < 2):
        print "Es necessiten dos paràmetres: postId i hasthatgs"
    postId = info[0]
    hashtags = info[1:]
    for hashtagId in hashtags:
        i.afegirHastagAlPost(postId, hashtagId)

def help():
    """
    Printeja una llista de les funcions existents a l'interpret i com funcionen

    """
    print "Ajuda per a fer instruccions:"
    print "- usuari <nick> -> Crea un usuari"
    print "- hashtag <id> -> Afegeix un hashtag a la xarxa Social"
    print "- publicar <nick> <hastag (únic)> <contingut post> -> Afegeix un post a l'usuari <nick>"
    print "- afHashtag <postId> [<hashtags>] -> Afegeix hashtags al post <id>"
    print "- follow <seguidor> <usuari a seguir> -> Es segueix a un usuari"
    print "- followers <nick> -> Printeja el nombre de followers d'un usuari"
    print "- print <ent> [<nick>] -> Per printejar infotmació. Ent pot ser:"
    print "\t0. users -> no és  necessari posar més paràmetres. Mostrarà una llista completa d'usuaris"
    print "\t1. posts -> tampoc és necessari posr més paràmetres. Mostrarà una llista de tots els posts"
    print "\t2. posts-user -> requereix un altre paràmetre: el nick de l'usuari del qual volem saber els posts. Si ho vols saber de més d'un introdueixne els que necessitis"
    print "\t3. followers-user -> printeja els nicks dels followers d'un usuari"
    print "\t4. following-user -> printeja els nicks usuaris que segueix l'usuari"
    print "\t5. following-posts -> printeja els posts dels usuaris que segueix l'usuari (el paràmetre necessàri és el nick)"

def follow(nicks):
    """
    S'utilitza per fer que un usuari en segueixi un altre

    :param nicks: Llista amb dos nicks dels usuaris: el primer serà el que seguirà i el segon el que serà seguit
    """
    if(len(nicks) != 2):
        print "Has d'introduir dos usuaris (persona que segueix, persona a seguir)"
        return
    i.follow(nicks[0], nicks[1])

def userFollowers(nick):
    """
    Printeja el nombre de followers i de persones que segueix

    :param nick: Nick de l'usuari
    """
    if (len(nick) != 1):
        print "Has d'introduir només un nick"
        return
    i.userFollow(nick[0])


#Desa---------------------------------------------------------------------------
def desa():
    fol = ReadWriteFiles.createUseFolder()
    desaPosts(fol)
    desaHashtags(fol)
    desaUsuaris(fol)

def desaPosts(fol):
    posts = []
    for post in i.getPosts().values():
        posts.append(post.desa())

    ReadWriteFiles.writeToFile(fol, ReadWriteFiles.NomFitPosts, posts)

def desaHashtags(fol):
    hashtags =[]
    for h in i.getHashtags().values():
        hashtags.append(h.id)

    ReadWriteFiles.writeToFile(fol, ReadWriteFiles.NomFitHashtags, hashtags)

def desaUsuaris(fol):
    usuaris = []
    for user in i.getUsuaris().values():
        usuaris.append(user.desa())

    ReadWriteFiles.writeToFile(fol, ReadWriteFiles.NomFitUsuaris, usuaris)


#Recupera------------------------------------------------------------------------
def recupera():
    try:
        fol =ReadWriteFiles.askFolder()
        hashtags = dict((value.id, value) for value in recuperaHashtags(fol))
        posts = dict((value.id, value) for value in recuperaPosts(fol,hashtags))
        usuaris = recuperaUsuaris(fol, posts)

        if(usuaris == False or posts == False or hashtags == False):
            recuperaFallida()
            return
    except:
        recuperaFallida()
        return
    print "Dades importades correctament"
    global i
    i= iTICApp(usuaris = usuaris, posts=posts, hashtags=hashtags)

def recuperaFallida():
    print "No s'ha pogut recuperar la xarxa correctament"
    if(MainLib.askYorNQuestion("Dessitja crear una xarxa social nova? ")):
        global i
        i = iTICApp()
    else:
        print "Inteni de buscar un altre directori"
        recupera()





def recuperaPosts(fol,hashtags):
    posts = []
    try:
        for post in ReadWriteFiles.readlines(fol, ReadWriteFiles.NomFitPosts):
            p = Post()
            if (not p.recupera(post, hashtags)):
                raise Exceptions.PostError()
            else:
                posts.append(p)

    except Exceptions.PostError:
        print "El post no s'ha pogut convertir correctament"
        return False
    except Exception as e:
        print e
        return False

    return posts

def recuperaUsuaris(fol,posts):
    usuaris = {}
    try:
        for user in ReadWriteFiles.readlines(fol, ReadWriteFiles.NomFitUsuaris):
            u = User()
            if (not u.recupera(user, posts)):
                raise Exceptions.UserError()
            else:
                usuaris[u.nick] = u

    except Exceptions.UserError:
        print "L'usuari no s'ha pogut convertir correctament"
        return False
    except Exception as e:
        print e
        return False

    try:
        for usuari in usuaris.values():
            followersInstance=[]
            for follower in usuari.followers:
                if (follower == ""):
                    continue
                if(follower not in usuaris):
                    raise Exceptions.NoUserException(follower)
                else:
                    followersInstance.append(usuaris[follower])
            usuari.followers = followersInstance
    except Exceptions.NoUserException as e:
        print "No hi ha cap usuari anomenat", e.message, "en la xarxa social"
        return False
    except Exception as e:
        print "Excepció al posar followers: ", e.message
        return False

    try:
        for usuari in usuaris.values():
            followingInstance=[]
            for following in usuari.following:
                if(following == ""):
                    continue
                if(following not in usuaris):
                    raise Exceptions.NoUserException(following)
                else:
                    followingInstance.append(usuaris[following])
            usuari.following=followingInstance
    except Exceptions.NoUserException as e:
        print "No hi ha cap usuari anomenat", e.message, "en la xarxa social"
        return False
    except Exception as e:
        print "Excepció al posar following: ", e.message
        return False

    return usuaris


def recuperaHashtags(fol):
    hash =[]
    try:
        for h in ReadWriteFiles.readlines(fol, ReadWriteFiles.NomFitHashtags):
            hash.append(Hashtag(h))
    except Exception as e:
        print "Error, no s'ha pogut recuperar els hashtags correctament: ", e.message
        return False
    return hash



if(__name__ == "__main__"):
    #usuari(["Ferran"])
    #usuari(["David"])
    #usuari(["Eloi"])
    #publicar(["Ferran", "esport", "Holiiii", "akjshdkjah"])
    #publicar(["Ferran", "vida", "ashdoahd", "akjshdkjah"])

    print "Per ajuda escriu - help"
    interpret = Interpret()
    interpret.setEnd(desa)
    interpret.setBegin(recupera)
    interpret.afegeixOrdre("usuari", usuari)
    interpret.afegeixOrdre("hashtag", hashtag)
    interpret.afegeixOrdre("publicar",publicar)
    interpret.afegeixOrdre("print", printT)
    interpret.afegeixOrdre("afHashtag", afegirHashtags)
    interpret.afegeixOrdre("follow", follow)
    interpret.afegeixOrdre("followers", userFollowers)
    interpret.setCustomHelp(help)
    interpret.setPrompt("- ")
    interpret.run()

