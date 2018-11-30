#!/usr/bin/env python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseEvent
import matplotlib.dates as mdates
from dataset import Dataset
import datetime
class DataSetPlot(object):
    """

    Un objecte d’aquesta classe representa un gràfic de un o més objectes DataSet.

    ======================= =============================== ===========================================================================================
    Atribut                 Tipus                           Significat
    ======================= =============================== ===========================================================================================
    +datasets               list                            Són els datasets a representar
    ======================= =============================== ===========================================================================================
    """

    def __init__(self):
        plt.ylabel("Temperatura(C)")
        plt.xlabel("Time")
        plt.title("Grafica Temperatura/Temps")
        self.datasets=[]
        fig = plt.figure(1)
        fig.autofmt_xdate()  # Rota les dates perquè capiguen bé en la gràfica

        ax = plt.axes()
        ax.fmt_xdata = mdates.DateFormatter(
            "%d-%m %H:%M:%S")  # Quan passes el ratoli per sobre la gràfica t'ho posara en aquest format
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m %H:%M"))  # Formateja l'eix de les x per tenir el format especificat

        fig.canvas.mpl_connect('button_press_event', self.onclick)

        plt.grid() #Posar quadricules

    def plot(self,d):
        """
        Afegeix a la gràfica un conjunt de dades determinat per DataSet d. Si s’afegeix més d’un
        DataSet es representa cadascun d’un color diferent. L’etiqueta de la llegenda corresponent
        a aquest DataSet és el nom del mateix.
        :param d: És un objecte Dataset
        """
        self.datasets.append(d)
        plt.plot(d.timeVector(),d.valueVector(), label=d.getName())

    def onclick(self, event):
        """
        Gestiona el click de l'usuari a la gràfica. Si fa doble click, es printeja per pantalla els datasets relacionats amb el gràfic

        :param event: :class:`matplotlib.backend_bases.MouseEvent` event del click
        """
        if(isinstance(event,  MouseEvent)):
            if(event.dblclick):
                print
                print "-----------------------------------------------------"
                print "-----Datasets in graph Grafica Temperatura/Temps-----"
                print "-----------------------------------------------------"
                print
                print "There are {0} datasets".format(len(self.datasets))
                t="\n"
                for d in self.datasets:
                    t+=str(d) +"\n\n"
                print t
                raw_input("\nPress enter to close the graph...")
                plt.close()



    def show(self):
        """
        Mostra la gràfica per la pantalla.
        :return:
        """
        print "Done. To see the datasets used in the graph double click on the graph"
        plt.legend()    #Fa que es mostri la llegenda
        plt.show()
        plt.close()
        return


if(__name__=="__main__"):
    d = DataSetPlot()
    data = Dataset("test")
    data.add(datetime.datetime(2018, 1, 1, 0,0,0), 100)
    data.add(datetime.datetime(2018, 1, 1,1,0,0), 200)
    d2 = Dataset("test2")
    d2.add(datetime.datetime(2018, 1, 1,0,0), 148)
    d2.add(datetime.datetime(2018, 1, 1,1,0,0), 010)
    d.plot(data)
    d.plot(d2)
    print d.show()

