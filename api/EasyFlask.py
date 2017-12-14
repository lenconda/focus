#! /usr/bin/python3

from flask import Flask, make_response
from flask import request
from ProjectLib import *
import random

def pack(data = ''): # solves the access-control problem
    res = make_response(data);
    res.mimetype = 'application/json';
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
    return res;

app = Flask(__name__);

@app.route('/login', methods = ['POST']) # provides authorization info
def login():
    user = User(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
    if request.form.get('type') == 'test':
        res = GetAuth(request.form.get('username'), request.form.get('password'));
        user.userid = request.form.get('username');
    else:
        form = json.loads(request.data);
        res = GetAuth(form['username'], form['password']);
        user.userid = form['username'];
    if not res['status']:
        return pack(json.dumps(res));
    profile = GetProfile(user.userid, res['token']);
    user.gender = profile['gender'];
    user.name = profile['name'];
    user.school = profile['school'];
    if not user.isexist():
        user.avatar = random.randrange(1,11,1);
        user.save_name_userid_avatar_gender_school();
    # User.userid = form['userid']
    # 查询userid，如果有记录的话直接返回，否则创建条目后返回
    return pack(json.dumps(res));

@app.route('/login', methods = ['GET'])
def test_login():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">SLog In</button></p>
              </form>
           ''';

@app.route('/profile', methods = ['POST']) # provides student profile
def profile_post():
    user = User(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
    if request.form.get('type') == 'test':
        user.userid = request.form.get('userid');
    else:
        info = json.loads(request.data);
        user.userid = info['userid'];
    extrainfo = user.query_profile();
    info = {'avatar': extrainfo['avatar'], 'profile': []};
    info['profile'].append({'key': '学号', 'value': user.userid});
    info['profile'].append({'key': '姓名', 'value': extrainfo['name']});
    info['profile'].append({'key': '性别', 'value': extrainfo['gender']});
    info['profile'].append({'key': '学院', 'value': extrainfo['school']});
    info['profile'].append({'key': '总时间', 'value': round(extrainfo['total_time'] / 3600.0, 1)});
    info['profile'].append({'key': '学习时间', 'value': round(extrainfo['total_study'] / 3600.0, 1)});
    info['profile'].append({'key': '当前排名', 'value': user.chaxunmingci()});
    info['profile'].append({'key': '分数', 'value': round(extrainfo['percentage'] * 100, 4)});
    return pack(json.dumps(info));
    

@app.route('/profile', methods = ['GET'])
def profile_get():
    return '''<form action="/profile" method="post">
              <p><input name="userid"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logr In</button></p>
              </form>
           ''';

@app.route('/schedule', methods = ['POST'])
def schedule_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('username');
        info = GetWeek(username, token);
    else:
        info = json.loads(request.data);
        info = GetWeek(info['username'], info['token']);
    return pack(json.dumps(info));
    
@app.route('/schedule', methods = ['GET'])
def schedule_get():
    return '''<form action="/schedule" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logr In</button></p>
              </form>
           ''';

@app.route('/current', methods = ['POST'])
def current_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('username');
        info = GetCurrentClass(username, token);
    else:
        info = json.loads(request.data);
        info = GetCurrentClass(info['username'], info['token']);
    return pack(json.dumps(info));
    
@app.route('/current', methods = ['GET'])
def current_get():
    return '''<form action="/current" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logc In</button></p>
              </form>
           ''';

@app.route('/start', methods = ['POST'])
def start_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('userid');
        info = TimerStart(username, token);
    else:
        info = json.loads(request.data);
        info = TimerStart(info['userid'], info['token']);
    return pack(json.dumps(info));
    
@app.route('/start', methods = ['GET'])
def start_get():
    return '''<form action="/start" method="post">
              <p><input name="userid"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logc In</button></p>
              </form>
           ''';

@app.route('/stop', methods = ['POST'])
def stop_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('userid');
        info = TimerStop(username, token);
    else:
        info = json.loads(request.data);
        info = TimerStop(info['userid'], info['token']);
    return pack(json.dumps(info));
    
@app.route('/stop', methods = ['GET'])
def stop_get():
    return '''<form action="/stop" method="post">
              <p><input name="userid"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logc In</button></p>
              </form>
           ''';

@app.route('/ranklist', methods = ['GET', 'POST'])
def ranklist():
    user = User(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
    info = user.paiming100();
    return pack(json.dumps(info));

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3000);
