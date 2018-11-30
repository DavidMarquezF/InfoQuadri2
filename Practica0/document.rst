================
Títol principal
================

: author : Pere Pi

Apartat
=======

Aquest es el primer apartat. Escriviu-lo aixi com el veieu aqui.
Fixeu-vos que , com en Python, les tabulacions son molt importants ates
que determinen l’estructura del document.

Subapartat
----------

Tambe podeu escriure enumeracions i llistes convencionals usant una
sintaxi molt natural com la que segueix:

    * Primer element
    * Segon element
      - Primera subllista
      - Segona subllista
    * Tercer element

Una altra facilitat molt corrent es la de poder inserir codi o exemples
de programacio d’una forma senzilla i elegant com per exemple:

.. code-block:: python

    def exemple(a,b):
    """
    Una funció per exemplificar reST
    """
    x = a
    for i in b:
        if i % 2 == 0:
            x += a
    return x