#Box2 - Anton Danylenko, Simon Tsui
#SoftDev1 pd8
#K15 -- Do I know you?
#2018-10-03

import os
from flask import Flask
from flask import session
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import make_response
from flask import flash

login_info = {"addis": "ababa"}
usr_input = {}
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def start():
    #if ((session["usrname"] == "addis") and (session["pswrd"] == "ababa")):
        #return render_template("auth.html", a = session["usrname"])
    #else:
    return render_template("login.html")

@app.route("/logout")
def back():
    session.pop("usrname")
    session.pop("pswrd")
    return redirect(url_for("start"))


@app.route("/auth", methods = ['GET'])
def authenticate():
    #print(url_for('authenticate'))
    session["usrname"] = request.args["Username"]
    session["pswrd"] = request.args["Password"]
    if (session["usrname"] == 'addis' and session["pswrd"] == 'ababa'):
        return redirect(url_for("success"))
    else:
        return redirect(url_for('display_login'))

@app.route("/again")
def display_login():
    if(session["usrname"] != "addis" and session["pswrd"] != "ababa"):
        flash("Username and Password invalid!")
        return render_template("failed.html", a  = "Username and Password ")
    elif(session["usrname"] != "addis"):
        flash("Username invalid!")
        return render_template("failed.html", a = "Username")
    else:
        flash("Password invalid!")
        return render_template("failed.html", a = "Password")

@app.route("/display_login")
def success():
    #print(request.args)
    # return render_template("auth.html", a = request.args['Username'])
    return render_template("auth.html", a = session["usrname"])


if __name__ == "__main__":
    app.debug = True
    app.run()
