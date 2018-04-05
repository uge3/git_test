
from __future__ import absolute_import, unicode_literals
from .celery import app
import time,random

@app.task
def randnum(x,y):
	#t=time()
	#t.sleep(3)
        return random.randint(x,y)


