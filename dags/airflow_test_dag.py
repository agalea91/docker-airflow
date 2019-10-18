# -*- coding: utf-8 -*-
"""
airflow_page_monitor.py

Test Airflow pipeline for Page Monitor app.

Author: Alex Galea
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import os
import datetime
import sys

project_home = os.getenv('PROJECT_HOME', '/app')
sys.path.append(project_home)

if len(sys.argv) > 1:
    scrape_folder = sys.argv[1]
else:
    scrape_folder = None

from page_monitor.config import Config
config = Config()

# Page monitor DAG for botify extract

botify_page_monitor_dag = DAG(
    'test_page_monitor',
    default_args=config.AIRFLOW_DEFAULT_ARGS,
    schedule_interval=config.MONITOR_FREQ,
    catchup=config.CATCHUP,
)

# Step 1: extract from botify

sleep_task = BashOperator(
    task_id='sleep_task',
    bash_command='{{ params.python_path }} {{ params.file_path }}',
    params={
        'python_path': config.PYTHON_PATH,
        'file_path': os.path.join(project_home, 'sleep_5_seconds.py'),
    },
    dag=botify_page_monitor_dag
)

# Step 2: process for errors

file_task_bash_command = (
    '{{ params.python_path }} {{ params.file_path }}'
)
file_task = BashOperator(
    task_id='file_task',
    bash_command=file_task_bash_command,
    params={
        'python_path': config.PYTHON_PATH,
        'file_path': os.path.join(project_home, 'make_file.py'),
    },
    dag=botify_page_monitor_dag
)


# Set DAG dependencies

sleep_task >> file_task

