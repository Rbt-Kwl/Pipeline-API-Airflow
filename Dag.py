


from airflow.operators.weekday import BranchDayOfWeekOperator
from airflow.operators.bash import BashOperator
from airflow.models import DAG
from datetime import timedelta, datetime



default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2022,10,31),
        'retries': 3,
        'retry_delay': timedelta(minutes=20)

}



dag = DAG(
    dag_id='Real_crypto_dag',
    schedule_interval='41 17 */1 * *',
    catchup=False,
    default_args=default_args
)


with dag:
    run_script = BashOperator(
        task_id='Trending_and_allMarkets',
        bash_command='python3 "/Users/kowalrobert/Desktop/Python/Gecko/db.py"',
    )





