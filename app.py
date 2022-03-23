from flask import Flask, request

app = Flask(__name__)

@app.get("/welcome")
def welcome():

    return "<html><h1>welcome</h1></html>"

@app.get("/welcome/home")
def welcome_home():

    return "<html><h1>welcome home</h1></html>"

@app.get("/welcome/back")
def welcome_back():

    return "<html><h1>welcome back</h1></html>"

