#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
=========================
Mòdul Predefined Circuits
=========================

En aquest mòdul s'inclouen alguns circuits predefinits utilitzant el sistema de components (toc personal :class:`Component.Component`)

"""

from Node import *
from Entrada import *
from Triport import *
from Supervisor import *
from Component import Component

def CreateMainCircuit():
    """
    Crea un component que fa el que se'ns havia demanat a la pràctica (el circuit proposat)

    :return: Un component amb el comportament del circuit proposat a la pràctica.
    """
    # definim 4 entrades
    e1 = Entrada("E1")
    e2 = Entrada("E2")
    e3 = Entrada("E3")
    e4 = Entrada('E4')

    # definim 1 sortida
    s = Sortida('S1')

    defaultC = Component({e1.getName(): e1, e2.getName(): e2, e3.getName(): e3, e4.getName(): e4}, {s.getName(): s}, "Main Circuit")

    # definim el circuit
    n1 = Node('N1')
    a1 = And(e1, e2, n1)
    n2 = Node('N2')
    a2 = And(e3, e4, n2)
    a3 = And(n1, n2, s)

    # creem un supervisor i l'informem dels nodes i triports que ha de supervisar
    sup = Supervisor()
    sup.addNode(n1)
    sup.addNode(n2)
    sup.addNode(s)

    sup.addTickable(a1)
    sup.addTickable(a2)
    sup.addTickable(a3)

    defaultC.AddArchitecture([n1, a1, n2, a2, a3], sup)

    return defaultC

def FullAdder():
    """
    Retorna un component amb el funcionament d'un full-adder (suma A, B i Cin).

    :return: Un component amb el comportament d'un full-adder
    """
    e1 = Entrada("A")
    e2 = Entrada("B")
    e3 = Entrada("Cin")

    s = Sortida('S')
    s1 = Sortida('Cout')

    componentFullAdder = Component({e1.getName(): e1, e2.getName(): e2, e3.getName(): e3}, {s.getName(): s, s1.getName() : s1}, "Full Adder")

    #calcul s
    n1 = Node("N1")
    x = XOR(e1, e2, n1)
    x2 =XOR(e3, n1, s)

    #Cout
    n2 = Node("N2")
    a1 = And(e3, n1, n2)
    n3 = Node("N3")
    a2 = And(e1,e2,n3)
    o = Or(n2,n3,s1)

    sup = Supervisor()
    sup.addNode(n1)
    sup.addNode(n2)
    sup.addNode(n3)
    sup.addNode(s)
    sup.addNode(s1)

    sup.addTickable(x)
    sup.addTickable(x2)
    sup.addTickable(a1)
    sup.addTickable(a2)
    sup.addTickable(o)

    componentFullAdder.AddArchitecture([n1,n2,n3,a1,a2,o,x,x2], sup)
    return componentFullAdder
