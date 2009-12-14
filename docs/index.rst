Welcome to django-osr's documentation!
======================================

.. toctree::
   :maxdepth: 2

Django-osr, where osr is a accronyme for Online Streaming Record, is a
web application built with the `Django framework`_ . It's main task
is scheduling online stream recording and record them for the user.
It use Streamripper_ to download the stream.

Look at the docs directory for more detail.

Dependency
----------

* Python
* Django_ 1.0+
* Streamripper_

Installation
------------

First, copy the osr directory in you django site and add the app to the
list of apps in your *settings.py* configuration file.

Also, you must configure in your *settings.py* file the absolute path where the
streams will be downloaded and the url to the directory like that::

  # Dont' forget the trailing slashs
  OSR_DIR = '/var/django/osr_site/media/audio/'
  OSR_URL = '/media/audio/'


To access the osr stream listing, you must add this urlconf to your *urls.py*
file like that::

  (r'^',include('osr.urls')),

To be able to view the listing and the detail view of the recording,
be sure to have a minimal *base.html* file in the *templates* directory.
If your not sure, take a look at the `Django documentation`_. Here's a
example of a *base.html* file::

  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
  <html>
  <head>
  <title>{% block title %}The title will be here{% endblock %}</title>
  </head>
  <body>

  {% block content %}
    The content will be here.
  {% endblock %}
  
  </body>
  </html>


Finally, you need to add a cron job to trigger the start/end of the streams. In
Linux, you can usally do it with the command::

  crontab -e

and a a line like that::

  # m    h   dom mon dow   command
  0-55/5 *    *   *   *    python /var/django/osr_site/manage.py osr_check

To run the command every 5 minutes.

Limitation
----------

Right now, only the following streaming formats are supported:

* mp3
* ogg
* nsv
* aac


.. _Streamripper: http://streamripper.sourceforge.net
.. _Django:
.. _`Django framework`: http://www.djangoproject.com
.. _`Django documentation`: http://docs.djangoproject.com


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

