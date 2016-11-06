from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/home")
def firstpage():
    return render_template("profile.html")

@app.route("/background")
def secondpage():
    return render_template("background.html")

@app.route("/pathophysiology")
def thirdpage():
    return render_template("pathophysiology.html")

@app.route("/clinical")
def fourthpage():
    return render_template("clinical.html")

@app.route("/research")
def fifthpage():
    return render_template("research.html")

if __name__ == "__main__":
    app.run()