from datetime import datetime

from app_models import db


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

# if __name__ == '__main__':
#     db.create_all()