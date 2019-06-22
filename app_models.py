from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WRON'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/blog_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = SQLAlchemy(app)
mysql = MySQL(app)
manage = Manager(app)

# @app.route('/')
# def hello_world():
# 	return render_template('index.html')

# from apps.users import users
# from apps.center import center
#
# app.register_blueprint(users, url_prefix='/')
# app.register_blueprint(center, url_prefix='/center')

@manage.command
def create_db():
	'''说明文件写在此处'''
	from models import db
	db.create_all()
	print('数据表创建完成')

if __name__ == '__main__':
	manage.run()
