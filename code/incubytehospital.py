# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:45:37 2021

@author: Rohit
"""

import pandas as pd
import cx_Oracle
con=cx_Oracle.connect('system/rohit1234@127.0.0.1/XE')
if con!=None:
    print(con.version)
    print("connect done")
else:
    print("not done")

cur=con.cursor()

query2 = "select * from patients"

cur.execute(query2)


table_rows = cur.fetchall()
df = pd.read_sql('SELECT * FROM patients', con=con) 
df.set_index(['CUST_ID'], inplace=True)  
print (df)
ans = df.loc[df['COUNTRY'] == "IND"]


def show_data(country):
    data = df.loc[df['COUNTRY'] == country]
    print(data)


def get_file(country):
    data = df.loc[df['COUNTRY'] == country]
    file_name = str(country)
    data.to_csv('E:\python/' + file_name + ".csv")  
    print("File has been created to the specified path")



show_data("NYC")
get_file("NYC")



