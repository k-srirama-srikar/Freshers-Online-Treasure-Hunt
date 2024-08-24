from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)

@app.route("/svvfhevhjbfjbwknjkbfw")
def hello_world():
    return render_template("page2.html")

@app.route("/f54ba756f6fd5a33ff943ed53c979235518b")
def welcome_to_r2():
    return render_template("answer2.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    c2 = False
    ans2 = ""

    pwd = request.form['pwd']

    if request.method == "POST":
        
        # pwd = request.form['pwd']
        if pwd == "https://www.youtube.com/watch?v=jtaqHzUhYdw":
            c2 = True
            ans2 = "first link"
            return welcome_to_r2()
        else:
            # return render_template("page.html", c1=c2, ans2=ans2)
            return render_template('page2.html', user_id=session.get('user_id'), c1=c2, ans2=ans2)
    return render_template("page2.html", c1=c2, ans2=ans2)


@app.route("/szhgjierbgojbdjbvjnvjr3", methods=["GET", "POST"])
def round3():
    return render_template('page3.html')

@app.route("/checkr3r3r3r3", methods=["GET", "POST"])
def checkr3():
    c3 = False
    ans3 = ""

    pwd = request.form['pwd']

    if request.method == "POST":
        
        # pwd = request.form['pwd']
        if pwd == "janetaylor":
            c3 = True
            ans3 = "first link"
            return render_template('answer3.html')
        else:
            return render_template('page3.html', user_id=session.get('user_id'), c3=c3, ans3=ans3)
    return render_template("page3.html", c3=c3, ans3=ans3)


@app.route("/jzhbcgfbbgxfjghsvbgjk", methods=["GET", "POST"])
def round4():
    return render_template('page4.html')

@app.route("/checkr4r4t4beruiherig", methods=["GET", "POST"])
def checkr4():
    c4 = False
    ans4 = ""
    pwd = request.form['pwd']

    if request.method == "POST":
        
        # pwd = request.form['pwd']
        if pwd == "thalaforareason":
            c4 = True
            ans4 = "first link"
            return render_template('answer4.html')
        else:
            return render_template('page4.html', user_id=session.get('user_id'), c4=c4, ans4=ans4)
    return render_template("page4.html", c4=c4, ans4=ans4)

@app.route("/ikekwgnvaguvagunvrnuvhjgasrjhb", methods=["GET", "POST"])
def round5():
    return render_template('page5.html')

@app.route("/checkr5jerbgjsbjkdbjkdbjb", methods=["GET", "POST"])
def checkr5():
    c5 = False
    ans5 = ""
    pwd = request.form['pwd']

    if request.method == "POST":
        
        # pwd = request.form['pwd']
        if pwd == "fiftythree":
            c5 = True
            ans5 = "first link"
            return render_template('answer5.html')
        else:
            return render_template('page5.html', user_id=session.get('user_id'), c5=c5, ans5=ans5)
    return render_template("page5.html", c5=c5, ans5=ans5)

@app.route("/sdbvvjksbjkdgdzjkfbdrjfvhmn", methods=["GET", "POST"])
def round1():
    return render_template('page.html')

@app.route("/checkr1hhgsbgjkbkjzsgkn", methods=["GET", "POST"])
def checkr1():
    c1 = False
    ans1 = ""
    pwd = request.form['pwd']

    if request.method == "POST":
        
        # pwd = request.form['pwd']
        if pwd == "aurjaoobt":
            c1 = True
            ans1 = "first link"
            return render_template('answer.html')
        else:
            return render_template('page.html',  c1=c1, ans1=ans1)
    return render_template("page1.html", c1=c1, ans1=ans1)

@app.route('/')
def home():
    return render_template('/rules.html')