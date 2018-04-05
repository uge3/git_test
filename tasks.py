
from celery import Celery
import time
app = Celery('TASK',
	broker='redis://localhost',
	backend='redis://localhost')

@app.task
def add(x,y):
        print("running...运行第一个。。相加。",x,y)
        return x+y


@app.task
def miuse(x,y):
	#time.sleep(6)
        print("moise...运行第二个。。相减。",x,y)
        return x-y

