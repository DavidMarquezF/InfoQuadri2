#coding=UTF-8

"""
Mòdul instruction
=================

Conté les classes que implementen el significat de totes i cadascuna de les operacions de llenguatge màquina que admet el simulador.

"""

from bitVector import *
from avrException import *
from state import *

CARRY = 0
ZERO = 1
NEG = 2

class BreakException(AVRException):
    """
    És una excepció que es llença sistemàticament cada vegada que s'executa la instrucció BRK. S'usa
    per aturar la simulació.
    """
    pass

class IOValueError(AVRException):
    pass

class InstRunner(object):
    """
    La classe InstRunner és la super-classe (abstracta) de totes les classes lligades a instruccions.
    Concentra els (pocs) serveis comuns que aquestes classes lligades a instrucció tenen.
    """

    def __repr__(self):
        """
        Retorna una cadena que representa la instrucció.
        """
        return ""

    def match(self,instr):
        """
        Indica si aquesta instància s'identifica amb l'opcode contingut a instr

        :param instr: :class:`bitVector.Word` que denota una instrucció
        :return: Retorna True ssi aquesta instància pot executar la instrucció instr.
        """
        return self._match(instr)

    def execute(self,instr,state):
        """
        Executa la instrucció i, com a resultat, modifica l’estat del microcontrolador
        al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar,
        obtenir els operands (fetch), calcular el resultat, modificar
        convenientment el registre d’estat i emmagatzemar el resultat.
        
        :param instr: :class:`bitVector.Word` que denota una instrucció
        :param state: instància de tipus State.
        """
        self._execute(instr, state)
        state.pc += 1
        

class ADD(InstRunner):
    """
    Suma registre + registre sense carry
    """
    def __repr__(self):
        return "ADD"


    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b000011

    def _execute(self,instr,state):
        a_reg_desti = instr.extract_field_u(0b0000000111110000)
        reg_desti = state.data[a_reg_desti]
        reg_origen = state.data[instr.extract_field_u(0b0000001000001111)]
        resultat = reg_desti + reg_origen
        state.data[a_reg_desti] = resultat
        state.flags[CARRY] = (reg_desti[7] & reg_origen[7]) | (reg_origen[7] & (not resultat[7])) | ((not resultat[7]) & reg_desti[7])
        state.flags[ZERO] = (resultat == 0)
        state.flags[NEG] = resultat[7]

class ADC(InstRunner):
    """
    Suma registre+registre amb carry.
    """

    def __repr__(self):
        return "ADC"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b000111

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000111110000)
        reg_desti = state.data[a_reg_desti]
        reg_origen = state.data[instr.extract_field_u(0b0000001000001111)]
        resultat = reg_desti + reg_origen + state.flags[CARRY]
        state.data[a_reg_desti] = resultat
        state.flags[CARRY] = (reg_desti[7] & reg_origen[7]) | (reg_origen[7] & (not resultat[7])) | ((not resultat[7]) & reg_desti[7])
        state.flags[ZERO] = (resultat == 0)
        state.flags[NEG] = resultat[7]
        

class SUBI(InstRunner):
    """
    Resta registre-constant sense carry.
    """
    def __repr__(self):
        return "SUBI"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111000000000000)
        return opcode == 0b0101

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000011110000) | (1 << 4)
        reg_desti = state.data[a_reg_desti]
        imediate = Byte(instr.extract_field_u(0b0000111100001111))
        resultat = reg_desti - imediate
        state.data[a_reg_desti] = resultat
        state.flags[CARRY] = ((not reg_desti[7]) & imediate[7]) | (imediate[7] & resultat[7]) | (resultat[7] & (not reg_desti[7]))
        state.flags[ZERO] = (resultat == 0)
        state.flags[NEG] = resultat[7]
        

