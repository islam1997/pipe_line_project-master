# Data_pipeline_project

# Introduction

Dans le cadre de notre projet pour le module **Data Pipeline** nous avons réalisé une étude portant sur des données politiques en vue des élections présidentielles 2022.

Ce projet est divisé en trois parties:

- Collecte des données.
- Traitement des données.
- Orchestration et automatisation du Data Pipeline.

# Première partie collecte des données

Le but de cette partie est alimenter le pipeline de données en inputs.

Cette partie est composé en trois étapes:

- Web scrapping on utilisant le langage python avec la bibliothéque 'flask_restful' et l'API de twitter 'tweepy'

- Extraction d'un dataset portant sur les élections de 2022

- Transformations des données vers Kafka en utilisant l'outil apache nifi


Etapes 1 & 2:
Nous avons utilisé la bibliothéque `flask_restful` consommant l'API `tweepy` ayant pour rôle de scraper les données à partir de twitter.

Ci dessous une illustration de notre scraping.

![image1](https://github.com/islam1997/Data_pipeline_project/blob/main/Capture/scaping.png)

Etape 3:
Cette API joue le rôle d'intermédiaire entre twitter et `Nifi` , notre gestionnaire de flux de données.

Le script de l'API est disponible sous le répertoire *"/data"*.

Le premier process group `condidats_groupe` consomme l'API twitter créé précédemment pour chaque candidat des élections.

Le deuxième process group `election`concerne un dataset portant sur les élections présidentielles de 2022.

Ci dessous quelques illustrations des schémas réalisé avec `Nifi`.

Pour chaque électeur, une requête `GET` sera envoyée vers l'API de twitter.

Nous procédons par la suite à l'extraction des informations les plus pertinentes via chaque data.

Les données seront regroupés dans un ficher `CSV` qui sera envoyé vers un topic `Kafka`.


## 2eme partie Traitement des données (mise en forme, nettoyage..)

Une fois les données collectées, nous avons procédés à la création d'un dataset regroupant les outputs de nos différents batchs pour créer un fichier final pour chaque candidat.

Nous avons effectués plusieurs opérations moyennant principalement `Pyspark` sur les données collectés via twitter et ceux des élections présidentielles de 2017 tel que:

- Suppression des doublons.
- Traitement des symboles.
- Traitement des dates.
- Ajout de colonnes (Feature Engineering).
- Calcul d'agrégats.




##  3eme partie Orchestrer et  automatiser notre Data Pipeline.

Pour orchestrer et automatiser notre data pipeline, nous avons utilisés le DAGs (code_automation_airflow.py) :
- avant d'executer notre code , il faut lancer notre airflow webserver a l'aide dela commande : airflow webserver -p 8080 :
![Run Airflow Webserver](https://github.com/anasdaghai98/airflow/blob/main/airflow%20webserver.JPG)

apres que on a executé notre code et acceder a notre UI airflow , il nous a afficher un probleme de scheduler not run : 
![Error Scheduler](https://github.com/anasdaghai98/airflow/blob/main/before%20run%20scheduler.JPG)

pour regler ce probleme on a executer la commande airflow scheduler dans notre terminal : 
![Probleme resolu](https://github.com/anasdaghai98/airflow/blob/main/after%20run%20scheduler.JPG)

tout est bien maintenent , on peut executer notre dag sans probleme !
comme vous voyer ci dessous : Airflow UI , notre dag qui s'appelle anas est en mode on :

![Dags nommé (anas) is on ](https://github.com/anasdaghai98/airflow/blob/main/dags%20on.JPG)

en cliquent sur notre dag >> graph >> vous voyer ici notre tasks : 
![Process tasks ](https://github.com/anasdaghai98/airflow/blob/main/4tasks.JPG)

comme vous voyer dans l'image notre process commence par start puis il execute notre premier script , apres il execute notre deuxieme script, 
et a la fin le processus end qui indique que c'est le dernier process qui sera executer dans notre dag
et pour voir si notre code s'execute chaque 5 second , on cliquent sur schedule en haut de la page , il nous affiche cette liste d'execution , 
comme vous voyer ci dessous dans la date d'execution , chaque 5 sec il execute notre code :

![Scheduler executed succesfully](https://github.com/anasdaghai98/airflow/blob/main/each%205%20sec%20succesfully.JPG)

et si notre code est executer et que il y'a pas d'erreur , on vas verifier notre fichier log , 
comme vous voyer dans le fichier log , le code est executer par succes  et  effectue les traitements nécessaires !
![Notre fichier Log ](https://github.com/anasdaghai98/airflow/blob/main/log%20file.JPG)

