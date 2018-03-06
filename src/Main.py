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
if(__name__ == "__main__"):
    interpret = Interpret()
    interpret.afegeixOrdre("usuari", usuari)
    interpret.afegeixOrdre("hashtag", hashtag)
    interpret.afegeixOrdre("publicar",publicar)
    interpret.afegeixOrdre("print", printT)
    interpret.setPrompt("- ")
    interpret.run()
