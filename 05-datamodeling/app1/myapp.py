from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# config Flask app  ให้ใช้งาน database ชนิดไหน
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #กำหนด ชื่อ database เช่น test.db
db = SQLAlchemy(app)

# สร้าง ต้นแบบของข้อมูลว่าต้องมีค่าอะไรบ้าง
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)




if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
