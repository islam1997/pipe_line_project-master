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

import os
import pandas as pd

list_folder=["Anne_Hidalgo","Jean_Lassalle","Nathalie_Arthaud","Valérie_Pécresse","Emmanuel_Macron",
"Jean-luc_Mélenchon","Poutou","Yannick_Jadot","Eric_Zemmour","Marine_le_pen","Poutou"]



def union_all(dfs):
    if len(dfs) > 1:
        return dfs[0].unionAll(union_all(dfs[1:]))
    else:
        return dfs[0]    

sc = pyspark.SparkContext('local')
sc = SparkSession(sc)
for name_folder in list_folder:
    liste=[]
    repertoire='/home/ece/condidats_2022/'+name_folder
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
    finale_df.toPandas().to_csv('/home/ece/condidats_2022/'+name_folder+'.csv',encoding='ISO-8859-1')
    
    
   
    
    







    
    
    
    