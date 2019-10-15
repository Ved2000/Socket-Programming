# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:07:56 2019

@author: cr712
"""

import time, socket, sys, pickle
#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/cr712/Documents/train.tsv',sep = '\t')
num_train = len(df)



def Punctuation(string): 
  
    # punctuation marks 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
    # traverse the given string and if any punctuation 
    # marks occur replace it with null 
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "") 
  
    # Print string without punctuation 
    return string




def final(S): #S is a string
    S = S.lower()
    S = Punctuation(S)
    S1 = S.split()
    unique = list(set(S1))
    ret = dict.fromkeys(saved_dict, 0)
    ret['misc'] = 0
    for word in unique:
        if word in ret.keys():
            ret[word] = S1.count(word)
        else:
            ret['misc'] += 1
    ret = list(ret.values())
    return ret







def sentiment(string):
    test = string
    test = np.array(final(test))
    test = test.reshape((-1,1))
    temp1 = saved_model.predict(test.T)
    temp1
    rating = 1 + temp1.argmax()
    return_dict = {}
    return_dict['5.Very GooD'] = round(temp1[0][4]*100,2)
    return_dict['4.GooD '] = round(temp1[0][3]*100)
    return_dict['3.Neutral'] = round(temp1[0][2]*100)
    return_dict['2.Bad '] = round(temp1[0][1]*100)
    return_dict['1.Very Bad '] = round(temp1[0][0]*100)
    print("The rating of this review is" , rating )
    print("percentage wise distribution is :")
    return return_dict


with open('C:/Users/cr712/Documents/newdict_pickle.pkl','rb') as pickle_file2:
 saved_dict = pickle.load(pickle_file2)





with open('C:/Users/cr712/Documents/model_pick.pkl','rb') as pickle_file:
 saved_model = pickle.load(pickle_file)














print('Client Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 9999
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')
while True:
   message = soc.recv(1024)
   message = message.decode()
   print(server_name, ">", message)
   message = input(str("Me > "))
   sentiment('message')
   if message == "[bye]":
      message = "I'm leaving the chat room -_-"
      soc.send(message.encode())
      print("\n")
      break
   soc.send(message.encode())