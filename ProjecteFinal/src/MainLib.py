#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
==============
Mòdul MainLib
==============

Aquest mòdul s'encarrega de fer funcions generals que s'utilitzaran dins de tota l'aplicació

"""


from avrException import *
import sys
def exception(message, LineProgram=None, place=None, exitProgram = True):
    """
    Mostrarà una excepció i farà exit si no s'especifica el contrari

    :param message: Missatge a mostrar
    :param LineProgram: Línia a on ha petat
    :param place: Lloc
    :param exitProgram: Si sortirà o no del programa
    """
    print "\033[01;31mError\033[00m{0}{1} - {2}".format((" a " + place) if place != None else "",
                                                          (" a la línia " + str(LineProgram)) if LineProgram != None else"", message)
    if exitProgram:
        sys.exit()

def logInfo(TAG, message):
    """
    Mostra informació per la pantalla

    :param TAG: Tag relacionada amb el missatge
    :param message: Missatge a mostrar
    """
    print "AVR Log: {0} - {1}".format(TAG, message)


def signed_to_int(binari,llargada=8):
    """
    Passa de signed a int

    >>> signed_to_int("1010")
    -6
    >>> signed_to_int("011")
    3
    """
    if binari[0]=='0':
        return int(binari, 2)
    else:
        length = "{0:" + str(llargada).zfill(3) + "b}"
        complement = ""
        for i in range(len(binari)):
            if binari[i] == "0":
                complement += '1'
            else:
                complement += '0'
        unsigned = length.format(int(complement, 2) + 1)
        return -int(unsigned,2)


def to_signed(numero,llargada=8):
    """
    Passa de int a signed

    >>> print to_signed(-2)
    11111110
    >>> print to_signed(5)
    00000101
    >>> print to_signed(-166)
    11011010
    >>> print to_signed(-1)
    11111111
    >>> print to_signed(10)
    00001010
    >>> print to_signed(403)
    10010011
    """
    length = "{0:" + str(llargada).zfill(3) + "b}"
    unsigned=str(length.format(abs(numero)))
    if len(unsigned)>llargada:
        unsigned=unsigned[len(unsigned)-llargada :]
    complement=""
    if numero<0:
        for i in range(len(unsigned)):
            if unsigned[i]=="0":
                complement+='1'
            else:
                complement+='0'
        signed = '{0:b}'.format(int(complement, 2) + 1)
        if len(signed)!=8:
            signed='1'*(llargada-len(signed))+signed
    if numero>0:
        signed=unsigned
    if numero==0:
        signed='0'*llargada
    return signed

def __check_int(num):
    """
    Comproba si és un int o no

    :param num: Nombre
    :return: Boleà
    """
    return int==type(num)