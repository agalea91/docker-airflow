# -*- coding: utf-8 -*-
"""
app.config

Configuration options for testing app

Author: Alex Galea
"""
import os
import datetime

dotenv_path = os.path.join(os.getenv('PROJECT_HOME', './'), '.credentials', '.env')
if not os.path.isfile(dotenv_path):
    DOTENV_WARNING = (
        'WARNING: No `.env` file found. '
        '\n * Check that required environment variables have been added (see README file). '
    )
else:
    DOTENV_WARNING = ''
from dotenv import load_dotenv
load_dotenv(dotenv_path=dotenv_path)





class Config:
    NOTIFY_SUMMARY_FREQ = datetime.timedelta(days=1) # every day
    MONITOR_FREQ = datetime.timedelta(seconds=60) # every 2 hours
    AIRFLOW_DEFAULT_ARGS = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': '2019-01-01', # datetime.datetime.utcnow(),
        'email': ['alexg@ayima.com'],
        'email_on_failure': True,
        'email_on_retry': True,
        'retries': 1,
        'retry_delay': datetime.timedelta(seconds=15),
    }
    PYTHON_PATH='python'
    CATCHUP = False





