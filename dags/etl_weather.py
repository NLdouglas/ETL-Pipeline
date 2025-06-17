from airflow import DAG
from airflow.providers.https.hook.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago

#latitude and longitude of the city
LATITUDE = 30.0368
LONGITUDE = 51.2090
POSTGRES_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

#DAG

with DAG(dag_id='weather_etl_pipeline',
        default_args=default_args,
        schedule_interval='@daily',
        catchup=False,) as dags:
    
    
    #Extracts weather data from Open-Meteo API using AirFlow Connetion
    @task()
    def extract_weather_data():
        # Use HTTP Hook to get connection details from Airflow
        http_hook=HttpHook(http_conn_id=API_CONN_ID,method='GET')

        ##Build the API endpoint
        # https://api.open-meteo.com/v1/forecast?latitude=30.0368&longitude=51.2090&current_weather=true  
        endpoint = f'/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'

        # Make the request via http hook 
        response = http_hook.run(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"failed to fetch weather data: {response.status.code}")


    #transform the extracted weather data.
    @task()
    def transform_weather_data(weather_data) :
        current_weather = weather_data['current_weather']
        transform_data = {
            
        }


    