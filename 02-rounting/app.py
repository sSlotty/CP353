from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username*5))

if __name__ == '__main__':
    app.run(use_reloader=True)