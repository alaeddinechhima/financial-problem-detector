#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd



def load_data(path):
    df=pd.read_excel(path,header=0)
    return df

def balance_test(df):
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    summ=df["Solde au 31/12/2016"].sum(axis=0)
    if(int(summ)==0):
        response="Your balance is equlibre go deeper and check GL"
    else :
        response="Stop please check your balance it is not equal to 0"
    return response

def balance_gl_test(df_bal,df_gl):
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    print(list(df_bal))
    for index, row in df_bal.iterrows():
        df_temp=df_gl.loc[df_gl['ID'] == row["N COMPTE"]]
        summ=df_temp["Solde"].sum(axis=0)
        summ=float("{0:.3f}".format(summ))
        summ1=float("{0:.3f}".format(row["Solde au 31/12/2016"]))
        if(summ!=summ1)  :
            response="Oh! Be careful you have a problem in compte "+ str(row["N COMPTE"])
            return response
    response="every thing is OK you can go further"
    return response
