from flask import Flask
app = Flask ("__name__")

#http://127.0.0.1:5000/

@app.route("/")
def aloMundo ():
	return ("<div align=\"center\"> <h1>Alo Mundo</h1></div>")

#http://127.0.0.1:5000/login

@app.route("/login")
def login ():
	return "<h1>Vamos realizar seu login. </h1>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
    print ("oi")