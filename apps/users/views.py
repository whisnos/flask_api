from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required
from flask_login import login_required
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from apps.common.maketoken import jwtEncoding
from apps.common.utils import trueReturn, falseReturn
from apps.models.user import User
from apps.users.forms import SearchForms
# from models import User

users = Blueprint('users', __name__)


@users.route('/')
def hello():
	# form做参数的验证
	form = SearchForms(request.args)
	if form.validate():
		q = form.q.data
		page = form.page.data
		print(123, q, page)
		resp = {'msg': '成功'}
		return jsonify(resp)
	return jsonify(form.errors),400


@users.route('/login', methods=['GET', 'POST'])
def login():
	str = request.get_json()
	print(str)
	name = str['name']

	admin = User.query.filter_by(name=name).first()  # 这里需要重新修改成成缓存里取，减少处理时间

	userInfo = {
		"id": admin.id,
		"username": admin.name,
		"email": admin.email
	}

	if admin == None:
		return jsonify(trueReturn("{'ok':Flase}", "not the user"))
	else:
		# request.headers['Authorization']='liuliuyyeshibushidslfdslfsdkfkdsf23234243kds'
		# login_user(admin)
		token = jwtEncoding(userInfo)
		print(token)
		return jsonify(trueReturn("{'ok':True,'token':" + token.decode() + "}", "you are sucess"))


class UserInfoViewset(Resource):
	"""
	示例profile list资源类
	"""

	def __init__(self):
		self.parser = RequestParser()

	def post(self):
		"""
				用户注册
				:return: json
		 """
		email = request.json.get('email')
		name = request.json.get('name')
		password = request.json.get('password')
		address = request.json.get('address')
		print('request.form', email)
		user = User(name=name, email=email, address=address, password=User.set_password(password))
		print('user', user)
		result = User.add(user)
		if user.id:
			returnUser = {
				'id': user.id,
				'name': user.name,
				'email': user.email,
				'address': user.address
			}
			return jsonify(trueReturn(returnUser, "用户注册成功"))
		else:
			return jsonify(falseReturn('', '用户注册失败'))

	# @login_required
	def get(self):
		openid = request.json.get('openid')
		user = User.query.filter(openid=openid)
		resp = {"get": "get"}
		return resp, 201

	def put(self, id):
		id = id
		dict_data = request.json
		name = dict_data.get('name')
		print('name', name)
		resp = {"put": "put"}
		return jsonify(trueReturn(resp, '修改成功'))
