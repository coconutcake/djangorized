from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .celery import app

@shared_task
def printHello():
    print("Hello")
    return "Hello"

@app.task(name="sum_two_numbers")
def add(x, y):
    return x + y