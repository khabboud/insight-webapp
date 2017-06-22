#Import the necessary methods from tweepy library
#from datetime import datetime, time, date
#import re
#import calendar
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.linear_model import LogisticRegression as LR
from scipy import sparse
import json
import pickle
#import tweepy
import pandas as pd
#import sqlite3
import os
import json
import sys
import numpy as np
#from tweepy import OAuthHandler,AppAuthHandler
#import matplotlib.pyplot as plt
import re 

def CleanURL(twt):
    twt = re.sub(r"http\S+|\@\S+|t.co\S+|\d+", "",twt)
    return twt

def isGood(user_input  = 'Default'):
    if user_input != 'Default':
        pkl_file = open('modelsCompareWeek4.pkl', 'rb')
        data1 = pickle.load(pkl_file)
        pkl_file.close()
        vectorizer=data1['featureMap']
        SVM_model=data1['SVM_model']
        NB_model=data1['NB_model']
        LR_model=data1['LR_model']
        X_test=data1['testing data']
        X_train=data1['training data']
        y_train=data1['train labels']
        y_test=data1['test labels']          
        user_input=CleanURL(user_input)
        analyzer = SentimentIntensityAnalyzer()
        n=X_train.shape[1]
        sentiment_input=analyzer.polarity_scores(user_input)['compound']
        input_vectorized = vectorizer.transform([user_input])
        input_feature=np.ones(n)
        input_feature[0:-1]=input_vectorized.toarray()
        input_feature[n-1]=sentiment_input
        input_feature_sprc=sparse.csr_matrix(np.matrix(input_feature))
        modelAccuracy=LR_model.score(X_test,y_test)
        return LR_model.predict(input_feature_sprc)[0], LR_model.predict_proba(input_feature_sprc)[0][1], modelAccuracy
    else:
        return 'check your input!'

def spitTweet(fromUser  = 'Default'):
    if fromUser != 'Default':
        print('your tweet is: ',fromUser)
        return 
    else:
        return 'check your input!'