from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pygsheets
import time
import pyautogui as pg
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import MWETokenizer

data_path = 'C:/Users/23794/Downloads/NEWS.xlsx'
data = pd.read_excel(data_path, sheet_name = 0)
date_headline = data.iloc[:, [0, 1]]

for i in range(len(data)):
    try:
        timefor = time.mktime(time.strptime(date_headline['Date'][i],"%d-%b-%Y %H:%MAM"))
    except:
        timefor = time.mktime(time.strptime(date_headline['Date'][i],"%d-%b-%Y %H:%MPM"))
    timefor_local = time.localtime(timefor)
    final = time.strftime("%Y-%m-%d", timefor_local)
    date_headline['Date'][i] = final

date_headline.sort_values('Date', inplace=True)
date_headline.drop_duplicates(inplace=True)
headline = pd.DataFrame(data.iloc[:, 1])
headline_count = headline.value_counts()
date_headline['frequency'] = 1
for j in range(len(date_headline)):
    for k in range(len(headline_count)):
        if date_headline.iloc[j,1] == str(headline_count.index[k][0]):
            date_headline.iloc[j,2] = str(headline_count.values[k])


date_headline = date_headline.reset_index(drop=True)
date_headline_final = date_headline
tokenizer = MWETokenizer()
word_list = []
for i in range(len(date_headline)):
    a = ''
    for j in str(date_headline.iloc[i,1]):
        a += str(j)
    tokens = tokenizer.tokenize(nltk.word_tokenize(a))
    word_list.append(tokens)

duplicated_list = []
for j in range(len(date_headline)):
    token_orginal = tokenizer.tokenize(nltk.word_tokenize(date_headline_final.iloc[j,1]))
    for k in range(j, len(word_list)):
        count = 0
        for l in token_orginal:
            if l in word_list[k]:
                count += 1
        if count > int(len(token_orginal) * 0.7) and j != k:
            duplicated_list.append(k)
            date_headline.loc[j]['frequency'] = int(date_headline_final.loc[j]['frequency']) + int(date_headline_final.loc[k]['frequency'])

duplicated_list_dup = list(set(duplicated_list))
date_headline = date_headline.drop(labels=duplicated_list_dup)

token = pygsheets.authorize(service_file='************')
DashBoard = token.open('PR Article Brand Mention Count')
News = DashBoard[4]
News.clear()

date = list(date_headline.iloc[:, 0])
title = list(date_headline.iloc[:, 1])
frequency = list(date_headline.iloc[:, 2])
News.update_col(1, date, row_offset=0)
News.update_col(2, title, row_offset=0)
News.update_col(3, frequency, row_offset=0)
