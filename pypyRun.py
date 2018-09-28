# coding=utf-8


#pypy启动方式
# import os
# os.chdir('/opt/Lucifer/')
import reloader
from celerycore.init import app

#python PyPyRun.py worker -c 3 --loglevel=info


def reload_stop_task():
    print('Reloading code end…')


if __name__ == "__main__":
    reloader.main(
        app.start,
        before_reload=lambda: reload_stop_task()
    )
    #app.start()