# -*- coding: utf-8 -*-
"""
Local settings file
"""
# Local imports
# Third-party imports
{% if cookiecutter.use_mongodb == "y" %}
import pymongo
{% endif %}{% if cookiecutter.use_redisdb == "y" %}
from redis import StrictRedis
{% endif %}

# Local imports
from base import *


{% if cookiecutter.use_mongodb == "y" %}
MONGO_DB = pymongo.MongoClient('localhost')
{% endif %}{% if cookiecutter.use_redisdb == "y" %}
REDIS_DB = StrictRedis('localhost')
{% endif %}
