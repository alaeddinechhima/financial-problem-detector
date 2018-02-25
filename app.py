from flask import Flask , render_template,request
import pandas as pd
from lib.compute import load_data, balance_test,balance_gl_test
from lib.verification_document import verif,verif_compte
import os

app = Flask(__name__, template_folder='templates/')
df_gl=load_data("ressources/GL-2016.xlsx")
print("data GL loaded")
df_bal=load_data("ressources/Bal-2016.xlsx")
print("data Bal loaded")

@app.route('/')
def index():
    return  "Welcome to our verification tool"

@app.route('/pre-test')
def pre_test():
    response1=verif(df_gl)
    response2=verif_compte(df_bal,df_gl)
    response=response1+"\n"+response2
    return  response

@app.route('/test-balance')
def test_balance():
    response=balance_test(df_bal)
    return  response

@app.route('/test-balance-gl')
def test_balance_gl():
    response=balance_gl_test(df_bal,df_gl)
    return  response


if __name__ == "__main__":

    app.run()
