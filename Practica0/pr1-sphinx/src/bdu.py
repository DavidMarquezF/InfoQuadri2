# -*- encoding: utf-8 -*-

"""
Modul bdu
=========

Gestiona una base de dades d'usuaris. Cada usuari té els següents
atributs:

    ========== =========== ================================
    Atribut    Tipus       Significat
    ========== =========== ================================
    idusuari   string      Identifica l'usuari (és la clau)
    nom        string      Indica en nom real de l'usuari
    email      string      Adreça de correu electrònic
    adreca     string      Adreça postal de l'usuari
    tel        int         Telèfon de l'usuari
    passwd     string      Paraula clau de l'usuari
    ========== =========== ================================

Les diferents operacions actuen modificant directament el paràmetre
corresponent atès que està implementat com un diccionari i els
diccionaris són mutables.

Representació
-------------

La base de dades es representa com un diccionari on la clau es
`idusuari` i el valor es una tupla de la forma::

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

    :param dict bd: La bdu a modificar
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
    Retorna True ssi en la bd s'acaren el nom_usuai i el passwd.

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
    """
    for k in sorted(bd.keys()):
        t = bd[k]
        print "%6s: " % k
        print "%10s %15s %15s %8s %8s\n" % t
