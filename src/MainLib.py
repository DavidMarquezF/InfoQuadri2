#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
===========
Main Lib
===========
"""

import base64
def encode(key, string):
    """
    Encripta una string a partir d'una clau
    :param key: La clau amb la qual s'encriptarà
    :param string: La string a encriptar
    :return: La string encriptada

    >>> encode("clau", "Hola")
    'q9vN1g=='
    """
    encoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)

def checkIfInt(number):
    """
    Mira si un numero és int o no
    :param number: número donat
    :return: retorna true si és int i false si no
    """
    try:
        int(number)
        return True
    except ValueError:
        return False


def askNumberOption(question, numbers):
    """
    Fa que l'usuari trii una opcio de les proposades en un menu printejat previament a la crida de la funció

    :param question: La pregunta que es vol fer a l'usuari
    :param numbers: Quantes opcions hi ha
    :return: La opcio vàlida triada per l'usuari
    """
    while(True):
        answerUser = raw_input(question)
        while(not checkIfInt(answerUser)):
            answerUser = raw_input("Escriu una opcio vàlida: ")
        answerUser = int(answerUser)
        if(answerUser > 0 and answerUser <= numbers):
            return answerUser

def askYorNQuestion(question):
    """
    Pregunta una pregunta de sí o no.

    :param question: La pregunta que es vol fer a l'usuari
    :return: True o False depenent del que ha triat l'usuari
    """
    while (True):
        answerUser = raw_input(question + "(Y/N) ")
        if (answerUser == "N" or answerUser == "n"):
            return False
        if (answerUser == "Y" or answerUser == "y"):
            return True