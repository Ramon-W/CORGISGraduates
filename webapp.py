from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/Data-For-Majors")
def render_page1():
    return render_template('page1.html')

if __name__=="__main__":
    app.run(debug=True)
