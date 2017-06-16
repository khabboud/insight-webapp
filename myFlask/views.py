#====================================================================================
#from a_Model import ModelIt
from TweetModel import spitTweet
from TweetModel import isGood
#from .a_Model import ModelIt
from flask import render_template
from myFlask import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd

from flask import request



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )




@app.route('/input')
def cesareans_input():
    return render_template("input.html")

@app.route('/output')
def output():
    #pull 'birth_month' from input field and store it
    user_tweet = request.args.get('birth_month')
    #just select the Cesareans  from the birth dtabase for the month that the user inputs
    #query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
    #print query
    #query_results=pd.read_sql_query(query,con)
    #print query_results
    #births = []
    #for i in range(0,query_results.shape[0]):
     #   births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
    spitTweet(user_tweet)
    the_result = isGood(user_tweet)
    if the_result[0]==0:
        output_res='Try another tweet, to increase favorability'
    else:
        output_res='Nice tweet! very likely to receive many likes.'
    accu=round(the_result[1],3)*100
    return render_template("output.html", the_result = output_res, the_accuracy=str(accu)+'%' )