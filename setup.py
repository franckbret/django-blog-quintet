#!/usr/bin/env python

from distutils.core import setup

setup(name='django-blog-quintet',
    version='0.1',
    description='Html5 blog templates for django blog zinnia',
    author='Franck BRET',
    author_email='franckbret@gmail.com',
    url='http://github.com/franckbret/django-blog-quintet/',
    packages=['blogquintet'],
    package_data={'blogquintet': [
        'templates/*.html',
        'templates/*/*.html',
        'templates/*/*/*.html',
        'templates/*/*/*/*.html',
        ]},
    classifiers = ['Development Status :: 1 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Django',
                   'Topic :: Templates',
                   'Topic :: Html5'
                   ],
     )