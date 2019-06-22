from datetime import datetime

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WRON'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/blog_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)

# @manager.command
# def create_db():
# 	'''说明文件写在此处'''
# 	from models import db
# 	db.create_all()
# 	print('数据表创建完成')

manager.add_command('db',MigrateCommand) #添加db 命令（runserver的用法）

class Articles(db.Model):
	__tablename__ = 'articles'		# 自定义数据表名称，如不设置默认设置为类名
	id = db.Column(db.Integer, primary_key=True)   # 主键
	title = db.Column(db.String(80))   # 唯一键
	content = db.Column(db.String(80))
	add_time = db.Column(db.DateTime, default=datetime.now)
	# def __repr__(self):
	#     return '<User %r>' % self.username


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True)
	password = db.Column(db.String(100))
	nickname = db.Column(db.String(20), unique=True)
	email = db.Column(db.String(30), unique=True)
	address = db.Column(db.String(100))
	status = db.Column(db.Boolean, default=True)  # T为正常
	login_num = db.Column(db.Integer, default=0)
	last_login_time = db.Column(db.DateTime, default=datetime.now)
	last_login_ip = db.Column(db.String(15), default='0.0.0.0')
	is_delete = db.Column(db.Boolean, default=False)
	add_time = db.Column(db.DateTime, default=datetime.now)
	def __repr__(self):
		return '<User> %s' % self.username
'''
python models.py db init 创建数据表
python models.py db migrate 提交修改 
python models.py db upgrade 执行修改 
python models.py db downgrade 回退修改
'''
if __name__ == '__main__':
	manager.run()