import jwt
import datetime
import hashlib

SECRECT_KEY = 'secret'

def md5Encoding(youstr):
    m=hashlib.md5()
    m.update(youstr)
    encodingstr=m.hexdigest()
    print(encodingstr)


# 生成jwt 信息
def  jwtEncoding(some,aud='webkit'):
    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=180)
    print(datetimeInt)
    option = {
        'exp':datetimeInt,
        'aud': aud,
        'some': some
    }
    encoded2 = jwt.encode(option, SECRECT_KEY, algorithm='HS256')
    return encoded2


# userInfo = {
#             "id":12,
#             "username":"2234",
#             "email":"23423dsd"
#         }
#
# listr = jwtEncoding(userInfo)
# print(listr.decode())


# 解析jwt 信息
def  jwtDecoding(token,aud='webkit'):
    decoded = None
    try:
        decoded = jwt.decode(token, SECRECT_KEY, audience=aud, algorithms=['HS256'])
    except jwt.ExpiredSignatureError :
        print("erroing.................")
        decoded = {"error_msg":"is timeout !!","some":None}
    except Exception:
        decoded ={"error_msg":"noknow exception!!","some":None}
        print("erroing2.................")
    return decoded