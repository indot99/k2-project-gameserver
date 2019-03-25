from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

##############
#Flask 라우팅#
##############

# @app.route()를 통해 URL패턴과 POST Method를 정의하고
# 바로 하단의 함수에서 URL 패턴 매칭되는 Action을 처리

# app.debug는 개발의 편의를 위해 존재하며, True값일 경우 코드를 변경하면
# 자동으로 서버가 재실행된다.
# 웹상에서 파이썬 코드를 수행할 수 있게 되므로, 운영환경에서는 주의해야함

# 외부에서도 접근을 가능하게 하려면 app.run(host='0.0.0.0')로
# 서버 실행부를 변경해야 한다.

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/main')
def main():
    return 'Main Page'

# <>로 URL패턴을 변수로 처리 가능
# <자료형: 변수명>형식으로 URL패턴 검증 가능 int:는 정수만 입력가능을 의미

@app.route('/routing/<username>')
def showUserProfile(username):
    return 'USER : %s' % username

@app.route('/routing/id<int:userId>')
def showUserProfileById(userId):
    return 'USER ID : %d' % userId

@app.route('/account/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data['id'])
    print(data['pw'])
    return data['id']

app.secret_key = 'sample_secret_key'

#######################################################

if __name__ == '__main__':
    app.run(debug = True)