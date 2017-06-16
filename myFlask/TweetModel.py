#Import the necessary methods from tweepy library
#from datetime import datetime, time, date
#import re
#import calendar
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.linear_model import LogisticRegression as LR
import json
import pickle
import pandas as pd
import os
import json
import sys
import numpy as np
import requests
#from tweepy import OAuthHandler,AppAuthHandler
#import matplotlib.pyplot as plt

def isGood(user_input  = 'Default'):
    if user_input != 'Default':
        # pkl_file = open('../static/modelMVP.pkl', 'rb')
        # data1 = pickle.load(pkl_file)
        # pkl_file.close()
        with open('/tmp/modelMVP.pkl', 'wb') as f:
            r = requests.get('https://github.com/khabboud/insight-webapp/raw/master/myFlask/modelMVP.pkl', stream=True)
            for chunk in r:
                f.write(chunk)
        with open('/tmp/modelMVP.pkl', 'rb') as f:
            data1 = pkl.load(f)
        model=data1['model']
        vectorizer=data1['featureMap']
        modelAccuracy=data1['Test_accuracy']
        YRaw=data1['labels']
        xRaw=data1['training data']
        test_x_point = vectorizer.transform([user_input])
        return model.predict(test_x_point)[0], modelAccuracy
    else:
        return 'check your input!'

def spitTweet(fromUser  = 'Default'):
    if fromUser != 'Default':
        print('your tweet is: ',fromUser)
        return 
    else:
        return 'check your input!'
