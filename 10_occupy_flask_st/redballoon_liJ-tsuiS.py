# Red Balloon - Johnson Li Simon Tsui
# SoftDev1 pd8
# K10 -- Jinja Tuning ...
# 2018-09-22

from flask import Flask, render_template
import random
import csv

def convert(filename):
    '''converts a two column csv file with table headers and footers into a key value pair dictionary'''
    #open file and parse it into a generator using csv reader
    #convert the generator into a list exluding the job and percentage table headers and footers
    #read values two at a time as tuples and use those to create a key value pair
    dict = {key:float(value) for key,value in list(csv.reader(open(filename)))[1:-1]}
    return dict

def pickRandom(f):
    '''takes a dictionary of key value pairs and returns a random key using the values as the percent chance of selecting the corresponding key'''
    #pick a number, any number (as long as it's an element of [0,99.8))
    rand = random.uniform(0, 99.8)
    #go through key value pairs in dict
    for key,value in dict.items():
        rand -= value
        #when the cumulative total is greater than the random value, return that key
        if rand <= 0:
            return key
    return "unemployed"

def randOcc():
    dict = convert("occupations.csv")
    return "weighted random pick: " + pickRandom(f)

app = Flask(__name__)

@app.route("/occupations")
def occupations():
    dict = convert("occupations.csv")
    return render_template("template.html", randomOcc = randOcc(), d=dict)

app.debug = True
app.run()

if __name__ == "__main__":
    app.debug = True
    app.run()
