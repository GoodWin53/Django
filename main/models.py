from django.db import models
from django.http import JsonResponse, HttpResponse
from django.contrib.sites import requests
from urllib import response
import json


class Countrys(models.Model):
    country=models.TextField('Страна')
    languages=models.TextField('Языки')

    def __str__(self):
        return self.country

