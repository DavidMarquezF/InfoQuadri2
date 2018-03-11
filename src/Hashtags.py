#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
======================
Classe Hashtag
======================

"""
class Hashtag(object):
    """
    Aquesta classe s'encarrega de crear els hashtags
    ======================= ========= =========================================================================
     Atribut                 Tipus                       Significat
    ======================= ========= =========================================================================
     +id                     string    És el hashtag que es vol posar.
   ======================= ========= =========================================================================


    """
    def __init__(self,id):
        self.id=id

    def __eq__(self, other):
        return self.id==other.id

    def __str__(self):
        return "#" + self.id


