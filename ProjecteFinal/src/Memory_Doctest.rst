=====================
Test del mòdul Memory
=====================

Com `Memory` és una classe abstracta, els tests els realitzem
únicament sobre les classes derivades.

Classe `ProgramMemory`
======================

.. code-block:: python

    >>> from memory import *
    >>> from bitVector import Byte, Word

Comprovem si el constructor i __repr__ funcionen correctament (si __repr__ funciona implica que dum també):

.. code-block:: python

    >>> print ProgramMemory(32)
    0000: 0000
    0001: 0000
    0002: 0000
    0003: 0000
    0004: 0000
    0005: 0000
    0006: 0000
    0007: 0000
    0008: 0000
    0009: 0000
    0010: 0000
    0011: 0000
    0012: 0000
    0013: 0000
    0014: 0000
    0015: 0000
    0016: 0000
    0017: 0000
    0018: 0000
    0019: 0000
    0020: 0000
    0021: 0000
    0022: 0000
    0023: 0000
    0024: 0000
    0025: 0000
    0026: 0000
    0027: 0000
    0028: 0000
    0029: 0000
    0030: 0000
    0031: 0000

Comprovem que el getItem funciona:

.. code-block:: python

    >>> a = ProgramMemory(32)
    >>> print a[0]
    0000
    >>> a.traceOn()
    >>> a[0]
    AVR Log: Memory - Read value 0000 from memory 0
    0000


Comprovem si setItem funciona:

.. code-block:: python

    >>> a = ProgramMemory(32)
    >>> a[0] = Word(2)
    >>> a.traceOn()
    >>> a[1] = Word(3)
    AVR Log: Memory - Write value 0003 to memory 1

Classe `DataMemory`
======================
Importem les eines

.. code-block:: python

    >>> from memory import *
    >>> from bitVector import Byte, Word

Comprovem si el constructor i __repr__ funcionen correctament (si __repr__ funciona implica que dum també):

.. code-block:: python

    >>> print DataMemory(32)
    0000: 00
    0001: 00
    0002: 00
    0003: 00
    0004: 00
    0005: 00
    0006: 00
    0007: 00
    0008: 00
    0009: 00
    0010: 00
    0011: 00
    0012: 00
    0013: 00
    0014: 00
    0015: 00
    0016: 00
    0017: 00
    0018: 00
    0019: 00
    0020: 00
    0021: 00
    0022: 00
    0023: 00
    0024: 00
    0025: 00
    0026: 00
    0027: 00
    0028: 00
    0029: 00
    0030: 00
    0031: 00
    >>> print DataMemory(2)
    0000: 00
    0001: 00
    0002: 00
    0003: 00
    0004: 00
    0005: 00
    0006: 00
    0007: 00
    0008: 00
    0009: 00
    0010: 00
    0011: 00
    0012: 00
    0013: 00
    0014: 00
    0015: 00
    0016: 00
    0017: 00
    0018: 00
    0019: 00
    0020: 00
    0021: 00
    0022: 00
    0023: 00
    0024: 00
    0025: 00
    0026: 00
    0027: 00
    0028: 00
    0029: 00
    0030: 00
    0031: 00

Comprovem que el getItem funciona:

.. code-block:: python

    >>> a = DataMemory(32)
    >>> print a[0]
    00
    >>> a.traceOn()
    >>> a[0]
    AVR Log: Memory - Read value 00 from memory 0
    00
  

Comprovem si setItem funciona:

.. code-block:: python

    >>> a = DataMemory(32)
    >>> a[0] = Byte(2)
    >>> a.traceOn()
    >>> a[1] = Byte(3)
    AVR Log: Memory - Write value 03 to memory 1

Probem que dump_reg funcioni:

.. code-block:: python

    >>> a = DataMemory(32)
    >>> print a.dump_reg()
    R00: 00
    R01: 00
    R02: 00
    R03: 00
    R04: 00
    R05: 00
    R06: 00
    R07: 00
    R08: 00
    R09: 00
    R10: 00
    R11: 00
    R12: 00
    R13: 00
    R14: 00
    R15: 00
    R16: 00
    R17: 00
    R18: 00
    R19: 00
    R20: 00
    R21: 00
    R22: 00
    R23: 00
    R24: 00
    R25: 00
    R26: 00
    R27: 00
    R28: 00
    R29: 00
    R30: 00
    R31: 00
    X(R27:R26): 0000
    Y(R29:R28): 0000
    Z(R31:R30): 0000



