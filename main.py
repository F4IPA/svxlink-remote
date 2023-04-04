#!/usr/bin/python3

import flask
import os

CODES = ['ri49', 'nord', 'rrf', 'fon', 'tec', 'int', 'bav', 'loc', 'exp', 'reg']
KEY = str(open('/opt/svxlink-remote/key.txt', 'r').read()).strip()

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/dtmf', methods=['GET','POST'])
def exec_dtmf():
    key = str(flask.request.json['key']).strip()
    code = str(flask.request.json['code'])
    if key != KEY: return 'error'
    if code not in CODES: return 'error'    
    os.system(f'/etc/spotnik/restart.{code}')
    print(f'exec dtmf {code}')
    return 'ok'

app.run(host='0.0.0.0', port=8049, debug=False)