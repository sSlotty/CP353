from flask import Flask, url_for, render_template
from markupsafe import escape
import feedparser

app = Flask(__name__)

@app.route("/")
def index():
    name = "Thanathip"
    return render_template("home.html", name=name)

@app.route("/grade/<int:score>")
def grade(score):
    return render_template('grade.html', score=score)
    

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)