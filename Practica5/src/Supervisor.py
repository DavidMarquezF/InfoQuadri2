#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Supervisor (object):
    """

    Un supervisor és un objecte que està informat de tots els nodes i triports que formen un circuit.
    La seva funció principal és "donar vida" a un circuit.

    ======================= =============================== ===========================================================================================
    Atribut                  Tipus                              Significat
    ======================= =============================== ===========================================================================================
    -nodes                        list                          Llista de nodes que el supervisor supervisarà
    -in2                        list                            Llista de tickables (triport o component) que el supervisor supervisarà
    ======================= =============================== ===========================================================================================


    """
    Changed = False
    def __init__(self):
        self.__nodes = []
        self.__tickables = []

    def addNode(self, n):
        """
        Afegeix el node n a la llista de nodes controlats pel supervisor. Addicionalment, s'informa
        al node a través del seu mètode set_supervisor de qui és el seu supervisor.

        :param n: Node a afegir
        """
        self.__nodes.append(n)
        n.setSupervisor(self)

    def addTickable(self, t):
        """
        Afegeix el triport o component t a la llista de triports controlats pel supervisor.

        :param t: triport o component a afegir
        """
        self.__tickables.append(t)

    def notifyChange(self):
        """
        Notifica al supervisor que un node ha canviat d'estat. Principalment utilitzada pels nodes.
        """
        Supervisor.Changed = True

    def run(self, log = False):
        """
        Fa funcionar el circuit aplicant l'estratègia que s'ha explicat prèviament. Si log és True,
        llavors escriu per la pantalla un missatge cada vegada que provoca un tick en un triport.

        :param log: el log ens serveix per saber quan escriure un missatge per pantalla
        :return: hi ha el return perquè no es quedi en bucle la funció
        """
        Supervisor.Changed = False
        for t in self.__tickables:
            t.tick()
            if(log):
                print "Tick -> {0}".format(t)
        if(Supervisor.Changed):
            self.run(log)
        else:
            return