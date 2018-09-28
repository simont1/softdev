#Simon Tsui
#SoftDev1 pd8
#K13 -- Echo Echo Echo
#2018-09-28


from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/") #root route
def run():
    print(app)
    print(request.headers) #gives information about requester's browser etc...
    print(request.method)
    return render_template("basic.html")

@app.route("/auth")
def authenticate():
    print(request.args)
    print(request.form)
    return render_template("basic2.html", a = request.args["Username"])
    return request.args["Username"]
    #The keys in the args disctionary are the name values of the input tag

app.debug = True
app.run()
