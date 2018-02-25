import numpy as np
import pandas as pd


def verif(df):
    ok=df.isnull().values.any()
    if(ok):
        response="Your document is invalid there are empty cases"
    else :
        response="Your document is OK, you can go further into tests"
    return response

def verif_compte(df_bal,df_gl):
    response=""
    for index, row in df_bal.iterrows():
        df_temp=df_gl.loc[df_gl['ID'] == row["N COMPTE"]]
        if(df_temp.empty):
            response="Be careful your GL did not mention compte num "+str(row["N COMPTE"])
            return response ;
