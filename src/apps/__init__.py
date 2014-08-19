try: import simplejson as json
except: import json
from django.core import serializers
from django.db import models
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.views.decorators.csrf import csrf_protect

from src.apps.misc import *