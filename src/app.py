import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload",methods=["POST"])
def upload():
    print request.files
    return 200

if __name__ == "__main__":
    app.run()
