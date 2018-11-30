# -*- encoding: utf-8 -*-

"""
Modul bduTest
=============

Gestiona una base de dades d'usuaris. Cada usuari té els següents
atributs:

    ========== =========== ================================
    Atribut    Tipus       Significat
    ========== =========== ================================
    idusuari   string      Identifica l'usuari
    nom        string      Nom real de l'usuari
    email      string      Correu electrònic
    adreca     string      Adreça postal de l'usuari
    tel        int         Telèfon de l'usuari
    passwd     string      Password de l'usuari
    ========== =========== ================================

Les operaions modifiquen el paràmetre directament ja que els diccionaris
són mutables.

Per tant aquest programa ens proporcionarà les següents funcions:

1. Afegir usuari
2. Eliminar usuari
3. Crear una base d'usuaris buida
#. Canvi de nom d'usuari
#. Canvi d'email
#. Fer "login" (comprovació de password)
#. Mostrar la *base de dades*

Representació
-------------

La base de dades es representa com un diccionari.

La clau és `idusuari` i el valor es una tupla de la forma::

   (nom, email, adreca, tel, passwd)


Funcions
--------

"""



def buida():
    """
    Retorna una base de dades d'usuaris buida.

    :return: Una bdu buida
    """
    return {}

def afegir (bd, idusuari, nom, email, adreca, tel, passwd):
    """
    Modifica la base de dades d'usuari `bd` una vegada s'ha donat
    d'alta l'usuari `idusuari` amb les dades corresponents.  En cas
    que l'usuari `idusuari` ja existis prèviament, la funció no
    modifica `bd`.

    :param bd: La bdu (diccionari) a modificar
    :param string idusuari: L'identificador d'usuari a afegir
    :param string nom: El nom de l'usuari que s'afegeix
    :param string email: L'email de l'usuari que s'afegeix
    :param string adreca: L'adreça de l'usuari que s'afegeix
    :param int tel: El telefon de l'usuari que s'afegeix
    :param string passwd: El password de l'usuariq ue s'afegeix

    >>> bd = buida()
    >>> afegir(bd, 'id1', 'Pep', 'pep@infern', 'carrer', 980, 'secret')
    >>> bd
    {'id1': ('Pep', 'pep@infern', 'carrer', 980, 'secret')}
    """
    if idusuari not in bd:
        bd[idusuari] = (nom, email, adreca, tel, passwd)


def esborrar(bd, idusuari):
    """
    Modifica la base de dades d'usuaris `bd` una vegada s'ha donat de
    baixa l'usuari amb clau `idusuari`. En cas que `bd` no contingui
    `idusuari` la funcio no modifica `bd`.

    :param bd: La bdu (diccionari) a modificar
    :param string idusuari: L'identificador d'usuari a afegir

    >>> bd = buida()
    >>> afegir(bd, 'u1','Pere','pere@infern','a',5656,'s1')
    >>> esborrar(bd, 'u1')
    >>> bd == buida()
    True
    """
    if idusuari in bd:
        del bd[idusuari]


def mod_nom(bd, idusuari, nom):
    """
    Modifica la bd d'usuaris una vegada s'ha modificat
    el 'nom' corresponent a 'idusuari'.

    Si 'idusuari' no existeix, no es modifica la bd.

    :param bd: La bdu (diccionari) a modificar
    :param string idusuari: L'identificador d'usuari a afegir
    :param string nom: El nom de l'usuari que s'afegeix

    >>> bd = buida()
    >>> afegir(bd, 'id1', 'Pep', 'pep@infern', 'carrer', 980, 'secret')
    >>> mod_nom(bd, 'id1', 'Josep')
    >>> bd
    {'id1': ('Josep', 'pep@infern', 'carrer', 980, 'secret')}
    """
    if idusuari in bd:
        dummy,email,adreca,tel,passwd = bd[idusuari]
        bd[idusuari] = (nom,email,adreca,tel,passwd)


def mod_email(bd, idusuari, email):
    """
    Modifica la bd d'usuaris una vegada s'ha modificat
    el 'email' corresponent a 'idusuari'.

    Si 'idusuari' no existeix, no es modifica la bd.

    :param bd: La bdu (diccionari) a modificar
    :param string idusuari: L'identificador d'usuari a afegir
    :param string email: L'email de l'usuari que s'afegeix

    >>> bd = buida()
    >>> afegir(bd, 'id1', 'Pep', 'pep@infern', 'carrer', 980, 'secret')
    >>> mod_email(bd, 'id1', 'pep@cel')
    >>> bd
    {'id1': ('Pep', 'pep@cel', 'carrer', 980, 'secret')}
    """
    if idusuari in bd:
        nom,dummy,adreca,tel,passwd = bd[idusuari]
        bd[idusuari] = (nom,email,adreca,tel,passwd)


def check_passwd(bd, idusuari, passwd):
    """
    Retorna True si en la bd s'acaren el nom_usuai i el passwd.

    :param bd: La bdu (diccionari) a modificar
    :param string idusuari: L'identificador d'usuari a afegir
    :param string passwd: El password de l'usuariq ue s'afegeix

    :return: Retorna True si el password és correcte i Fals si no ho és

    >>> bd = buida()
    >>> afegir(bd, 'id1', 'Pep', 'pep@infern', 'carrer', 980, 'secret')
    >>> check_passwd(bd, 'id1', 'secret')
    True
    >>> check_passwd(bd, 'id1', 'secret3')
    False
    """
    return (idusuari in bd) and (bd[idusuari][4] == passwd)


def escriure(bd):
    """
    Escriu per pantalla la bd.

    :param bd: La bdu (diccionari) a modificar

    """
    for k in sorted(bd.keys()):
        t = bd[k]
        print "%6s: " % k
        print "%10s %15s %15s %8s %8s\n" % t
