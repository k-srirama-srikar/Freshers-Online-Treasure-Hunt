from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import json
import os


app = Flask(__name__)
app.secret_key = "e7193bbd8a4ab1dc8bf29c8de5024e4ab10269d9c3cc59bf475f1486e811c6fd5996a0a0873ddb63b07b"

users = ["weasley@1223414432", "dumbledore@1761837661", "lovegood@1846657233", "granger@280282620", "riddle@-931195728", "malfoy@1081489288"]

@app.route("/")
def hello_world():
    return render_template("page.html")

@app.route("/f54ba756f6fd5a33ff943ed53c979235518b")
def welcome_to_r2():
    return render_template("answer.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    c2 = False
    ans2 = ""

    user_id = request.form['user_id']
    pwd = request.form['pwd']

    if request.method == "POST":
        if user_id in users:
        # pwd = request.form['pwd']
            session['user_id'] = user_id
            if pwd == "https://www.youtube.com/watch?v=jtaqHzUhYdw":
                c2 = True
                ans2 = "first link"
                return welcome_to_r2()
            else:
                # return render_template("page.html", c1=c2, ans2=ans2)
                return render_template('page.html', user_id=session.get('user_id'), c1=c2, ans2=ans2)
        else:
            return render_template("page.html")
    return render_template("page.html", c1=c2, ans2=ans2)
