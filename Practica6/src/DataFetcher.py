#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Modul DataFetcher
==================

"""
from dataset import *
import datetime
import urllib2
import csv
import copy
class UnknownDatasetException(Exception):
    pass
class InvalidDateRange(Exception):
    pass

class DataFetcher(object):
    """

    **Classe DataFetcher**

    Els objectes de la classe DataSetFetcher són utilitats que saben importar dades d’un sensor cor-
    responents a un dia o un rang de dies des d’un servidor de dades.
    Els objectes d’aquesta classe tenen un únic atribut que és l’URL del servidor d’on s’han
    d’obtenir les dades.

    ======================= =============================== =======================================================================
    Atribut                  Tipus                            Significat
    ======================= =============================== =======================================================================
    +url                     string                           És l'url de on treiem totes les dades
    ======================= =============================== =======================================================================

    """
    def __init__(self,url="https://ocwitic.epsem.upc.edu/assignatures/tecpro/laboratori-material/dadespractica6/"):
        self.url=url            #Data esta organitzada: hora, sensor, valor

    def fetch(self,dia,sensor=0, logErrors=True):
        """
        El mètode retorna un DataSet de nom 'Sensor X', essent X el número de sensor, que conté
        les observacions del sensor sensor corresponents al dia dia. Dia és un objecte de classe date.
        Si no es poden obtenir les dades aixeca l'excepció UnknownDataSetException.

        :param dia: Es un objecte de classe date.
        :param sensor: L'identificador del sensor
        :param logErrors: Si ha de mostrar els errors  per  pantalla
        :return: El :class:`dataset.Dataset` extret del link

        """
        url = self.url + "dades_{0}_{1}_{2}/at_download/file".format(dia.strftime("%y"), dia.strftime("%m"),dia.strftime("%d"))
        try:
            try:
                d = urllib2.urlopen(url)
                dades = csv.reader(d)
            except urllib2.HTTPError:
                raise UnknownDatasetException()
            except urllib2.URLError:
                raise UnknownDatasetException()
        except UnknownDatasetException as e:
            if(logErrors):
                print "\033[01;31mError\033[00m - Unknown dataset exception:",url,"doesn't exist"
                exit()
            e.message = "\033[01;31mError\033[00m - Unknown dataset exception: "+url+" doesn't exist"
            return e

        dataset = Dataset("Sensor " + str(sensor))

        for line in dades:
            if(line[1] == str(sensor)):
                time=datetime.datetime.strptime(line[0], "%H:%M:%S")
                dataset.add(copy.deepcopy(dia).replace(hour=time.hour, minute=time.minute, second=time.second, microsecond=time.microsecond), float(line[2]))
        return dataset


    def fetch_interval(self,from_day,to_day,sensor=0):
        """
        El mètode retorna un DataSet de nom ’Sensor X’, essent X el número de sensor, que
        conté les observacions del sensor sensor corresponents als dies que van de from day a to day
        incloent el primer i excloent el darrer. from day i to day són objectes de la classe date. Si
        no es poden obtenir les dades aixeca l’excepció UnknownDataSetException.

        :param from_day:  objecte de tipus date. És la data on començarà a recopilar dades
        :param to_day: també de tipus date és la data on acabarà de recopilar dades.
        :param sensor: número del sensor
        :return: Dataset del conjunt de dies del sensor

        """

        try:
            if from_day>to_day:
                raise InvalidDateRange()
            if from_day==to_day:
                d=self.fetch(to_day,sensor)
                if d==False:
                    raise UnknownDatasetException()
                return d
            s=self.fetch(from_day,sensor, logErrors=False)
            if isinstance(s, Exception):
                raise s
            return s.concat(self.fetch_interval(from_day+datetime.timedelta(days=1),to_day,sensor))
        except UnknownDatasetException as e:
            print e.message, ": The day",from_day,"doesn't exist in the database"
            exit()
        except InvalidDateRange:
            print "\033[01;31mError\033[00m - From_day es mes gran que to_day"
            exit()

if(__name__ == "__main__"):
    d = DataFetcher()
    #print d.fetch(datetime.datetime(2016,3,1))

    #d.fetch(datetime.datetime.today())
    print d.fetch_interval(datetime.datetime(2016,2,27),datetime.datetime(2016,3,1))
