from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return "Welcome to the Daily Nutrition"

@app.route("/hi/")
def who():
    return "Who are you ?"

@app.route("/hi/<username>")
def great(username):
    return f"Hi there {username}"


app.run()
