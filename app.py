from flask import Flask , render_template,request
import os

app = Flask(__name__, template_folder='templates/')

@app.route('/')
def index():
    return  "done"


if __name__ == "__main__":

    app.run()
