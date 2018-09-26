# Red Balloon - Johnson Li Simon Tsui
# SoftDev1 pd8
# K10 -- Jinja Tuning ...
# 2018-09-22

from flask import Flask, render_template
from util import occupations

app = Flask(__name__)

# route for occupation
@app.route("/occupations")
def runOcc():
    occupationDict = occupations.convert("data/occupations.csv")
    return render_template("template.html", randomOcc=occupations.randOcc(), d=occupationDict)


app.debug = True
app.run()

if __name__ == "__main__":
    app.debug = True
    app.run()
