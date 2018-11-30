#!/usr/bin/env python
#-*- coding: utf-8 -*-
from dataset import Dataset
import datetime

class Sensor(object):
    """
    **Classe Sensor**: S'utilitza per contenir les constants de cada sensor

    ======================= =============================== ========================================================================
    Atribut                  Tipus                              Significat
    ======================= =============================== ========================================================================
    +dci                     float                              És una constant del sensor
    +ki                      float                              És una constant del sensor
    +dTi                     float                              És una constant del sensor
    ======================= =============================== ========================================================================

    """

    number = 0
    def __init__(self, dci, ki,dTi):
        self.dci = dci
        self.ki = ki
        self.dTi = dTi
        self.sensor = Sensor.number
        Sensor.number+=1

Sensors = None

def createDict():
    """
    Simplement assigna a la variable global una llista amb els sensors amb les seves constants.

    """
    global Sensors
    if(Sensors == None):
        d = dict()
        d[0] = Sensor(3.1418, 5.65, 0.24)
        d[1] = Sensor(0.0, 1.0, 1.37)
        d[2] = Sensor(2.185, 5.3972, 0.95)
        d[3] = Sensor(2.1313, 5.2959,0.42)
        d[4] = Sensor(10.5953, 16.8243, 0.29)
        d[5] = Sensor(10.5842, 16.5574, 0.79)
        Sensors = d

def calculateAB(sensor):
    """
    Calcula la A i B utilitzant les seguents formules:

    A = 330.4 / (1024.0 * sensor.ki)
    B = (100 * dci) / ki - 50 + dTi

    :param sensor: Objecte de la classe sensor que conte les constants relacionades amb el calcul de A i B
    :return: una llista amb A i B

    >>> s = Sensor(3.1418, 5.65, 0.24)
    >>> calculateAB(s)
    [0.05710730088495575, 5.847079646017695]
    """
    A = 330.4 / (1024.0 * sensor.ki)
    B = (100 * sensor.dci) / sensor.ki - 50 + sensor.dTi
    return [A,B]


def normalize(d,s=0):
    """
    Modifica el dataset que se l'hi passa per convertir tots els seus valors a graus celcius depenent del sensor que hi estigui assignat.

    :param d: El dataset
    :param s: El nombre del sensor

    >>> d = Dataset("test")
    >>> d.add(datetime.datetime(1,1,1), 100)
    >>> d.add(datetime.datetime(2,1,1), 200)
    >>> normalize(d, 0)
    >>> print d
    Dataset:
    Temps: 0001-01-01 00:00:00  Valor: 11.5578097345
    Temps: 0002-01-01 00:00:00  Valor: 17.268539823
    """
    createDict()
    try:
        ab = calculateAB(Sensors[s])
    except KeyError:
        print "\033[01;31mError\033[00m - Sensor",s, "doesn't exist"
        exit()
    d.transform(ab[0], ab[1])