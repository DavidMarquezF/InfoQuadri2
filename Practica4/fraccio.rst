===================================================
Pràctica 4:Control de versions i treball concurrent
===================================================

:Author: David Marquez i Ferran Godoy
:Date: 11/03/2018

Classe Fraccio
==============

Aquesta classe s'encarrega de les operacions necessàries amb fraccions.

Té dues variables:

    1. Numerador
    #. Denominador

Hem fet que es simplifiqui sola (es fa en el constructor, cridant una variable privada __simplifica que ho fa).

Aquesta classe pot realitzar les següents operacions:

    1. Suma
    #. Resta
    #. Multiplicació
    #. Divisió
    #. Negació

També hem gestionat una mica els errors possibles (crear fraccions amb strings, etc.)

Un doctest de la classe seria el seguent:

.. code-block:: python

    >>> from fraccio import *
    >>> f = Fraccio(2,4)
    >>> print repr(f)
    1/2
    >>> f1 = Fraccio(3,4)
    >>> print repr(f1)
    3/4
    >>> print repr(f + f1)
    5/4
    >>> print repr(f - f1)
    -1/4
    >>> print repr(f * f1)
    3/8
    >>> print repr(f / f1)
    2/3
    >>> print repr(-f)
    -1/2


