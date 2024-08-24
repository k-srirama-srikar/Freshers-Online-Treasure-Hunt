from flask import Flask, render_template, request
from random import randint
import datetime
app = Flask(__name__)
gen=0
def wrongimage():
    global gen
    gen=randint(1,6)
    st=f"{gen}.mp4"
    return st
c=0

@app.route("/svvfhevhjbfjbwknjkbfw")
def hello_world():
    return render_template("page2.html")

@app.route("/check", methods=["GET", "POST"])
def check():
    global c
    c = 0
    pwd = request.form['pwd']
    c1=0
    current_time = datetime.datetime.now()
    if current_time >= datetime.datetime.combine(current_time.date(), datetime.time(11, 30)):
        c1=1
    if request.method == "POST":
        
        if pwd == "https://www.youtube.com/watch?v=jtaqHzUhYdw":
            return render_template("answer2.html",c=c,ind=wrongimage(),c1=c1)
        else:
            c=1
            return render_template('page2.html',c=c,ind=wrongimage(),c1=c1)
    return render_template("page2.html",c=c,ind=wrongimage(),c1=c1)


@app.route("/szhgjierbgojbdjbvjnvjr3", methods=["GET", "POST"])
def round3():
    return render_template('page3.html')

@app.route("/checkr3r3r3r3", methods=["GET", "POST"])
def checkr3():
    global c
    c = 0
    c1=0
    current_time = datetime.datetime.now()
    if current_time >= datetime.datetime.combine(current_time.date(), datetime.time(12, 30)):
        c1=1
    pwd = request.form['pwd']
    if request.method == "POST":
        if pwd == "janetaylor":
            return render_template('answer3.html',c=c,ind=wrongimage(),c1=c1)
        else:
            c = 1
            return render_template('page3.html',c=c,ind=wrongimage(),c1=c1)
    return render_template('page3.html',c=c,ind=wrongimage(),c1=c1)


@app.route("/jzhbcgfbbgxfjghsvbgjk", methods=["GET", "POST"])
def round4():
    return render_template('page4.html')

@app.route("/checkr4r4t4beruiherig", methods=["GET", "POST"])
def checkr4():
    global c
    c = 0
    c1=0
    current_time = datetime.datetime.now()
    if current_time >= datetime.datetime.combine(current_time.date(), datetime.time(1, 0)):
        c1=1
    pwd = request.form['pwd']
    if request.method == "POST":
        if pwd == "thalaforareason":
            return render_template('answer4.html',c=c,ind=wrongimage(),c1=c1)
        elif pwd=="cr7" or pwd=="cristianoronaldo":
            c=1
            return render_template('page4.html',c=c,ind="cr7.mp4",c1=c1)
        else:
            c = 1
            return render_template('page4.html', c=c ,ind=wrongimage(),c1=c1)
    return render_template("page4.html",c=c,ind=wrongimage(),c1=c1)

@app.route("/ikekwgnvaguvagunvrnuvhjgasrjhb", methods=["GET", "POST"])
def round5():
    return render_template('page5.html')

@app.route("/checkr5jerbgjsbjkdbjkdbjb", methods=["GET", "POST"])
def checkr5():
    global c
    c = 0
    c1=0
    current_time = datetime.datetime.now()
    if current_time >= datetime.datetime.combine(current_time.date(), datetime.time(1, 0)):
        c1=1
    pwd = request.form['pwd']
    if request.method == "POST":
        if pwd == "fiftythree":
            return render_template('answer5.html',c=c,ind=wrongimage(),c1=c1)
        else:
            c = 1
            return render_template('page5.html',c=c,ind=wrongimage(),c1=c1)
    return render_template("page5.html",c=c,ind=wrongimage(),c1=c1)

@app.route("/sdbvvjksbjkdgdzjkfbdrjfvhmn", methods=["GET", "POST"])
def round1():
    return render_template('page.html')

@app.route("/checkr1hhgsbgjkbkjzsgkn", methods=["GET", "POST"])
def checkr1():
    global c
    c = 0
    c1=0
    current_time = datetime.datetime.now()
    if current_time >= datetime.datetime.combine(current_time.date(), datetime.time(9, 30)):
        c1=1
    pwd = request.form['pwd']
    if request.method == "POST":
        if pwd == "aurjaoobt":
            return render_template('answer.html',c=c,ind=wrongimage(),c1=c1)
        else:
            c = 1
            return render_template('page.html',c=c,ind=wrongimage(),c1=c1)
    return render_template("page.html",c=c,ind=wrongimage(),c1=c1)

@app.route('/')
def home():
    return render_template('/rules.html')