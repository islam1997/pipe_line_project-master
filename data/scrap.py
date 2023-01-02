
# IMPORT
from flask import Flask
from flask_cors import CORS
# APP SETUP
app = Flask(__name__)
# enable resource sharing between frontend and server
CORS(app)

# ROUTES
# @app.route('/', methods=['GET'])
# def getHello():
# 	return 'This is a GET request!'

# if __name__ == "__main__":
#     app.run(debug=True)



# # IMPORT
# from flask import Flask
# from flask_cors import CORS
# # APP SETUP
# app = Flask(__name__)
# # enable resource sharing between frontend and server
# CORS(app)

import pandas as pd
from TwitterAPI import TwitterAPI
import os
import tweepy as tw
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import datetime
from tqdm import tqdm

from flask import Flask,request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json


# class tweeterApi(Resource):
#     def get (self):
#       args = request.args
#       search_words =args["candidat"]
#       tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(500)
#       list_of_tweets=[]
#       print("islam")
#       for item in tweets:
#         list_of_tweets.append(item._json)
#       print(len(list_of_tweets))
#       return list_of_tweets

app = Flask(__name__)
api_flask = Api(app)


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-proxy-server')
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")

sleep_on_rate_limit=False

consumer_key= 'jg0kH9QA20VKHlLOcosd7Vqcp'
consumer_secret= '3d9OfftAvdgvQYKJAYlkJwruQ3M3Hc77aexWP0IjCb5T0nYqFK'
access_token= '3293263684-9nUohBEDohlREGtWreeWBlyVS6STtjWLvMrgp2r'
access_token_secret= '1NmcBPb5Bj8aHK9Mcz8CR6gDjx0tefji8xYA7N8f7Pi4M'

print("ok")
auth = tw.OAuthHandler(consumer_key, consumer_secret)
print("ok")
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

@app.route('/zemmor', methods=['GET'])
def get_zemmour ():

    args = request.args
    search_words ="Eric Zemmour"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste

@app.route('/macron', methods=['GET'])
def get_macron ():

    args = request.args
    search_words ="Emmanuel Macron"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste
@app.route('/melenchon', methods=['GET'])
def get_melenchon ():

    args = request.args
    search_words ="Jean-Luc Mélenchon"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste
#api_flask.add_resource(tweeterApi, '/get_twitter')

@app.route('/arthaud', methods=['GET'])
def get_arthaud ():

    args = request.args
    search_words ="Nathalie Arthaud"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste

@app.route('/roussel', methods=['GET'])
def get_roussel ():

    args = request.args
    search_words ="Fabien Roussel"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste

@app.route('/lassalle', methods=['GET'])
def get_lassalle ():

    args = request.args
    search_words ="Jean Lassalle"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste


@app.route('/lepen', methods=['GET'])
def get_lepen ():

    args = request.args
    search_words =" Marine Le Pen "
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste

@app.route('/anne', methods=['GET'])
def get_anne ():

    args = request.args
    search_words ="Anne Hidalgo"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste

@app.route('/jadot', methods=['GET'])
def get_jadot ():

    args = request.args
    search_words ="Yannick Jadot"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste
@app.route('/pecresse', methods=['GET'])
def get_pecresse ():

    args = request.args
    search_words ="Valérie Pécresse"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste

@app.route('/poutou', methods=['GET'])
def get_poutou ():

    args = request.args
    search_words ="Philippe Poutou"
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="fr",tweet_mode="extended").items(100)
    list_of_tweets=[]
      #print("islam")
    for item in tweets:

        list_of_tweets.append(item._json)
    jsonStr = json.dumps(list_of_tweets)
    with open('/home/ece/Images/json_data.json', 'w') as outfile:
        outfile.write(jsonStr)
    new_liste=[]
    for i in range(len(list_of_tweets)):


        new_dict=dict()
        new_dict['created_at']=list_of_tweets[i]['created_at']
        new_dict['tweet_id']=list_of_tweets[i]['id']
        new_dict['user_name']=list_of_tweets[i]['user']['name']
        new_dict['text']=list_of_tweets[i]['full_text']
        new_dict['user_id']=list_of_tweets[i]['user']['id']
        new_dict['user_location']=list_of_tweets[i]['user']['location']
        new_liste.append(new_dict)
    
    #print(len(list_of_tweets))
    return new_liste



if __name__ == '__main__':
    app.run(debug=True)



    
