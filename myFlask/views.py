#====================================================================================
#from a_Model import ModelIt
from TweetModel import spitTweet
from TweetModel import isGood
#from .a_Model import ModelIt
from flask import render_template
from myFlask import app
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
    #pull 'tweet' from input field and store it
    user_tweet = request.args.get('tweet')
    spitTweet(user_tweet)
    the_result = isGood(user_tweet)
    if the_result[0]==0:
        output_res='Try another tweet, to increase favorability'
    else:
        output_res='Nice tweet! very likely to receive many likes.'
    accu=round(the_result[1],3)*100
    return render_template("output.html", the_result = output_res, the_accuracy=str(accu)+'%' )
