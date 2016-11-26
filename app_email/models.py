from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, Group
from sorl.thumbnail import get_thumbnail
from django.template.defaultfilters import slugify
import datetime
from django.template import loader
from django.utils import timezone
from datetime import timedelta
from django.db.models import Prefetch
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_init, pre_init, post_save
import math
from django.core.urlresolvers import reverse
from django.conf import settings
from decimal import Decimal
from emailer.settings import *
from urlparse import urlparse
from django.core.files import File
from amazon.api import AmazonAPI
import bottlenose.api
import urllib
import requests, json

