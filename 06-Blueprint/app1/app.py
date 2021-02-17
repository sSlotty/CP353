from flask import Flask
from main import main
from auth import auth

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(auth)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)