=====================
Pràctica 1: iTICBanck
=====================

:Author: David Marquez i Ferran Godoy
:Date: 20/02/2018

Objectius
=========

L’objectiu del problema a resoldre consisteix en aprendre a crear una classe en Python que
compleixi les especificacions demanades i provar-ne la seva funcionalitat. A tal efecte se us demana
que dissenyeu i implementeu un aplicatiu que simuli el funcionament dels comptes corrents d’un
banc.

El primer que cal destacar és que tracta d’un exercici acadèmic, l’objectiu del qual és la
implementació d’una aplicació d’una certa complexitat. En aquest sentit, cal tenir en compte
que la funcionalitat descrita a l’enunciat constitueix una simplificació de la realitat, i en algun
aspecte concret, pot diferir de la pràctica habitual de les operacions descrites. A continuació
segueix el llistat de requeriments d’especificació que ha de complir l’aplicatiu a desenvolupar.

Temps dedicat a les tasques
===========================

====== ========= ========== =========
Tasca   David M.  Ferran G.  Total
====== ========= ========== =========
T1        20min     0min      20min
T2         1h        10min    1h10min
T3        10min      3h       3h10min
T4          2h       2h         4h

Total   3h30min    5h10min    8h40min
====== ========= ========== =========




Toc personal
============

El nostre toc personal ha consistit en crear un banc funcional, que permet les següents opcions:

1. Afegir i eliminar usuaris
2. Mostrar informació bancària dels usuaris
3. Mostrar una llista completa dels usuaris amb les seves comptes
4. Cobrar interessos mensuals de tots els usuaris.

Un Usuari és un contenidor d'informació bancaria, nom i contrassenya per accedir-hi.
Quan es crea un usuari se l'hi assigna un ID aleatòri i uns interessos mensuals també aleatoris.

Per assolir aquest comportament hem implementat dos mòduls:

* El mòdul :ref:`usuari-link` - Per fer la gestió d'usuaris
* El mòdul :ref:`bank-link` - Per fer la gestió del banc