=============================
Escriure amb RestructuredText
=============================

`RestructuredText`_ és un format d'escriptura dels anomenats "àgils",
que permeten escriure document d'una forma molt senzilla però
eficient. Aquests formats són hereus de la tradició dels wiki's. 

Tots els formats àgils s'escriuen en un fitxer de text convencional
amb un editor de textos com emacs. Després, els fitxers es poden
traduir a formats de sortida habituals com podria ser pdf.

En el cas de `RestructuredText`_, una de les seves característiques
principals és que, el fitxer de text original "imita" en certa manera
com serà el resultat final. D'aquesta manera resulta mé senzill
treballar-hi.

Escriure amb reST, és senzill. Amb l'editor proveu de crar un fitxer
de nom :file:`document.rst` amb aquest contingut:

.. code-block:: rest

   ================
   Títol principal
   ================

   :author: Pere Pi

   Apartat
   =======

   Aquest és el primer apartat. Escriviu-lo així com el veieu aquí.
   Fixeu-vos que, com en Python, les tabulacions són molt importants atès
   que determinen l'estructura del document.

   Subapartat
   ----------

   També podeu escriure enumeracions i llistes convencionals usant una sintaxi
   molt natural com la que segueix:

     * Primer element
     * Segon element
       - Primera subllista
       - Segona subllista
     * Tercer element

   Una altra facilitat molt corrent és la de poder inserir codi o exemples
   de programació d'una forma senzilla i elegant com per exemple:

   .. code-block:: python

      def exemple(a,b):
         """
	 Una funció per exemplificar reST
	 """
	 x = a
	 for i in b:
	    if i % 2 == 0: x += a
         return x


 

Una vegada hagueu escrit el contingut anterior, processeu el fitxer
:file:`document.rst` fent:

.. code-block:: bash

   $ rst2pdf document.rst
   $ ls -l document.*

Haureu comprovat que s'ha creat un fitxer de nom :file:`document.pdf`
que ara podeu veure fent servir el visualitzador de l'escriptori.

.. note::

   Es important que practiqueu l'escriptura amb reST unes quantes
   vegades per acostumar-vos a la seva sintaxi. La `documentació
   d'Sphinx conté un apartat <http://sphinx.pocoo.org/rest.html>`_ en
   que es resumeix la forma d'escriure de reST.

   També **és important** fer-se un petit xuletari amb les principals
   construccions de reST i tenir-lo a mà quan es treballa.


.. _RestructuredText: http://docutils.sourceforge.net

