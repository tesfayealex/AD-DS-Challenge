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

def format_design_json_data(location , destination_location):
    log.info(os. getcwd())
    with open(location) as f:
        data = json.load(f)
    columns = ['game_key' , 'labels','text','colors','videos_data','eng_type','direction','adunit_sizes']
    new_json_data = {}
    for j in data:
        for rows in data[j]:
            new_json_data[f'{j}/{rows}'] = data[j][rows]
    new_df = pd.DataFrame(new_json_data).T
    new_df.index.name='game_key'
    new_df.to_csv(destination_location)



with DAG(
    dag_id='load_ad_data',
    default_args=default_args,
    description='extract and load raw data from the given datasets',
    start_date=datetime(2022,8,7,2),
    schedule_interval='@once'
)as dag:
    task1 = PythonOperator(
       task_id='format_design_json_dataset',
       python_callable=format_design_json_data,
       op_kwargs={'location': 'data/global_design_data.json' , 'destination_location': 'data/structured_design_data.csv'},
    )
    task2 = PostgresOperator(
        task_id='create_raw_briefing_table',
        postgres_conn_id='postgres_connection',
        sql='/sql/create_raw_briefing_table.sql',
    )
    task3 = PostgresOperator(
        task_id='create_raw_campaigns_inventory_table',
        postgres_conn_id='postgres_connection',
        sql='/sql/create_raw_campaigns_inventory_table.sql',
    )
    task4 = PostgresOperator(
        task_id='create_raw_design_data_table',
        postgres_conn_id='postgres_connection',
        sql='/sql/create_raw_design_data_table.sql',
    )
    task5 = PostgresOperator(
        task_id='load_briefing_data',
        postgres_conn_id='postgres_connection',
        sql='/sql/load_raw_briefing_data.sql',
    )
    task6 = PostgresOperator(
        task_id='load_campaigns_inventory_data',
        postgres_conn_id='postgres_connection',
        sql='/sql/load_raw_campaigns_inventory_data .sql',
    )
    task7 = PostgresOperator(
        task_id='load_design_data',
        postgres_conn_id='postgres_connection',
        sql='/sql/load_raw_design_data.sql',
    )
    task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7