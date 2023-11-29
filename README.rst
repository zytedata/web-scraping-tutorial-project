=============================
Web scraping tutorial project
=============================

Scrapy_ project built following `Zyte’s web scraping tutorial`_.

.. _Scrapy: https://scrapy.org/
.. _Zyte’s web scraping tutorial: https://docs.zyte.com/web-scraping/tutorial/index.html

.. note:: If you are looking for a template for a new Scrapy project
    pre-configured to make the most out of Zyte services, see
    `zyte-spider-templates-project`_ instead.

    .. _zyte-spider-templates-project: https://github.com/zytedata/zyte-spider-templates-project

Requirements
============

Python 3.8 or higher.


Setup
=====

To be able to use this project, you must first:

#.  Create a Python virtual environment.

    -   On **Windows**:

        .. code-block:: shell

            python3 -m venv tutorial-env
            tutorial-env\Scripts\activate.bat

    -   On **macOS** and **Linux**:

        .. code-block:: shell

            python3 -m venv tutorial-env
            . tutorial-env/bin/activate

#.  Install the project requirements:

    .. code-block:: shell

        pip install --upgrade -r requirements.txt

#.  To be able to deploy to `Scrapy Cloud`_, copy your `Scrapy Cloud API key`_,
    run ``shub login`` and, when prompted, paste your API key and press Enter.

    .. _Scrapy Cloud: https://docs.zyte.com/scrapy-cloud/get-started.html
    .. _Scrapy Cloud API key: https://app.zyte.com/o/settings/apikey

#.  To be able to use `Zyte API`_, append the following line to
    ``tutorial/settings.py``, replacing ``YOUR_API_KEY`` with your `Zyte API
    key`_:

    .. code-block:: python

        ZYTE_API_KEY = "YOUR_API_KEY"

    .. _Zyte API: https://docs.zyte.com/zyte-api/get-started.html
    .. _Zyte API key: https://app.zyte.com/o/zyte-api/api-access

    .. tip:: For local development, you can alternatively use an environment
        variable with that name. In Scrapy Cloud, the ``ZYTE_API_KEY`` setting
        will be automatically defined with your Zyte API key.
