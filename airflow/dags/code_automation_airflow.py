from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from datetime import timedelta
import json
import findspark
findspark.init()
import pyspark
import random
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
import os
import pyspark.sql.functions as f
from pyspark.sql.functions import lit
import math
from pyspark.sql import Row
from pyspark.sql.functions import unix_timestamp, from_unixtime,substring
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType, IntegerType, DateType
import pyspark
import findspark
import findspark
findspark.init()
import pyspark
import random
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
import os
import pyspark.sql.functions as f
from pyspark.sql.functions import lit
import math
from pyspark.sql import Row
from pyspark.sql.functions import unix_timestamp, from_unixtime,substring
from datetime import datetime
from pyspark.sql import functions as F
import pandas
import os
import pandas as pd


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 3),
    'depends_on_past': False,
    'catchup': False,
    'retries': 10,
    'retry_delay': timedelta(seconds=5)
}
dag = DAG(
    'anas',
    default_args=default_args,
    schedule_interval=timedelta(seconds=5)
)



# Définissez la fonction Python que vous souhaitez exécuter
def mon_script_python():
    sc = pyspark.SparkContext('local')
    sc = SparkSession(sc)
    df_pyspark=sc.read.format("csv").option("header","true").load(r'/home/anasdaghai/Téléchargements/p2022-resultats-circonscriptions-t1.csv')
    df_pyspark.show()

    df_departement=df_pyspark.select('Département','Inscrits','Abstentions','Votants','Blancs','Nuls','Exprimés')
    sum_str=dict()

    for i in range(1,len(df_departement.columns)):
        sum_str[df_departement.columns[i]]='sum'
    

    #df_pyspark=sc.read.format("csv").option("header","true").load(r'/home/anasdaghai/Téléchargements/p2022-resultats-circonscriptions-t1.csv')
    #df_pyspark.show()



    df_departement_type=df_departement.withColumn('Inscrits', col('Inscrits').cast(IntegerType()))\
.withColumn('Abstentions', col('Abstentions').cast(IntegerType()))\
.withColumn('Votants', col('Votants').cast(IntegerType()))\
.withColumn('Blancs', col('Blancs').cast(IntegerType()))\
.withColumn('Nuls', col('Nuls').cast(IntegerType()))\
.withColumn('Exprimés', col('Exprimés').cast(IntegerType()))

    df_departement_finale=df_departement_type.groupBy("Département").agg(sum_str)

    df_departement_finale=df_departement_finale.withColumnRenamed("sum(Abstentions)", "Nombre d'abstentions")\
.withColumnRenamed("sum(Exprimés)", "Nombre de votes exprimés")\
.withColumnRenamed("sum(Blancs)", "Nombre de votes blancs")\
.withColumnRenamed("sum(Inscrits)", "Nombre d'inscrits")\
.withColumnRenamed("sum(Votants)", "Nombre de votants")\
.withColumnRenamed("sum(Nuls)", "Nombre de votes Nuls")

    df_departement_finale.toPandas().to_csv('/home/anasdaghai/Téléchargements/Resultats_par_département.csv',encoding='ISO-8859-1')

    df_condidats_nombre=df_pyspark.select('Département','ARTHAUD','ROUSSEL','MACRON','LASSALLE','LE PEN','ZEMMOUR','MÉLENCHON','HIDALGO','JADOT','PÉCRESSE','POUTOU','DUPONT-AIGNAN')

    sum_str=dict()

    for i in range(1,len(df_condidats_nombre.columns)):

        sum_str[df_condidats_nombre.columns[i]]='sum'

    df_condidats_nombre=df_condidats_nombre.withColumn('ARTHAUD', col('ARTHAUD').cast(IntegerType()))\
.withColumn('ROUSSEL', col('ROUSSEL').cast(IntegerType()))\
.withColumn('MACRON', col('MACRON').cast(IntegerType()))\
.withColumn('LE PEN', col('LE PEN').cast(IntegerType()))\
.withColumn('ZEMMOUR', col('ZEMMOUR').cast(IntegerType()))\
.withColumn('LASSALLE', col('LASSALLE').cast(IntegerType()))\
.withColumn('MÉLENCHON', col('MÉLENCHON').cast(IntegerType()))\
.withColumn('HIDALGO', col('HIDALGO').cast(IntegerType()))\
.withColumn('JADOT', col('JADOT').cast(IntegerType()))\
.withColumn('PÉCRESSE', col('PÉCRESSE').cast(IntegerType()))\
.withColumn('POUTOU', col('POUTOU').cast(IntegerType()))\
.withColumn('DUPONT-AIGNAN', col('DUPONT-AIGNAN').cast(IntegerType()))

    df_condidats_nombre=df_condidats_nombre.groupBy("Département").agg(sum_str)

    df_condidats_nombre=df_condidats_nombre.withColumnRenamed("sum(ARTHAUD)", "Nombre de vote pour ARTHAUD")\
