# Importación de librerias
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Definimos default_args para los argumentos relacionados con correo y reintentos
default_args = {
    "email": ["orlando.mbaa@gmail.com"],
    "email_on_failure": True,   # Enviar correo si falla el DAG
    "email_on_retry": False,    # No enviar correo en caso de reintento
    "email_on_success": False,  # Configura en True si deseas notificación en caso de éxito
} # IMPORATNTE: Estos parámetros tienen que ir dentro del diccionario, no pueden ir directamente en la función DAG

# Inicializamos el DAG con default_args
dag = DAG(
    dag_id="Mlops_pipeline", # nombre del DAG
    default_args=default_args,
    start_date=datetime(year=2024, month=11, day=4),
    schedule_interval="0 15 * * *", # Lo definimos con un fromato cron
    catchup=True,
    tags=['Tec de monterrey']  # Integramos un Tag al DAG
)

# 2) Primera tarea: Inicio de la instancia
start_instance = BashOperator(
    task_id='start_workbench_instance', # ID del task
    bash_command='gcloud workbench instances start instance-20241016-074208 --location=us-west1-a',
    dag=dag)

# 3) Segunda tarea: Conexion y ejecucion del pipeline
# Segunda tarea: Conexion y ejecucion del pipeline
execution = BashOperator(
    task_id='execution',
    bash_command=(
        'gcloud compute ssh instance-20241016-074208 --zone=us-west1-a ' # Conexión via SSH a la VM de vertex 
        '--command="sudo -i bash -c \'' # --command="..." usa comillas dobles para definir todo el comando que se pasará al SSH
        # Entreamos como super usuario 
        'cd /home/jupyter/main/machine-learning-operations/mlops/src/mlops/pipelines && ' # Nos dirigimos a la direccion donde están los pipelines
        'kedro run \'"' # Ejecutamos todos los pipelines
    ),
    retries=2,
    dag=dag
)


# Orden de ejeuccion (secuencial)
start_instance >> execution