class SUB(InstRunner):
    """
    Resta registre-registre sense carry
    """

    def __repr__(self):
        return "SUB"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b000110

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000111110000)
        reg_desti = state.data[a_reg_desti]
        reg_origen = state.data[instr.extract_field_u(0b0000001000001111)]
        resultat = reg_desti - reg_origen
        state.data[a_reg_desti] = resultat
        state.flags[CARRY] = ((not reg_desti[7]) & reg_origen[7]) | (reg_origen[7] & resultat[7]) | (resultat[7] & (not reg_desti[7]))
        state.flags[ZERO] = (resultat == 0)
        state.flags[NEG] = resultat[7]
        

class AND(InstRunner):
    """
    And registre-registre.
    """

    def __repr__(self):
        return "AND"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b001000

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000111110000)
        reg_desti = state.data[a_reg_desti]
        reg_origen = state.data[instr.extract_field_u(0b0000001000001111)]
        resultat = reg_desti & reg_origen
        state.data[a_reg_desti] = resultat
        state.flags[ZERO] = (resultat == 0)
        state.flags[NEG] = resultat[7]
        

class OR(InstRunner):
    """
    Or registre-registre.
    """
    def __repr__(self):
        return "OR"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b001010

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000111110000)
        reg_desti = state.data[a_reg_desti]
        reg_origen = state.data[instr.extract_field_u(0b0000001000001111)]
        resultat = reg_desti | reg_origen
        state.data[a_reg_desti] = resultat
        state.flags[ZERO] = (resultat == 0)
        state.flags[NEG] = resultat[7]
        

class EOR(InstRunner):
    """
    Or exclusiva registre-registre.
    """
    def __repr__(self):
        return "EOR"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b001001

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000111110000)
        reg_desti = state.data[a_reg_desti]
        reg_origen = state.data[instr.extract_field_u(0b0000001000001111)]
        resultat = reg_desti ^ reg_origen
        state.data[a_reg_desti] = resultat
        state.flags[ZERO] = (resultat == 0)
        state.flags[NEG] = resultat[7]
        

class LSR(InstRunner):
    """
    Desplaçament dreta registre.
    """
    def __repr__(self):
        return "LSR"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111111000001111)
        return opcode == 0b10010100110

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000111110000)
        reg_desti = state.data[a_reg_desti]
        resultat = reg_desti >> 1
        state.flags[CARRY] = reg_desti[0]
        state.flags[ZERO] = (resultat == 0)
        state.data[a_reg_desti] = resultat
        

class MOV(InstRunner):
    """
    Còpia registre-registre
    """
    def __repr__(self):
        return "MOV"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b001011

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000111110000)
        a_reg_origen = instr.extract_field_u(0b0000001000001111)
        state.data[a_reg_desti] = state.data[a_reg_origen]
        

class LDI(InstRunner):
    """
    Assigna valor a registre.
    """
    def __repr__(self):
        return "LDI"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111000000000000)
        return opcode == 0b1110

    def _execute(self,instr,state):

        a_reg_desti = instr.extract_field_u(0b0000000011110000) | (1 << 4)
        k = Byte(instr.extract_field_u(0b0000111100001111))
        state.data[a_reg_desti] = k
        

class RJMP(InstRunner):
    """
    Salt relatiu a una nova instrucció.
    """
    def __repr__(self):
        return "RJMP"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111000000000000)
        return opcode == 0b1100

    def _execute(self,instr,state):
        constant = instr.extract_field_s(0b0000111111111111)
        state.pc +=constant


class BRBS(InstRunner):
    """
    Salta a adreça de programa si cert bit de FLAGS és 1.
    """
    def __repr__(self):
        return "BRBS"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b111100

    def _execute(self,instr,state):
        constant = instr.extract_field_s(0b000000111111000)
        bit = instr.extract_field_u(0b000000000000111)
        if not state.flags[bit]:
            constant = 0
        state.pc += constant

class BRBC(InstRunner):
    """
    Salta a adreça de programa si cert bit de FLAGS és 0.
    """
    def __repr__(self):
        return "BRBC"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b111101

    def _execute(self,instr,state):

        constant = instr.extract_field_s(0b000000111111000)
        bit = instr.extract_field_u(0b000000000000111)
        if state.flags[bit]:
            constant = 0
        state.pc += constant

