# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return render_template("page.html")


# @app.route("/check", methods=["GET", "POST"])
# def check():
#     c2 = False
#     ans2 = ""

#     if request.method == "POST":
#         pwd = request.form['pwd']
#         if pwd == "aurjaoobt":
#             c1 = True
#             ans1 = "first link"
#         else:
#             return render_template("page.html")
#     return render_template("page.html", c1=c2, ans2=ans2)



# if __name__ == '__main__':
#     app.run()





from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os


app = Flask(__name__)


DATA_FILE = 'user_data.json'

# Function to load data from the JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save data to the JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


@app.route("/")
def hello_world():
    return render_template("page.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    c2 = False
    ans2 = ""

    user_id = request.form['user_id']
    pwd = request.form['pwd']
    
    # Load existing data
    data = load_data()
    
    # Store the new input by user ID
    if user_id in data:
        data[user_id].append(pwd)
    else:
        data[user_id] = [pwd]
    
    # Save data to file
    save_data(data)
    
    # return jsonify({"message": "Data saved successfully!", "data": data})

    if request.method == "POST":
        pwd = request.form['pwd']
        if pwd == "aurjaoobt":
            c1 = True
            ans1 = "first link"
        else:
            return render_template("page.html")
    return render_template("page.html", c1=c2, ans2=ans2)
