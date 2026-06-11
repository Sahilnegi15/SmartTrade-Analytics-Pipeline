from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import subprocess

def run_ingest():
    subprocess.run(["python", "/opt/airflow/scripts/ingest.py"], check=True)

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'stap_elt_pipeline',
    default_args=default_args,
    description='Daily ELT from S3 to dbt',
    schedule_interval='0 8 * * *',   # daily at 8 AM
    catchup=False,
) as dag:

    ingest = PythonOperator(
        task_id='ingest_data',
        python_callable=run_ingest
    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/dbt && dbt run'
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/dbt && dbt test'
    )

    ingest >> dbt_run >> dbt_test