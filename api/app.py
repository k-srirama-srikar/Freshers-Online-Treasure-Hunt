from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from random import randint
app = Flask(__name__)
gen=0
def wrongimage():
    global gen
    gen=randint(1,6)
    st=f"{gen}.mp4"
    return st

@app.route("/svvfhevhjbfjbwknjkbfw")
def hello_world():
    return render_template("page2.html")

@app.route("/check", methods=["GET", "POST"])
def check():
    c = "False"
    

    pwd = request.form['pwd']

    if request.method == "POST":
        
        if pwd == "https://www.youtube.com/watch?v=jtaqHzUhYdw":
            return render_template("answer2.html",c=c,ind=wrongimage())
        else:
            c="True"
            return render_template('page2.html',c=c,ind=wrongimage())
    return render_template("page2.html",c=c,ind=wrongimage())


@app.route("/szhgjierbgojbdjbvjnvjr3", methods=["GET", "POST"])
def round3():
    return render_template('page3.html')

@app.route("/checkr3r3r3r3", methods=["GET", "POST"])
def checkr3():
    c = "False"

    pwd = request.form['pwd']

    if request.method == "POST":
        if pwd == "janetaylor":
            return render_template('answer3.html',c=c,ind=wrongimage())
        else:
            c = "True"
            return render_template('page3.html',c=c)
    return render_template("page3.html",c=c,ind=wrongimage())


@app.route("/jzhbcgfbbgxfjghsvbgjk", methods=["GET", "POST"])
def round4():
    return render_template('page4.html')

@app.route("/checkr4r4t4beruiherig", methods=["GET", "POST"])
def checkr4():
    c = "False"
    pwd = request.form['pwd']
    if request.method == "POST":
        if pwd == "thalaforareason":
            return render_template('answer4.html',c=c,ind=wrongimage())
        else:
            c = "True"
            return render_template('page4.html',c=c,ind=wrongimage())
    return render_template("page4.html",c=c,ind=wrongimage())

@app.route("/ikekwgnvaguvagunvrnuvhjgasrjhb", methods=["GET", "POST"])
def round5():
    return render_template('page5.html')

@app.route("/checkr5jerbgjsbjkdbjkdbjb", methods=["GET", "POST"])
def checkr5():
    c = "False"
    pwd = request.form['pwd']
    if request.method == "POST":
        if pwd == "fiftythree":
            return render_template('answer5.html',c=c,ind=wrongimage())
        else:
            c = "True"
            return render_template('page5.html',c=c,ind=wrongimage())
    return render_template("page5.html",c=c,ind=wrongimage())

@app.route("/sdbvvjksbjkdgdzjkfbdrjfvhmn", methods=["GET", "POST"])
def round1():
    return render_template('page.html')

@app.route("/checkr1hhgsbgjkbkjzsgkn", methods=["GET", "POST"])
def checkr1():
    c = "False"
    pwd = request.form['pwd']
    if request.method == "POST":
        if pwd == "aurjaoobt":
            c = "True"
            return render_template('answer.html',c=c,ind=wrongimage())
        else:
            return render_template('page.html',c=c,ind=wrongimage())
    return render_template("page1.html",c=c,ind=wrongimage())

@app.route('/')
def home():
    return render_template('/rules.html')