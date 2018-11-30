=================
Test mòdul AvrMcu
=================

.. code-block:: python

  >>> from AVRMCU import *

Classe Avrmcu
=============

.. code-block:: python

      >>> avr = Avrmcu(prog=8)
      >>> avr.set_prog([0b1110111101100011,0b1110011100010001,0b00001100100010001,0x2e01,0x2200,0x9598])
      >>> print avr.dump_prog()
      0000: EF63
      0001: E711
      0002: 1911
      0003: 2E01
      0004: 2200
      0005: 9598
      >>> avr.set_trace(True)
      >>> avr.run()
      AVR Log: Memory - Write value F3 to memory 22
      AVR Log: Memory - Write value 71 to memory 17
      AVR Log: Memory - Read value 71 from memory 17
      AVR Log: Memory - Read value 00 from memory 1
      AVR Log: Memory - Write value 71 to memory 17
      AVR Log: Memory - Read value 71 from memory 17
      AVR Log: Memory - Write value 71 to memory 0
      AVR Log: Memory - Read value 71 from memory 0
      AVR Log: Memory - Read value 00 from memory 16
      AVR Log: Memory - Write value 00 to memory 0
      AVR Log: Break - Simulation ended
      >>> print avr.dump_reg()
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
      R17: 71
      R18: 00
      R19: 00
      R20: 00
      R21: 00
      R22: F3
      R23: 00
      R24: 00
      R25: 00
      R26: 00
      R27: 00
      R28: 00
      R29: 00
      R30: 00
      R31: 00
      R32: 00
      R33: 00
      R34: 00
      R35: 00
      R36: 00
      R37: 00
      R38: 00
      R39: 00
      R40: 00
      R41: 00
      R42: 00
      R43: 00
      R44: 00
      R45: 00
      R46: 00
      R47: 00
      R48: 00
      R49: 00
      R50: 00
      R51: 00
      R52: 00
      R53: 00
      R54: 00
      R55: 00
      R56: 00
      R57: 00
      R58: 00
      R59: 00
      R60: 00
      R61: 00
      R62: 00
      R63: 00
      R64: 00
      R65: 00
      R66: 00
      R67: 00
      R68: 00
      R69: 00
      R70: 00
      R71: 00
      R72: 00
      R73: 00
      R74: 00
      R75: 00
      R76: 00
      R77: 00
      R78: 00
      R79: 00
      R80: 00
      R81: 00
      R82: 00
      R83: 00
      R84: 00
      R85: 00
      R86: 00
      R87: 00
      R88: 00
      R89: 00
      R90: 00
      R91: 00
      R92: 00
      R93: 00
      R94: 00
      R95: 00
      R96: 00
      R97: 00
      R98: 00
      R99: 00
      R100: 00
      R101: 00
      R102: 00
      R103: 00
      R104: 00
      R105: 00
      R106: 00
      R107: 00
      R108: 00
      R109: 00
      R110: 00
      R111: 00
      R112: 00
      R113: 00
      R114: 00
      R115: 00
      R116: 00
      R117: 00
      R118: 00
      R119: 00
      R120: 00
      R121: 00
      R122: 00
      R123: 00
      R124: 00
      R125: 00
      R126: 00
      R127: 00
      X(R27:R26): 0000
      Y(R29:R28): 0000
      Z(R31:R30): 0000
      PC: 0005
      CARRY: 0 ZERO: 1 NEG: 0
