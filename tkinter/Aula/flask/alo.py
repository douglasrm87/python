from flask import Flask
app = Flask ("AloMundo")
#http://127.0.0.1:5000/
@app.route("/")
def aloMundo ():
    return ("<div align=\"center\"> <h1>Alo Mundo</h1></div>")
#http://127.0.0.1:5000/
@app.route("/login")
def login ():
    return "<h1>Vamos realizar seu login. </h1>"
print ("oi")