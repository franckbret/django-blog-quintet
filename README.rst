Django Blog Quintet
===================

This application is just an utility that extends django-blog-zinnia in order
to provide Html5 templates + css3 styling

I've also tried to implement some aria attributes and microformats.

Before all be sure to follow Zinnia installation steps.
http://django-blog-zinnia.com/docs/

Installation
------------
Basically you can just get the sources, copy the templates folder to your
project templates directory and make directly your changes.

You can also use Django Blog Quintet as an app.

Add 'blogquintet' to your installed apps.

Be sure to put 'blogquintet' __BEFORE__ 'zinnia' in order to have templates
inheritance.

Something like this : ::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.comments',
        'tagging',
        'mptt',
        'blogquintet',
        'zinnia',
    )

Media
------------
You can use BLOGQUINTET_MEDIA_URL in you settings to define url path.::

    BLOGQUINTET_MEDIA_URL = os.path.join(MEDIA_URL, 'blogquintet/')

Note that you need to add 'blogquintet.context_processors.media', context
processor for that.

For example ::

    TEMPLATE_CONTEXT_PROCESSORS = (
            'django.core.context_processors.auth',
            'django.core.context_processors.i18n',
            'django.core.context_processors.request',
            'django.core.context_processors.media',
            'django.contrib.messages.context_processors.messages',
            'zinnia.context_processors.media',
            'zinnia.context_processors.version', # Optional
            'blogquintet.context_processors.media',
    )

Now you can see it in action !

Make it your own
----------------
You'll probably want to customize some parts of the templates to integrate into
your project.

In your project templates directory make a 'zinnia' directory with your template.

Example extending base.html :
in yourproject/templates/zinnia/base.html::

    {% extends "zinnia/skeleton.html" %}
    {% load zinnia_tags tagging_tags %}
    {% block title-tag %}
    <title>
    The greastest blog of the wwworld - {% block title %}{% endblock %}
    </title>
    {% endblock title-tag %}
    
Thanks
------
Thanks to fantomas42 http://github.com/Fantomas42/django-blog-zinnia for this
great django blog app.

Don't hesitate to reports bugs, improvments and suggestion. You're welcome.

You can reach me at http://www.franckbret.com




