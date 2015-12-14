#!/usr/bin/env python
# coding: utf-8

import json
from flask import Flask, request, render_template, make_response, jsonify
from saber.dbs.db_mysql import Db_mysql

app = Flask(__name__)
db_mysql = Db_mysql()


@app.route('/')
def index():
    obj = {
        'foo': 'bar',
        'sth': 'happend'
    }
    return json.dumps(obj)

@app.route('/form')
def form():
    print request.data
    return render_template('bing.html', title="test page")

@app.route('/post/info', methods=['POST'])
def post_info():
    val = request.form['foo']
    return db_mysql.get_multi(val)

@app.route('/test/patch', methods=['GET'])
def get_test_patch():
    with open('static/static/demo.js') as f:
        content = f.read()
        
    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=demo.js"
    return response


@app.route('/sdk/db/patch/info', methods=['GET'])
def get_patch_db_info():
    with open('static/patch/Tyrantdb-iOS/db/patch.json') as f:
        content_json = json.loads(f.read())
    response = jsonify(content_json)
    return response

@app.route('/sdk/db/patch/resource/<filename>', methods=['GET'])
def get_patch_db_src(filename):
    with open('static/patch/Tyrantdb-iOS/db/{}.{}'.format(filename, 'js')) as f:
        response = f.read();
    return response

@app.route('/sdk/game/patch/info', methods=['GET'])
def get_patch_game_info():
    with open('static/patch/Tyrantdb-iOS/game/patch.json') as f:
        content_json = json.loads(f.read())
    response = jsonify(content_json)
    return response

@app.route('/sdk/game/patch/resource/<filename>', methods=['GET'])
def get_patch_game_src(filename):
    with open('static/patch/Tyrantdb-iOS/game/{}.{}'.format(filename, 'js')) as f:
        response = f.read();
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
