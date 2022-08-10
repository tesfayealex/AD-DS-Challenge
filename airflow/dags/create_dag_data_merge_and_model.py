from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import logging
import json
import os
import pandas as pd
log: logging.log = logging.getLogger("airflow")
log.setLevel(logging.INFO)

default_args={
    'owner':'tesfaye',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='merger_dag',
    default_args=default_args,
    description='merge_and_model_dataset',
    start_date=datetime(2022,8,7,2),
    schedule_interval='@once'
)as dag:
    task1 = PostgresOperator(
        task_id='merge_different_datasets',
        postgres_conn_id='postgres_connection',
        sql='/sql/merge_different_datasets.sql',
    )
    task1 