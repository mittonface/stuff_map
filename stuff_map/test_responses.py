from django.test import TestCase
from django.test.client import Client
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage


class ResponseTestCases(TestCase):

    def setUp(self):
        self.c = Client()



