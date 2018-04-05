from __future__ import absolute_import, unicode_literals #绝对路径导入
from celery import Celery

app = Celery('proj',
	broker='redis://localhost',#
	backend='redis://localhost',
	include=['celery_pro.tasks',
		'celery_pro.tasks2',
		'celery_pro.periodic_tasks'])#包含多个文件

app.conf.update(#实例化后可更新
	result_expires=3600,#任务何存时间
)
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'celery_pro.tasks.add',
        'schedule': 4.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'

if __name__=='__main__':
	app.start()

