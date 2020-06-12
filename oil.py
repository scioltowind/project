# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:59:25 2020

@author: Liang



"""
import os
import pandas as pd
import requests




def lineNotefy(token, msg):
    
    url = "https://notify-api.line.me/api/notify"
    
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    
    r = requests.post(url, headers = headers, params = payload)
    print(r.status_code)
    return 



ReadData = pd.read_html('https://www2.moeaboe.gov.tw/oil102/oil2017/A01/A0108/tablesprices.asp')[0]
GetOilNewdate = ReadData.loc[1][6][0:10]
#print(getoilnewdate)

GetOilData = ReadData.drop(ReadData[[4, 5, 6]], axis = 1)
#print(getoildata)
GetOilData = GetOilData[0:3]
#print(read_data.loc[1:2][0:5])
#print(getoildata)
token = "QIK74QAvXEGEQ9Ip2LCYEqDpdlq4xlaGtWjtx2eAsji"
msg1 = "最新油價報告：%s \n" %GetOilNewdate
msg2 = "**中油家油價** \n92無鉛汽油：%s \n95無鉛汽油：%s \n98無鉛汽油：%s  \n" %(GetOilData.loc[2][3], GetOilData.loc[2][2], GetOilData.loc[2][1])
msg3 = "===楚  河   漢 界===\n"
msg4 = "**台塑家油價** \n92無鉛汽油：%s \n95無鉛汽油：%s \n98無鉛汽油：%s  \n" %(GetOilData.loc[1][3], GetOilData.loc[1][2], GetOilData.loc[1][1])
msg = msg1 + msg2 + msg3 + msg4
print(msg)

lineNotefy(token, msg)
