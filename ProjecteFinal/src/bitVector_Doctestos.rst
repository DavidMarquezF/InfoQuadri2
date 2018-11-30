=========================
Test del mòdul bitVector
=========================

Com `bitVector` és una classe abstracta, els tests els realitzem
únicament sobre les classes derivades.

Classe Byte i Word
==================

.. code-block:: python

    >>> from bitVector import Byte, Word

Comprovem que el constructor i el metode __repr__ funciona correctament, així assegurem que els objectes es creen tal com toca:

.. code-block:: python

    >>> print Byte(10)
    0A
    >>> print Word(10)
    000A
    >>> print Byte(1)
    01
    >>> print Byte(15)
    0F
    >>> print Byte(-1)
    FF
    >>> print Byte(403)
    93
    >>> print Byte(255)
    FF

Amb el mètode predefinit __len__() podem obtenir la longitud corresponent de Byte o de Word.

.. code-block:: python

    >>> print len(Word(24))
    16
    >>> print len(Byte(4))
    8

Les seguents funcions s'encarreguen d'extreure els bits que ens interessen de cada insància bitVector:

.. code-block:: python

    >>> Byte(166).extract_field_u(51)
    10
    >>> Byte(-166).extract_field_s(51)
    6
    >>> Byte(166).extract_field_s(51)
    -6

Els metodes __índex__() i __int__() retornen un int corresponent al valor de l'instancia bitVector.
Malgrat retornin el mateix, normalment sempre s'implementen plegats ja que un servirà per la conversió
de binari a decimal, i l'altre per per generar l'index d'un diccionari.

.. code-block:: python

    >>> int(Byte(7))
    7
    >>> int(Byte(0b1011))
    11
    >>> int(Word(403))
    403
    >>> Byte(7).__index__()
    7
    >>> Byte(0b1011).__index__()
    11
    >>> Word(403).__index__()
    403

A continuació comprovarem que els mètodes corresponents a les operacions funcionen tal com toca

.. code-block:: python

    >>> Byte(2)+Byte(12)
    0E
    >>> Byte(12)+2
    0E
    >>> Byte(12)-Byte(2)
    0A
    >>> Byte(12)-2
    0A
    >>> Byte(8)&Byte(8)
    08
    >>> Byte(7)&Byte(0b0010)
    02
    >>> Byte(0xff)&Byte(0b1011)
    0B
    >>> Byte(24)|Byte(8)
    18
    >>> Byte(7)|Byte(0b0010)
    07
    >>> Byte(3)|Byte(4)
    07
    >>> Byte(24)^Byte(8)
    10
    >>> Byte(0xff)^Byte(0b1011)
    F4
    >>> ~Byte(24)
    E7
    >>> ~Byte(0xf0)
    0F
    >>> print ~Byte(0b101010)
    D5
    >>> Byte(1)<<4
    10
    >>> Byte(0xfe)<<3
    F0
    >>> Byte(0xff)>>4
    0F
    >>> Byte(2)==2
    True
    >>> Byte(8)==Byte(8)
    True
    >>> Byte(12)==-12
    False
    >>> Byte(2)!=2
    False
    >>> Byte(8)!=Byte(8)
    False
    >>> Byte(12)!=-12
    True

Els seguents mètodes serveixen per consultar i modificar posicions determinades de la representació binària de les instàncies bitVector

.. code-block:: python

    >>> Byte(2)[0]
    False
    >>> Byte(2)[1]
    True
    >>> Byte(10)[7]
    False
    >>> a=Byte(2)
    >>> a[1]=0
    >>> print a
    00
    >>> b=Byte(4)
    >>> b[0]=1
    >>> print b
    05

Aquest mètode està unicament implementat per a la classe Byte. S'utilitza per generar un Word a partir de la concatenació de dos Bytes.

.. code-block:: python

    >>> b=Byte(255)
    >>> c=Byte(0)
    >>> d=b.concat(c)
    >>> print d
    FF00

Aquests mètodes estàn unicament implementats per a la classe Word. Serveixen per extreuren una instància de Byte corresponent al MSB o
al LSB, segons la funció.

.. code-block:: python

    >>> Word(255).lsb()
    FF
    >>> Word(65535).lsb()
    FF
    >>> Word(255).msb()
    00
    >>> Word(65535).msb()
    FF