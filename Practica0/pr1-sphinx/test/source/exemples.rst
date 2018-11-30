Exemples de codi inserit en la documentació
===========================================


Es pot inserir codi i exemples d'execucions en la documentació d'una
manera molt senzilla. Pel que fa a execucions senzillament cal fer::

>>> from math import log
>>> x = 3.2
>>> print log(3.2)

El codi també es pot inserir amb aquest mateix procediment. Per
exemple, per sumar una llista, es pot fer servir la primitiva
:py:func:`sum` però també podem emprar una funció definida així::

   def suml(l):
      """
      Retorna la suma dels valors emmagatzemats a la llista l.
      """
      r = 0
      for v in l:
         r += v
      return r



