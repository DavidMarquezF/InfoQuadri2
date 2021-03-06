#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
SimAVR
=======

Aquest modul se n'encarrega de gestionar l'input de l'usuari. Es crida com un executable i se l'hi ha de passar com a mínim
la direcció del fitxer .hex que conté el programa en el format intelhex.

Només es pot cridar una de les següents comandes:

1. -p : Volcarà Program memory
#. -pt: Volcarà Program memory i farà trace
#. -r : Volcarà els registres
#. -rt : Volcarà els registres i farà trace
#. -d : Volcarà DataMemory
#. -dt : Volcarà Data memory i farà trace
#. -t : Únicament habilitarà el trace

"""

import sys, MainLib, AVRMCU
from intelhex import IntelHex16bit

Program=False
Register=False
Trace=False
Dades = False

def argsAct():
    """
    A partir dels arguments sys.argv fa trace o no i farà el volcament demanat
    """
    args = sys.argv[1:]
    if(len(args) > 2):
        MainLib.exception("Es necessita un màxim de 2 paràmetres", place="SimAVR")

    commandSel=""
    file=""
    for command in args:
        if(command in Commands):
            commandSel = command
        elif(command.endswith(".hex")):
            file=command

    if(file == ""):
        MainLib.exception("Es necessita un fitxer .hex", place="SimAVR")
    if(commandSel != ""):
        Commands[commandSel]()
    ih = intelhex(file)
    setUpMiniAvr(ih)

def setUpMiniAvr(ih):
    """
    Prepara el miniAVR a partir del intelhex bit array

    :param ih: intelhex bit array
    """
    avr = AVRMCU.Avrmcu()
    avr.set_prog(ih)
    avr.set_trace(Trace)
    avr.run()
    if(Program):
        print avr.dump_prog()
    elif(Register):
        print avr.dump_reg()
    elif(Dades):
        print avr.dump_dat()




def intelhex(file):
    """
    A partir del fitxer hex extreu l'array d'enters

    :param file: el nom del fitxer .hex
    :return: L'array de dades
    """
    ih = IntelHex16bit()
    ih.fromfile(file, format='hex')
    return ih.tobinarray()


def memory():
    """
    Activa volcatge de programa
    """
    global Program
    Memory = True

def register():
    """
    Activa volcatge de registre
    """
    global Register
    Register = True

def dades():
    """
    Activa volcatge de dades
    """
    global Dades
    Dades = True

def memoryTrace():

    """
    Activa volcatge de programa amb trace
    """
    trace()
    memory()

def registerTrace():

    """
    Activa volcatge de registre amb trace
    """
    trace()
    register()


def dadesTrace():
    """
    Activa volcatge de dades amb trace
    """
    trace()
    dades()

def trace():
    """
    Activa trace
    """
    global Trace
    Trace = True

Commands={
    "-p":memory,
    "-pt":memoryTrace,
    "-r":register,
    "-rt":registerTrace,
    "-d":dades,
    "-dt":dadesTrace,
    "-t":trace
}






if (__name__ == "__main__"):
    argsAct()