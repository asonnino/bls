.. BLS documentation master file, created by
   sphinx-quickstart on Wed May 23 12:24:34 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to BLS's documentation!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. image:: https://img.shields.io/badge/license-BSD-brightgreen.svg
    :target: https://github.com/asonnino/bls/blob/master/LICENSE

.. image:: https://travis-ci.org/asonnino/bls.svg?branch=master
    :target: https://travis-ci.org/asonnino/bls

.. image:: https://readthedocs.org/projects/bls-lib/badge/?version=latest
    :target: https://readthedocs.org


A simple Python implementation of threshold BLS signatures.

A link to the full paper is available here_. 

.. _here: https://iacr.org/archive/asiacrypt2001/22480516.pdf


Pre-requisites
--------------
This implementation is built on top of petlib_ , make sure to follow `these instructions`_ to install all the pre-requisites.

.. _petlib: https://github.com/gdanezis/petlib
.. _`these instructions`: https://github.com/gdanezis/petlib#pre-requisites


Install
-------

If you have `pip` installed, you can install **Coconut** with the following command:

.. code-block:: none
   
   pip install bls-lib


otherwise, you can build it manually as below:

.. code-block:: none

    git clone https://github.com/asonnino/bls
    cd bls
    pip install -e .


Test
----

Tests can be run as follows:

.. code-block:: none

	pytest -v --cov=bls tests/

or simply using tox:

.. code-block:: none

	tox


BLS Modules
-----------
.. automodule:: bls

.. automodule:: bls.scheme

.. autofunction:: bls.scheme.setup()

.. autofunction:: bls.scheme.ttp_keygen(params, t, n)

.. autofunction:: bls.scheme.aggregate_vk(params, vk, threshold=True)

.. autofunction:: bls.scheme.sign(params, sk, m)

.. autofunction:: bls.scheme.aggregate_sigma(params, sigs, threshold=True)

.. autofunction:: bls.scheme.verify(params, aggr_vk, sigma, m)


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


License
==================
`The BSD license`_ 

.. _`The BSD license`: https://opensource.org/licenses/BSD-3-Clause
