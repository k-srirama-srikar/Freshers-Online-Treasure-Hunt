from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("page.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    c2 = False
    ans2 = ""

    if request.method == "POST":
        pwd = request.form['pwd']
        if pwd == "aurjaoobt":
            c1 = True
            ans1 = "first link"
        else:
            return render_template("page.html")
    return render_template("page.html", c1=c2, ans2=ans2)



if __name__ == '__main__':
    app.run()
