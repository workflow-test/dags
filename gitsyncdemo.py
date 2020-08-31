import airflow
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
import logging
import json
import time
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
DAG_NAME='git_sync_dag'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2019, 10, 14, 9, 58, 00),
    'concurrency': 1,
    'catchup':True,
    'retries': 0,
    'id':'id'
}

def task_1(**context):
    log.info("Generatting CID")
    time.sleep(60)
    log.info("Completed Generating CID")

def task_2(**context):
    log.info("OnBoarding new Tenant")
    time.sleep(10)
    log.info("Completed OnBoarding new Tenant")


'''
This DAG represents Customer OnBoarding process flow.
'''
with DAG(DAG_NAME,
         catchup=True,
         default_args=default_args,
         schedule_interval=None,
         ) as demo_workflow:
    step1 = PythonOperator(task_id='task_1', python_callable=task_1,executor_config={
            "KubernetesExecutor": {"request_cpu": "100m",
                                   "request_memory": "256Mi",
                                   "limit_memory": "256Mi"}}, provide_context=True)
    step2 = PythonOperator(task_id='task_2', python_callable=task_2, executor_config={
            "KubernetesExecutor": {"request_cpu": "100m",
                                   "request_memory": "256Mi",
                                   "limit_memory": "256Mi"}}, provide_context=True)
  
step1 >> step2
