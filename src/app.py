import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    months=('January','February','March','April','May','June',\
        'July','August','September','October','November','December')
    return render_template('index.html',months=months)

@app.route("/upload",methods=['GET','POST'])
def upload():
    print request.form
    print request.files
    return render_template('index.html')

if __name__ == "__main__":
    app.debug=True
    app.run()
