from flask import Flask
from flask import render_template, redirect, url_for
from flask import Response, request, jsonify
app = Flask(__name__)

#routes
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True)