.withColumnRenamed("sum(ROUSSEL)", "Nombre de vote pour ROUSSEL")\
.withColumnRenamed("sum(MACRON)", "Nombre de vote pour MACRON")\
.withColumnRenamed("sum(LE PEN)", "Nombre de vote pour LE PEN")\
.withColumnRenamed("sum(ZEMMOUR)", "Nombre de vote pour ZEMMOUR")\
.withColumnRenamed("sum(MÉLENCHON)", "Nombre de vote pour MÉLENCHON")\
.withColumnRenamed("sum(HIDALGO)", "Nombre de vote pour HIDALGO")\
.withColumnRenamed("sum(JADOT)", "Nombre de vote pour JADOT")\
.withColumnRenamed("sum(PÉCRESSE)", "Nombre de vote pour PÉCRESSE")\
.withColumnRenamed("sum(POUTOU)", "Nombre de vote pour POUTOU")\
.withColumnRenamed("sum(DUPONT-AIGNAN)", "Nombre de vote pour DUPONT-AIGNAN")\
.withColumnRenamed("sum(LASSALLE)", "Nombre de vote pour LASSALLE")

    df_condidats_nombre.show()


    df_condidats_nombre.toPandas().to_csv('/home/anasdaghai/Téléchargements/Resultats_condidats.csv',encoding='ISO-8859-1')
    

# Instanciez la tâche en utilisant la fonction Python définie ci-dessus
tache1 = PythonOperator(
    task_id='execute_code_each_5sec',
    python_callable=mon_script_python,
    dag=dag
)


def mon_code_2():


    list_folder=["Anne_Hidalgo","Jean_Lassalle","Nathalie_Arthaud","Valérie_Pécresse","Emmanuel_Macron","Jean-luc_Mélenchon","Poutou","Yannick_Jadot","Eric_Zemmour","Marine_le_pen","Poutou"]



    def union_all(dfs):


        if len(dfs) > 1:

           return dfs[0].unionAll(union_all(dfs[1:]))
        else:

            return dfs[0]    
    sc = pyspark.SparkContext('local')

    sc = SparkSession(sc)

    for name_folder in list_folder:


        liste=[]
        repertoire='/home/anasdaghai/Téléchargements/condidats_2022/condidats_2022/'+name_folder
        for filename in os.listdir(repertoire):

           f= os.path.join(repertoire,filename)
           liste.append(sc.read.format("csv").option("sep", ",").option("multiline",True).option("header","true").option('encoding','ISO-8859-1').load(f))
        finale_df = union_all([liste[i] for i in range(len(liste))])
        finale_df = finale_df.dropDuplicates(finale_df.columns)
        finale_df=finale_df.na.fill('Adresse Privé',['user_location'])
        finale_df=finale_df.na.fill('Inconnu',['user_name'])
    
        finale_df  = finale_df.na.drop(subset=["text"])
        finale_df = finale_df.withColumn('text', pyspark.sql.functions.regexp_replace(pyspark.sql.functions.col("text"), r'[^A-Za-z0-9\s]+', ""))
        finale_df = finale_df.withColumn('user_name', pyspark.sql.functions.regexp_replace(pyspark.sql.functions.col("user_name"), r'[^A-Za-z0-9\s]+', ""))
        finale_df = finale_df.withColumn('user_location', pyspark.sql.functions.regexp_replace(pyspark.sql.functions.col("user_location"), r'[^A-Za-z0-9\s]+', ""))
        finale_df.toPandas().to_csv('/home/anasdaghai/Téléchargements/condidats_2022/condidats_2022/'+name_folder+'.csv',encoding='ISO-8859-1')

start = DummyOperator(task_id='start',dag=dag) 
end = DummyOperator(task_id='end',dag=dag)
tache2 = PythonOperator(
    task_id='execute_code_2',
    python_callable=mon_code_2,
    dag=dag
)


start >> tache1 >> tache2 >> end





