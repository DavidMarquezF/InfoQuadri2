=============
Usant autodoc
=============

Introducció
===========

Una situació habitual es dona quan volem docuemntar un mòdul o
programa. En aquest cas ens trobarem que el propi codi ja conté una
quantitat important de documentació. Autodoc permet incorporar aquesta
informació a la documentació de manera automàtica. A tal efecte cal:

* Indicar on es troben els mòduls a documentar.
* Afegir a l adocuemntació les clausules necessàries per que incorpori
  aquesta informació.


Indicar on es troben
====================

Cal fer-ho en el fitxer :file:`conf.py`. Per exemple::

   # If extensions (or modules to document with autodoc) are in another directory,
   # add these directories to sys.path here. If the directory is relative to the
   # documentation root, use os.path.abspath to make it absolute, like shown here.
   sys.path.insert(0, os.path.abspath('../../src'))



Incorporar la informació
========================

Es pot fer senzillament amb la construcció següent:


.. code-block:: rest

   .. automodule:: bdu	
      :members:


En el capítol següent podeu veure el resultat d'aquesta
construcció. S'ha inclos automàticament la documentació del mòdul
:module:`bdu`.
