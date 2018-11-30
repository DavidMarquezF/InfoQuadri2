# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Tickable(object):
    """

    Classe mare de tots els elements que siguin supervisats per un :class:`Supervisor.Supervisorr`

    Conté la funció tick que obliga que tots els fills d'aquesta classe implementin la funció protegida _tick.

    """
    def tick(self):
        """
        Funció utilitzada per forçar a tots els fills d'aquesta classe implementar self._tick, que és necessària quan un
        supervisor la crida
        """
        self._tick()