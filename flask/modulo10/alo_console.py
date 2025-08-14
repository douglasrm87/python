from flask import Flask

app = Flask("Alo Mundo")

def aloMundo():
		print ("Alo Mundo")

def loginAloMundo():
		print ("Login do alo mundo")

aloMundo()
loginAloMundo()