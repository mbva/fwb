import string
import random
import datetime
import json
import requests

import itertools

from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from django.db.models import (
    Count,
    Sum,
    Case,
    When,
    Value,
    IntegerField,
)
from portal.models import *




def home(request):
    return render_to_response("index.html")
