import os
from flask import Flask, render_template, request,redirect
from werkzeug import secure_filename
from util import Util,Data
from makecalendar import TexCalendar

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload",methods=['GET','POST'])
def upload():
    if Util.validate_data(request.form, request.files):
        data = Util.extract_form_data(request.form,request.files)
        TexCalendar(data.year, data.images).make_pdf()
    return redirect("/",200)

if __name__ == "__main__":
    app.debug=True
    app.run()
