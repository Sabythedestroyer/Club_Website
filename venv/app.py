from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

#This is main route to the home/index directory

@app.route('/')
@app.route('/index')
def main():
    return render_template('Index.html')

# This is the about route for the about directory page

@app.route('/about')
def about_club():
    return render_template('about.html')

if __name__ == ' __main__':
    app.run()
