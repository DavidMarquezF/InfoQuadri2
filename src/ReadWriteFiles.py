#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
==============
ReadWriteFiles
==============

Aquest mòdul conté totes les funcions necessaries per guardar i recuperar strings de fitxers, crear directoris si és necessari
amb els fitxers requerits a dins, comprobar que els fitxers requerits existeixen en un directori, etc.

Per gestionar tot lo relacionat amb guardar i recuperar, hem decidit que les dades es guardin en tres fitxers:

1. Usuaris.txt
2. Posts.txt
3. Hashtags.txt

Tots aquests aniran dins d'un directori que l'usuari especificarà.

Per assegurar-nos que els fitxers tenen sempre el mateix nom, hem creat variables globals en aquest mòdul amb els noms
que es posaran a cada fitxer:

.. code-block:: python

    NomFitUsuaris ="Usuaris.txt"
    NomFitPosts ="Posts.txt"
    NomFitHashtags ="Hashtags.txt"

"""

import os, MainLib

NomFitUsuaris ="Usuaris.txt"
NomFitPosts ="Posts.txt"
NomFitHashtags ="Hashtags.txt"

def checkFilesExist(fol):
    """
    Chequeja si el directori fol conté els fitxers necessaris

    :param fol: El directori que s'ha de comprobar si té els fitxers o no
    :return: True si conté els fitxers necessàris i False si no
    """
    return (os.path.isfile(fol + "/" +NomFitUsuaris) and os.path.isfile(fol + "/" + NomFitPosts) and os.path.isfile(fol + "/" + NomFitHashtags))
def askFolder():
    """
    Demana un directori on hi ha els fitxers necessaris (chequeja si existeix, conté els fitxers necessàris, etc.)

    :return: El nom del directori
    """
    while True:
        fol = raw_input("Esculli el directori on hi ha les dades de la iTICApp: ")
        if(not os.path.exists(fol)):
            print "Aquest directori no existeix"
        else:
            if(not checkFilesExist(fol)):
                print "Aquest directori no és el correcte, ja que no conte els fitxers", NomFitUsuaris, NomFitPosts, NomFitHashtags
            else:
                break
    return fol

def prepareFiles(folderName, createDir =True):
    """
    Crea els fitxers necessàris en un directori, que, si no existeix, també es crea

    :param folderName: El nom del directori
    :param createDir: Si s'ha de crear o no un directori
    :return:
    """
    if(createDir):
        os.makedirs(folderName)
    open(folderName+"/"+NomFitUsuaris, "w").close()
    open(folderName + "/" + NomFitPosts, "w").close()
    open(folderName + "/" + NomFitHashtags, "w").close()

def createUseFolder():
    """
    S'utilitza per guardar dades (crear el directori i fitxers, utilitzar-ne de ja existents, etc.)

    :return: El nom del directori on s'han guardat
    """
    while True:
        fol = raw_input("Esculli un directori on hi vol guardar la informació: ")
        if(not os.path.exists(fol)):
            prepareFiles(fol)
            return fol
        else:
            if(MainLib.askYorNQuestion("Aquest directori ja existeix. Vol sobreescriure els seus continguts? ")):
                if(not checkFilesExist(fol)):
                    print "Aquest directori no conte els fitxers necessaris. Creant els fitxers..."
                    prepareFiles(fol, False)
                    print "Done"
                return fol

def checkIfTypeExists(type):
    """
    Chequeja si el nom del fitxer és un dels existents en el mòdul

    :param type: El nom del fitxer
    :return: True si existeix i False si no
    """
    return type == NomFitUsuaris or type == NomFitPosts or type == NomFitHashtags

def writeToFile(folderName, type, lines):
    """
    Escriu al fitxer type dins de folderName el text (lines)

    :param folderName: El nom del directori que conté els fitxers adeqüats
    :param type: El nom del fitxer que es vol accedir
    :param lines: El text que se li vol  posar
    :return: False si no s'ha pogut realitzar correctament i True si s'ha pogut fer tot correctament
    """
    if not checkIfTypeExists(type):
        print "El tipus no existeix", type
        return False

    try:
        f = open(folderName+"/"+type,"w")
    except IOError as e:
        print "Error al obrir el fitxer",type,":",e.message
        return False
    except Exception as e:
        print "Error al obrir fitxer",":",e.message
        return False

    f.write("\n".join(lines))
    f.close()
    return True

def readlines(folderName, type):
    """
    Llegeix el fitxer type dins de folderName

    :param folderName: El nom del directori que conté els fitxers adeqüats
    :param type: El nom del fitxer que es vol accedir
    :return:
    """
    if not checkIfTypeExists(type):
        print "El tipus no existeix", type
        return False
    try:
        f = open(folderName + "/" + type)
    except IOError as e:
        print "Error al obrir el fitxer",type,":",e.message
        return
    except Exception as e:
        print "Error al obrir fitxer",":",e.message
        return

    l = f.readlines()
    for line in range(len(l)):
        l[line] = l[line].rstrip("\n")
    f.close()
    return l
