#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
BitVector
=========

Aquest mòdul conté les següents classes:

BitVector
------------

Aquesta classe representa una paraula binària de mida arbitrària (> o = a 16 bits i sense signe).
És ua classe abstracta, és a dir, només té la funció de ser super-classe.

    ======================== =========== ===================================================
    Atribut                  Tipus       Significat
    ======================== =========== ===================================================
    _w                       int         Codifica el valor del BitVector
    ======================== =========== ===================================================


Funcions
---------

"""
import MainLib,avrException

class OutOfBitRange(avrException.AVRException):
    pass

class _BitVector(object):

    def __init__(self,w=0):
        """
        Constructor
        """
        self._w=self.chek_w(w)

    def chek_w(self,w):
        """
        Comprova que w sigui vàlid
        """
        try:
            if w<=65535:
                if str(w)[:1]=="0b" :
                    return w
                else:
                    return int('{0:b}'.format(w))
            else:
                raise OutOfBitRange()
        except OutOfBitRange:
            MainLib.exception("Binari massa gros, màx 16 bits (65535)", place="BitVector (check_w)")


    def extract_field_u(self,mask):
        """
        Retorna un valor entern corresponent al camp desitjat extret de self aplicant la mascara mask
        """
        length = "{0:" + str(len(self)).zfill(3) + "b}"
        mask=str(length.format(mask))
        num=str(self._w).zfill(len(self))
        result=""
        for i in range(len(mask)):
            if mask[i]=="1":
                result+=num[i]
        return int(result,2)


    def extract_field_s(self,mask):
        """
        Retorna un valor entern amb sibne corresponent al camp desitjat extret de self (interpretat amb complement a 2) aplicant la mascara mask
        """

        length="{0:"+str(len(self)).zfill(3)+"b}"
        mask = length.format(mask)
        num = MainLib.to_signed(int(str(self._w),2),len(self))
        result = ""

        for i in range(8):
            if mask[i] == "1":
                result += num[i]
        result=MainLib.signed_to_int(result,len(self))
        return result





    def __int__(self):
        """
        Retorna l'enter decimal corresponent a self
        """
        return int(str(self._w),2)


    def __index__(self):
        """
        Retorna el mateix que el __int__ però aquest s'utilitza per retornar l'index d'un diccionari

        """
        return int(self)

    def __repr__(self):

        vector=MainLib.to_signed(int(str(self._w),2),len(self))
        return hex(int(str(vector),2))[2:].zfill(len(self)/4).upper()



    def __add__(self,o):
        """
        Suma
        """
        try:
            other=o._w if isinstance(o,_BitVector) else int('{0:08b}'.format(o))
            suma=int(str(self._w),2)+int(str(other),2)
            return self.classe()(suma)

        except Exception as e:
            MainLib.exception(e.message, place="Bitvector (__add__)")


    def __sub__(self,o):
        """
        Resta
        """

        try:
            a=MainLib.signed_to_int(MainLib.to_signed(int(str(self._w),2),len(self)))
            b=MainLib.signed_to_int(MainLib.to_signed(-int(str(o._w),2),len(self))) if isinstance(o,_BitVector) else -o
            return self.classe()(a+b)
        except Exception as e:
            MainLib.exception(e.message, place="BitVector (__sub__)")


    def __and__(self,o):
        """
        AND lògica
        """
        try:
            a=int(str(self._w),2)
            b=int(str(o._w),2) if isinstance(o, _BitVector) else int('{0:08b}'.format(o))
            result=int(bin(a&b),2)
            return self.classe()(result)

        except Exception as e:
            MainLib.exception(e.message, place="BitVector (__and__)")



    def __or__(self,o):
        """
        OR lògica
        """
        try:
            a=int(str(self._w),2)
            b=int(str(o._w),2) if isinstance(o, _BitVector) else int('{0:08b}'.format(o))
            result=int(bin(a|b),2)
            return self.classe()(result)

        except Exception as e:
            MainLib.exception(e.message, place="BitVector (__or__)")


    def __xor__(self,o):
        """
        XOR lògica
        """
        try:
            a=int(str(self._w),2)
            b=int(str(o._w),2) if isinstance(o, _BitVector) else int('{0:08b}'.format(o))
            result=int(bin(a^b),2)
            return self.classe()(result)

        except Exception as e:
            MainLib.exception(e.message, place="BitVector (__xor__)")

    def __invert__(self):
        """
        Inverteix els bits de la representació binària de self
        """
        try:
            w=str(self._w).zfill(len(self))
            invert=""
            for i in range(len(w)):
                invert+='0' if(w)[i]=='1' else '1'
            return self.classe()(int(invert,2))
        except Exception as e:
            MainLib.exception(e.message, place="BitVector (__invert__)")

    def __lshift__(self,i):
        """
        Desplaça i posicions a l'esquerra els bits de l'instància BitVector
        """
        try:
            w=str(self._w).zfill(len(self))
            shift=str(w)[i:]+'0'*(i)
            return self.classe()(int(shift,2))
        except Exception as IndexError:
            MainLib.exception(IndexError.message, place="BitVector (__lshift__)")


    def __rshift__(self,i):
        """
        Desplaça i posicions a la dreta els bits de l'instància BitVector
        """
        try:
            w = str(self._w).zfill(len(self))
            shift = '0'*(i)+str(w)[:-i]
            return self.classe()(int(shift, 2))

        except Exception as IndexError:
            MainLib.exception(IndexError.message, place="BitVector (__rshift__)")

    #TODO: nse quan hauria d'estar fora de rang

    def __eq__(self,o):
        """
        Compara el valor de l'instàcia BitVector amb el d'una altre instància BitVector o bé amb un enter.
        Retorna True si són iguals
        """
        other = o._w if isinstance(o, _BitVector) else int('{0:08b}'.format(o))
        return self._w==other


    def __ne__(self,o):
        """
        Compara el valor de l'instàcia BitVector amb el d'una altre instància BitVector o bé amb un enter.
        Retorna True si són diferents
        """
        other = o._w if isinstance(o, _BitVector) else int('{0:08b}'.format(o))
        return self._w != other


    def __getitem__(self,i):
        """

        """
        try:
            w=str(self._w).zfill(len(self))
            return True if w[-i-1]=='1' else False

        except Exception as KeyError:
            MainLib.exception(KeyError.message, place="BitVector (__getitem__)")


    def __setitem__(self,i,v):
        """
        canvia el bit de la posició i de la representació binària de self per v
        """
        try:
            if(isinstance(v, bool)):
                v = 1 if v else 0;
            w=list(str(self._w).zfill(len(self)))
            w[-i-1]=str(v)
            self._w=int("".join(w))

        except Exception as KeyError:
            MainLib.exception(KeyError.message, place="BitVector (__setitem__)")


class Byte(_BitVector):


    def __len__(self):
        """
        sempre retorna 8
        """
        return 8


    def concat(self,b):
        """
        retorna el Word resultant de concatenar self amb el Byte b. self es MSB i b el LSB
        """
        w=repr(self)
        w+=repr(b)
        return Word(int(w,16))

    def classe(self):
        return Byte

class Word(_BitVector):


    def __len__(self):
        """
        sempre retorna 16
        """
        return 16


    def lsb(self):
        """
        retorna un Byte corresponent als 8 bits de menys per de word
        """
        return Byte(int(repr(self)[2:],16))

    def msb(self):
        """
        retorna un Byte corresponent als 8 bits de més per de word
        """
        return Byte(int(repr(self)[:2], 16))

    def classe(self):
        return Word
