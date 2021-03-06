#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'fklosowski'
SITENAME = u'blog'
SITEURL = 'https://geofix.github.io/'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'pl'

DEFAULT_DATE_FORMAT = '%d.%m.%Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Javad GNSS', 'https://www.javad.com/jgnss/index.html'),
#         ('Javad PL', 'http://www.geoida.pl/javad/'),
#	('Geoida', 'http://www.geoida.pl'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/fklosowski'),
          ('Twitter', 'https://twitter.com/geofixed'),)

DEFAULT_PAGINATION = 10
#TWITTER_USERNAME = 'geofixed'

#MENUITEMS = (('Github', 'https://github.com/fklosowski'),
#          ('Twitter', 'https://twitter.com/geofixed'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican_themes/pelican-blue'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

