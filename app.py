from flask import Flask , render_template,request
import pandas as pd
from lib.compute import load_data, balance_test
from lib.verification_document import verif
import os

app = Flask(__name__, template_folder='templates/')

@app.route('/')
def index():
    return  "Welcome to our verification tool"

@app.route('/pre-test')
def pre_test():
    df=load_data("ressources/GL-2016.xlsx")
    print("data loaded")
    response=verif(df)
    return  response

@app.route('/test-balance')
def test_balance():
    df=load_data("ressources/Bal-2016.xlsx")
    print("data loaded")
    response=balance_test(df)
    return  response


if __name__ == "__main__":

    app.run()
