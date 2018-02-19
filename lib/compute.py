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
