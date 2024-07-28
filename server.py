from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.before_request
def redirect_to_non_www():
    if request.host.startswith('www.'):
        return redirect('https://' + request.host[4:] + request.path, code=301)

# Routes
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/aboutme')
def aboutme():
    return render_template('AboutMe.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug=True)
