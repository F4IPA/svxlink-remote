#!/usr/bin/python3

import flask
import os

PATH = os.getcwd() + '/'
DTMF = [96, 97, 98, 99, 100, 101, 102, 104, 200, 1000]
KEY  = str(open(PATH + 'key.txt', 'r').read()).strip()

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/dtmf', methods=['GET','POST'])
def exec_dtmf():
    key = str(flask.request.json['key']).strip()
    code = int(flask.request.json['code'])
    if key != KEY: return 'error'
    if code not in DTMF: return 'error'    
    os.system(f'echo {code}# > /tmp/dtmf_uhf')
    print(f'exec dtmf {code}')
    return 'ok'

app.run(host='0.0.0.0', port=8049, debug=False)