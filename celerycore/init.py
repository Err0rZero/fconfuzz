# coding=utf-8
from __future__ import absolute_import
from celery import Celery


app = Celery('fuzz', include=['fuzzRun'])

app.config_from_object('celerycore.configs')
#init(app,"postgresql://safe_dba:SS3edc4rfv@rm-p2u0ur53gw668wt0j.pg.rds.aliyuncs.com:3433/riskdb","safe_dba","SS3edc4rfv")


if __name__ == '__main__':
    app.start()


