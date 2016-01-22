import os
from flask import Flask, render_template, request,redirect
from util import Util,Data
from makecalendar import TexCalendar

app = Flask(__name__)
cal = None

@app.route("/")
def index():
    return render_template('index.html', months=Util.read_months('English'))

@app.route("/upload",methods=['GET','POST'])
def upload():
    global cal
    if Util.validate_data(request.form, request.files):
        data = Util.extract_form_data(request.form,request.files)
        cal = TexCalendar(data.year, data.images, data.lang)
    return render_template('calendar.html', data=data)

@app.route("/month/<int:num>")
def month(num):
    global cal
    cal.make_month(num)
    return ('',200)

@app.route("/stitch")
def stitch():
    global cal
    cal.stitch()
    return ('',200)

if __name__ == "__main__":
    app.debug=True
    app.run()
