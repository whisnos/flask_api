# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
from apps.models import db
from apps.models.base import BaseModel


class Book(db.Model,BaseModel):
	name = db.Column(db.String(20), unique=True)
	mobile = db.Column(db.String(11), unique=True)
	def __repr__(self):
		return '<User> %s' % self.name
