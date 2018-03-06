#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Interpret import  *
from iTICApp import *
from getpass import getpass

i = iTICApp()

def usuari(nick):
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
    if (len(id) > 1):
        print "El hashtag no pot tenir espais"
        return
    id = id[0]
    i.afegeixHashtag(id)

def publicar (info):
    if(len(info) < 3):
        print "Has d'incloure com a mínim tres paràmetres: nick, id i post"

    nick = info[0]

    id = info[1]

    post=" ".join(info[2:])

    i.publicarPost(nick, id, post)

def printT(info):
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
    else:
        print "El primer paràmetre ha de ser users, posts o posts-user"

def afegirHashtags(info):
    if (len(info) < 2):
        print "Es necessiten dos paràmetres: postId i hasthatgs"
    postId = info[0]
    hashtags = info[1:]
    for hashtagId in hashtags:
        i.afegirHastagAlPost(postId, hashtagId)

def help(i):
    print "Ajuda per a fer instruccions:"
    print "- usuari <nick> -> Crea un usuari"
    print "- hashtag <id> -> Afegeix un hashtag a la xarxa Social"
    print "- publicar <nick> <hastag (únic)> <contingut post> -> Afegeix un post a l'usuari <nick>"
    print "- afHashtag <postId> [<hashtags>] -> Afegeix hashtags al post <id>"
    print "- print <ent> [<nick>] -> Per printejar infotmació. Ent pot ser:"
    print "0. users -> no és  necessari posar més paràmetres. Mostrarà una llista completa d'usuaris"
    print "1. posts -> tampoc és necessari posr més paràmetres. Mostrarà una llista de tots els posts"
    print "2. posts-user -> requereix un altre paràmetre: el nick de l'usuari del qual volem saber els posts. Si ho vols saber de més d'un introdueixne els que necessitis"

if(__name__ == "__main__"):
    usuari(["Ferran"])
    publicar(["Ferran", "vida", "ashdoahd", "akjshdkjah"])
    print "Per ajuda escriu - help me"
    interpret = Interpret()
    interpret.afegeixOrdre("usuari", usuari)
    interpret.afegeixOrdre("hashtag", hashtag)
    interpret.afegeixOrdre("publicar",publicar)
    interpret.afegeixOrdre("print", printT)
    interpret.afegeixOrdre("afHashtag", afegirHashtags)
    interpret.afegeixOrdre("help", help)
    interpret.setPrompt("- ")
    interpret.run()
