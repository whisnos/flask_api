from datetime import datetime

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WRON'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/tong_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

# @manager.command
# def create_db():
# 	'''说明文件写在此处'''
# 	from models import db
# 	db.create_all()
# 	print('数据表创建完成')

manager.add_command('db', MigrateCommand)  # 添加db 命令（runserver的用法）


# class Articles(db.Model):
#     __tablename__ = 'articles'  # 自定义数据表名称，如不设置默认设置为类名
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     title = db.Column(db.String(80))  # 唯一键
#     content = db.Column(db.String(80))
#     add_time = db.Column(db.DateTime, default=datetime.now)
# def __repr__(self):
#     return '<User %r>' % self.username


class User(db.Model):
    CHOOSEY_TYPE = {
        (1, '1队'),
        (2, '2队'),
        (3, '3队'),
    }
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    mobile = db.Column(db.String(11), unique=True)
    back_mobile = db.Column(db.String(11), nullable=True)
    group = db.Column(db.Integer, default=CHOOSEY_TYPE, unique=True, )  # 分组
    work = db.Column(db.String(50), nullable=True)
    openid = db.Column(db.String(50), unique=True)
    session_token = '123213dsfw3432'

    def __repr__(self):
        return '<User> %s' % self.name

    @classmethod
    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    @classmethod
    def add(self, user):
        db.session.add(user)
        return session_commit()

    def get_id(self):
        return self.session_token


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason


'''
python models.py db init 创建数据表
python models.py db migrate 提交修改 
python models.py db upgrade 执行修改 
python models.py db downgrade 回退修改
'''
# if __name__ == '__main__':
#     manager.run()
