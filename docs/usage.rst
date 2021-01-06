=====
Usage
=====

To use proposals-core in a project, add it to your `INSTALLED_APPS`:

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
