from flask import Flask
from flask import request
from flask import render_template
import urllib
import json

app = Flask(__name__)
@app.route("/")
def start():


    #World Population API
    base_url = "http://api.population.io:80/1.0/"

    enter = urllib.request.urlopen("http://api.population.io:80/1.0/countries")

    display = enter.read()

    # print (display)
    data=json.loads(display)


    enter = urllib.request.urlopen(base_url+"population/United%20States/2018-01-01/")
    display1=enter.read()
    #print(display1)
    pop_data = json.loads(display1)


    #Advice Slip API
    url =  	"https://api.adviceslip.com/advice"
    enter = urllib.request.urlopen(url)
    m = enter.read()
    advice_data = json.loads(m)


    #cat facts api
    enter = urllib.request.urlopen("https://catfact.ninja/fact")
    cat = enter.read()
    cat_data = json.loads(cat)

    return render_template("index.html",
    country=data["countries"][223],
    date = pop_data['total_population']['date'],
    pop = pop_data['total_population']['population'],
    thing = advice_data["slip"]["advice"],
    cats = cat_data["fact"])



if __name__ == "__main__":
    app.debug = True
    app.run()
