#!/usr/bin/python3
"""Module to initialize routers and endpoints"""

# IMPORT DEPENDENCIES
import pytz
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler

from api.database import SQLALCHEMY_DATABASE_URL

# DEFINE INSTANCES
jobstores = {'default': SQLAlchemyJobStore(
    url=SQLALCHEMY_DATABASE_URL or 'sqlite:///./asset_store.db')}
executors = {'default': ThreadPoolExecutor(
    20), 'processpool': ProcessPoolExecutor(5)}
job_defaults = {'coalesce': False, 'max_instances': 3}

# DEFINE JOB SCHEDULER
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors,
                                job_defaults=job_defaults, timezone=pytz.utc, misfire_grace_time=60)
