from flask import Flask, url_for, render_template
from markupsafe import escape
import feedparser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/news")
def news(score):
    return render_template('grade.html')
    
@app.route("/about")
def about(score):
    return render_template('grade.html')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)