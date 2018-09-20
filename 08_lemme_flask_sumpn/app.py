'''Simon Tsui
   SoftDev1 pd8
   K08 -- Fill Yer Flask
   2018-09-20R'''



from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")  #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)
    return "No hablo queso! <a href = /food> Click me! </a> "

@app.route("/food")
def food():
    return """
    <table border = 5><tr>
    <td>Cake</td>
    <td>Ice Cream Cake</td>
    <td>Ice Cream</td>
    </tr></tr>
    <td>Steak</td>
    <td>Shrimp</td>
    <td>Salad</td>
    <a href = /others> Click me again! </a>
    """

@app.route("/others")
def things():
    return"""
    Computer Science Classes:
    <ul>
    <li>Computer Graphics</li>
    <li>Systems Level Programming</li>
    <li> Software Development</li>
    <li> Artificical Intelligence </li>
    </ul>
    <a href = /> Click me one last time </a>
    """

if __name__ == "__main__":
    app.debug = True
    app.run()
