===========
Introducció
===========

En la producció de programari i en l'àmbit tecnològic en general la
documentació tècnica té un paper fonamental. En aquesta pràctica
estudiarem el problema de la documentació del programari i també
algunes eines com `Sphinx`_ que simplifiquen aquesta feina.

Entenem per documentació tècnica d'un programari tot aquella
documentació que descriu amb precissió com és aquest programari i com
se'n fa ús quan el lector target és una persona de perfil tècnic.
Entre altres coses pot descriure:

  * L'arquitectura del programa o mòdul. És a dir de quins blocs està
    format, quina funcionalitat tenen i quines interrelacions hi ha
    entre ells.

  * Les funcions de cada mòdul i la seva especificació.

  * Documentació d'utilització incloent doctests i altres exemples
    d'ús.

  * Principis de disseny que s'han utilitzat.

  * Referències a altres documents importants en relació a aquest
    software.

La documentació resultant ha de ser consultable sobre una diversitat
de formats. Aquests inclouen formats habituals com ara:

  * HTML
  * pdf

Aquest és un primer exemple de documentació escrita amb
`Sphinx`_. `Sphinx`_ és un generador de documentació tècnica
especialment orientat al software, tot i que pot usar-se en altres
contextos i serà l'objectiu principal d'aquesta pràctica.

Sphinx pot obtenir la documentació de:

  * Documentació escrita explícitament per l'usuari en format
    `RestructuredText`_.

  * Documentació extreta automàticament d'un programa (per exemple
    Python). A partir del codi i dels comentaris que hi ha en el codi.
    Millora si els comentaris del codi s'escriuen usant
    `RestructuredText`_.

.. note::

   Atenció! Si seguiu llegint aquest text mireu d'anar-ho provant
   simultàniament en el vostre computador. Així ho entendreu millor.

.. _RestructuredText:  http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx.pocoo.org