class NOP(InstRunner):
    """
    No fa res. La instrucció nul·la.
    """

    def __repr__(self):
        return "NOP"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111111111111111)
        return opcode == 0b0

    def _execute(self,instr,state):
        pass

        

class BREAK(InstRunner):
    """
    Atura la simulació i acaba l'execució del programa simulador.
    """

    def __repr__(self):
        return "BREAK"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111111111111111)
        return opcode == 0b1001010110011000

    def _execute(self,instr,state):
        raise BreakException("Simulation ended")

class IN(InstRunner):
    """
    Quan s'aplica al port 0x0, llegeix un caràcter del teclat.
    """
    def __repr__(self):
        return "IN"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111100000000000)
        return opcode == 0b10110

    def _execute(self,instr,state):

        reg_desti = instr.extract_field_u(0b0000000111110000)
        adr = instr.extract_field_u(0b0000011000001111)
        try:
            if adr == 0:
                c = raw_input("Type I/O input in hex, bin, or int format: ").lower()
                if c[:2] == "0b":
                    c = c[2:]
                    base = 2
                elif c[:2] == "0x":
                    c = c[2:]
                    base = 16
                else:
                    base = 10
                try:
                    c = int(c,base)
                except ValueError:
                    raise IOValueError("The input must be in hex, bin or int with specified base.")
                state.data[reg_desti] = Byte(c)
            else:
                raise IOValueError("I/O input adress not valid (PC: {})".format(state.pc))
        except IOValueError as e:
            MainLib.exception(e.message, place="Instruction (IN)")

class OUT(InstRunner):
    """
    S'usa per escriure per la pantalla.
    """

    def __repr__(self):
        return "OUT"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111100000000000)
        return opcode == 0b10111

    def _execute(self,instr,state):

        reg_origen = state.data[instr.extract_field_u(0b0000000111110000)]
        adr = instr.extract_field_u(0b0000011000001111)
        try:
            if adr == 0:
                MainLib.logInfo("IN/OUT","OUT: " + str(int(reg_origen)))
            elif adr == 1:
                MainLib.logInfo("IN/OUT","OUT: " + repr(reg_origen))
            elif adr == 2:
                MainLib.logInfo("IN/OUT","OUT: " + chr(int(reg_origen)).upper())
            else:
                raise IOValueError("I/O output adress not valid (PC: {})".format(str(state.pc)))
        except IOValueError as e:
            MainLib.exception(e.message, place="Instruction (OUT)")

class LDS(InstRunner):
    """
    Còpia memòria a registre.
    """

    def __repr__(self):
        return "LDS"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111100000000000)
        return opcode == 0b10100

    def _execute(self,instr,state):

        reg_desti = instr.extract_field_u(0b0000000011110000) | (1 << 4)
        k = Byte(instr.extract_field_u(0b0000011100001111))
        adress = Byte(k.extract_field_u(0b1111))
        adress[3] = k[5]
        adress[2] = k[6]
        adress[1] = k[4]
        adress[0] = not k[4]
        state.data[reg_desti] = state.data[adress]
        

class STS(InstRunner):
    """
    Còpia registre a memòria.
    """

    def __repr__(self):
        return "STS"

    def _match(self,instr):
        opcode = instr.extract_field_u(0b1111100000000000)
        return opcode == 0b10101

    def _execute(self,instr,state):
       
        reg_desti = instr.extract_field_u(0b0000000011110000) | (1 << 4)
        k = Byte(instr.extract_field_u(0b0000011100001111))
        adress = Byte(k.extract_field_u(0b1111))
        ka=str(k._w).zfill(8)
        ad=str(adress._w).zfill(7)

        adress[3] = k[5]
        adress[2] = k[6]
        adress[1] = k[4]
        adress[0] = not k[4]
        state.data[adress] =state.data[reg_desti]
        

