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
DAG_NAME='demo_dag'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2019, 10, 14, 9, 58, 00),
    'concurrency': 1,
    'catchup':True,
    'retries': 0,
    'tenant_id':'tename_id',
    'tenant_name':'tenant_name',
    'service_id':'service_id',
    'service_name':'service_name',
    'id':'id',
    'workflow_definition_id':'workflow_definition_id'
}

def task_1(**context):
    log.info("Generatting CID")
    time.sleep(1)
    log.info("Completed Generating CID")

def task_2(**context):
    log.info("OnBoarding new Tenant")
    time.sleep(10)
    log.info("Completed OnBoarding new Tenant")

def task_3(**context):
    log.info("Add Tenant to GLC")
    time.sleep(10)
    log.info("Completed adding Tenant to GLC")

def task_4(**context):
    log.info("Provision GPC")
    time.sleep(10)
    log.info("Completed provisioning GPC")

def task_5(**context):
    log.info("Assign RDA")
    time.sleep(10)
    log.info("Completed RDA")

def task_6(**context):
    log.info("Add opsramp and logzio")
    time.sleep(10)
    log.info("Completed opsramp and logzio")

def task_7(**context):
    time.sleep(10)

def task_8(**context):
    time.sleep(10)

def task_9(**context):
    time.sleep(10)

def task_10(**context):
    time.sleep(10)

'''
This DAG represents Customer OnBoarding process flow.
'''
with DAG(DAG_NAME,
         catchup=False,
         default_args=default_args,
         schedule_interval=None,
         ) as demo_workflow:
    step1 = PythonOperator(task_id='task_1', python_callable=task_1,provide_context=True)
    step2 = PythonOperator(task_id='task_2', python_callable=task_2, provide_context=True)
    step3 = PythonOperator(task_id='task_3', python_callable=task_3, provide_context=True)
    step4 = PythonOperator(task_id='task_4', python_callable=task_4, provide_context=True)
    step5 = PythonOperator(task_id='task_5', python_callable=task_5, provide_context=True)
    step6 = PythonOperator(task_id='task_6', python_callable=task_6, provide_context=True)
    step7 = PythonOperator(task_id='task_7', python_callable=task_7, provide_context=True)
    step8 = PythonOperator(task_id='task_8', python_callable=task_8, provide_context=True)
    step9 = PythonOperator(task_id='task_9', python_callable=task_9, provide_context=True)
    step10 = PythonOperator(task_id='task_10', python_callable=task_10, provide_context=True)

step1 >> step2 >> step3 >> step4 >> step5 >> step6 >> step7 >> step8 >> step9 >> step10
