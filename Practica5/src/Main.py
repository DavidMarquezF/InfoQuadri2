#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Node import *
from Entrada import *
from Triport import *
from Supervisor import *
from Component import Component
import PredefinedCircuits

if(__name__ == "__main__"):
    main = PredefinedCircuits.CreateMainCircuit()
    # fixem les entrades i simulem
    main.GetEntrada("E1").up()
    main.GetEntrada("E2").up()
    main.GetEntrada("E3").down()
    main.GetEntrada("E4").up()


    e1 = Entrada("E1")
    s = Sortida('S2')
    # definim el circuit
    n1 = Node('N1')
    a1 = And(e1, main.GetSortida("S1"), s)

    sup = Supervisor()
    sup.addNode(n1)
    sup.addNode(s)

    sup.addTickable(a1)
    sup.addTickable(main)

    e1.up()
    sup.run()



    # escrivim resultats
    print main.GetSortida("S1")
    print s

    print "Full Adder-----------------------------"
    fullAdder = PredefinedCircuits.FullAdder()

    sup = Supervisor()
    sup.addTickable(fullAdder)
    print "1 + 1"
    fullAdder.GetEntrada("A").up()
    fullAdder.GetEntrada("B").up()
    fullAdder.GetEntrada("Cin").down()
    sup.run()
    print fullAdder.GetSortida("S")
    print fullAdder.GetSortida("Cout")
    print "1 + 0"
    fullAdder.GetEntrada("A").down()
    fullAdder.GetEntrada("B").down()
    fullAdder.GetEntrada("Cin").up()
    sup.run()
    print fullAdder.GetSortida("S")
    print fullAdder.GetSortida("Cout")
    print "0 + 0"
    fullAdder.GetEntrada("A").down()
    fullAdder.GetEntrada("B").down()
    fullAdder.GetEntrada("Cin").down()
    sup.run()
    print fullAdder.GetSortida("S")
    print fullAdder.GetSortida("Cout")
    print "1 + 1 + 1"
    fullAdder.GetEntrada("A").up()
    fullAdder.GetEntrada("B").up()
    fullAdder.GetEntrada("Cin").up()
    sup.run()
    print fullAdder.GetSortida("S")
    print fullAdder.GetSortida("Cout")




