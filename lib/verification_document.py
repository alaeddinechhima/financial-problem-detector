import numpy as np
import pandas as pd


def verif(df):
    ok=df.isnull().values.any()
    if(ok):
        response="Your document is invalid there are empty cases"
    else :
        response="Your document is OK, you can go further into tests"
    return response    
