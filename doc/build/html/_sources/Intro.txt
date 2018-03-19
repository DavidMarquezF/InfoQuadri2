=========================================================
Pràctica 3: Gestió de la Xarxa Social iTICApp: Ampliació
=========================================================

:Author: David Marquez i Ferran Godoy
:Date: 19/03/2018

Objectius
=========

L’objectiu d’aquesta pràctica és prendre contacte amb els programes estructurats en base a
classes d’objectes. El context del projecte se sitúa en una xarxa social, en el marc d’un projecte
de recerca sobre els seus usuaris i els posts que publiquen a la xarxa.
Després d’haver lliurat la pràctica 2, en que es construı̈a una aplicació per a la gestió d’usuaris
i posts, en aquesta ampliació ens proposem els següents objectius:

* Millorar lleugerament l’intèrpret d’ordres.
* Afegir ordres per desar les dades en un fitxer i recuperar-les més endavant.
* Simplificar la lectura i gravació de dades.

Les tasques cal fer-les durant aquesta sessió de laboratori i no haurien de suposar més temps.
Aquesta pràctica també us la podeu prendre com una auto-avaluació. Haurı́eu de veure-us
capaços de poder-la fer individualment si heu treballat convenientment la pràctica 2.

Temps dedicat a les tasques
===========================

====== ========= ========== =========
Tasca   David M.  Ferran G.  Total
====== ========= ========== =========
T1        5min     5min      10min
T2        10min     0min     10min
T3        20min      20min    40min
T4        2:00h      2:00h     4h
T5        10min     10min     20min
T6        10min     10min     20min
T7        10min     10min     20min

Total   3:05h     2:55h          6h
====== ========= ========== =========




Toc personal
============

Tot i que aquesta pràctica no requeria el toc personal, nosaltres al implementar desa i recupera ho hem d'una manera
lleugerament diferent a la plantejada en les tasques. Hem fet que es creein 3 fitxers (un per usuaris, l'altre per posts
i l'últim per hashtags) i aquests es guarden dins d'un directori que especifica l'usuari. Cada vegada que s'inicialitza
l'intèrpret es demana des de quin directori es vol carregar les dades. Si el directori no existeix o no conté els fitxers
requerits es seguirà demanant fins que se'n tingui un de vàlid.

A partir d'aquest directori es recuperaran totes les dades i si no hi ha cap problema es crearà la instancia de iTICApp amb
aquestes dadaes. En el cas que no es puguin recuperar les dades (alguna malformació en el fitxer, etc.) Es donarà dues opcions:
crear una iTICApp nova o seleccionar un altre directori.

Quan es surt de l'intèrpret es demana a on es vol guardar la informació (directori). Si el directori no existeix ses crearà
un directori nou amb els fitxers necessaris. Si el directori existeix i té els fitxer correctes a dins
es demanarà si es vol sobreescriure'l.

D'aquesta manera hem aconseguit que les dades quedin molt més ordenades i més clares i a més a més l'usuari pot triar a on
guardarles.


