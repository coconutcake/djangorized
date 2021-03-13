from django.test import TestCase
import unittest
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.views import *
import datetime
from rest_framework import status
from core.additionals.functions import *


class AdditionalFunctionsCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_current_time_instance(self):
        """ Testuje czy fukcja zwraca clase datetime z dzisiejsza datą"""
        current = get_current_time()
        now = datetime.datetime.now()
        self.assertTrue(isinstance(current,datetime.datetime))
        self.assertTrue(current.date,now.date)
        
    def test_yesterday_date_instance(self):
        """ Sprawdza czy zwracany jest dzien poprzedni """
        now = datetime.datetime.now()
        yesterday = now - datetime.timedelta(days=1)
        instance = get_yesterday_date()
        self.assertTrue(yesterday.date,instance)