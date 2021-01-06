=============================
proposals-core
=============================

.. image:: https://badge.fury.io/py/dj-proposals-candidates.svg
    :target: https://badge.fury.io/py/dj-proposals-candidates

.. image:: https://travis-ci.org/lfalvarez/dj-proposals-candidates.svg?branch=master
    :target: https://travis-ci.org/lfalvarez/dj-proposals-candidates

.. image:: https://codecov.io/gh/lfalvarez/dj-proposals-candidates/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/lfalvarez/dj-proposals-candidates

Modelos de propuestas y candidaturas

Documentation
-------------

The full documentation is at https://dj-proposals-candidates.readthedocs.io.

Quickstart
----------

Install proposals-core::

    pip install dj-proposals-candidates

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_proposals_candidates.apps.DjProposalsCandidatesConfig',
        ...
    )

Add proposals-core's URL patterns:

.. code-block:: python

    from dj_proposals_candidates import urls as dj_proposals_candidates_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_proposals_candidates_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
