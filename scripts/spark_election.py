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
from datetime import datetime
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType, IntegerType, DateType


from pyspark.sql import functions as F
import pandas
sc = pyspark.SparkContext('local')
sc = SparkSession(sc)

df_pyspark=sc.read.format("csv").option("header","true").load(r'C:/Users/islam/Pictures/p2022-resultats-circonscriptions-t1.csv')
df_pyspark.show()

df_departement=df_pyspark.select('Département','Inscrits','Abstentions','Votants','Blancs','Nuls','Exprimés')
sum_str=dict()

for i in range(1,len(df_departement.columns)):
    sum_str[df_departement.columns[i]]='sum'

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

df_departement_finale.toPandas().to_csv('C:/Users/islam/Pictures/Resultats_par_département.csv',encoding='ISO-8859-1')

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


df_condidats_nombre.toPandas().to_csv('C:/Users/islam/Pictures/Resultats_condidats.csv',encoding='ISO-8859-1')
    