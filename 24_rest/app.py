from flask import Flask
from flask import request
from flask import render_template
import urllib
import json

app = Flask(__name__)
@app.route("/")
def start():
    enter = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=Btf1nFd88IvnSzme84ebBWYRhveHfNqYhhRYyYtU&date=2018-04-15")
    display = enter.read()
    print (display)
    data=json.loads(display)
    return render_template("index.html", pic=data['url'], explanation = data['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()
