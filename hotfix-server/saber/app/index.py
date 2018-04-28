#!/usr/bin/env python
# coding: utf-8

import time
import json
from flask import Flask, request, render_template, make_response, jsonify
# from saber.dbs.db_mysql import Db_mysql

app = Flask(__name__)
# db_mysql = Db_mysql()


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

# @app.route('/post/info', methods=['POST'])
# def post_info():
#     val = request.form['foo']
#     return db_mysql.get_multi(val)

@app.route('/test/patch', methods=['GET'])
def get_test_patch():
    with open('static/static/demo.js') as f:
        content = f.read()
        
    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=demo.js"
    return response


# stable version server
@app.route('/sdk/db/patch/info', methods=['GET'])
def get_patch_db_info():
    with open('static/patch/Tyrant/db/patchTyrantdb.json') as f:
        content_json = json.loads(f.read())
    response = jsonify(content_json)
    return response

@app.route('/sdk/db/patch/resource/<filename>', methods=['GET'])
def get_patch_db_src(filename):
    with open('static/patch/Tyrant/db/{}.{}'.format(filename, 'js')) as f:
        response = f.read();
    return response

@app.route('/sdk/game/patch/info', methods=['GET'])
def get_patch_game_info():
    with open('static/patch/Tyrant/game/patchTyrantdbGameTracker.json') as f:
        content_json = json.loads(f.read())
    response = jsonify(content_json)
    return response

@app.route('/sdk/game/patch/resource/<filename>', methods=['GET'])
def get_patch_game_src(filename):
    with open('static/patch/Tyrant/game/{}.{}'.format(filename, 'js')) as f:
        response = f.read();
    return response


# current version server
@app.route('/sdk/db/1.4/<jsonfile>', methods=['GET'])
def get_beta_patch_db_info(jsonfile):
    with open('static/patch/Tyrant/upyun/local/db/{}'.format(jsonfile)) as f:
        content_json = json.loads(f.read())
    response = jsonify(content_json)
    return response

@app.route('/db/<version>/patch/<filename>', methods=['GET'])
def get_beta_patch_db_src(version, filename):
    with open('static/patch/Tyrant/upyun/local/db/{}/{}'.format(version, filename)) as f:
        response = f.read();
    return response

@app.route('/sdk/game/1.4/<jsonfile>', methods=['GET'])
def get_beta_patch_game_info(jsonfile):
    with open('static/patch/Tyrant/upyun/local/game/{}'.format(jsonfile)) as f:
        content_json = json.loads(f.read())
    response = jsonify(content_json)
    return response

@app.route('/game/<version>/patch/<filename>', methods=['GET'])
def get_beta_patch_game_src(version, filename):
    with open('static/patch/Tyrant/upyun/local/game/{}/{}'.format(version, filename)) as f:
        response = f.read();
    return response


# mock tyrantdb server
def rebase_tyrantdb_response():
    time.sleep(20);
    return '1';

@app.route('/event', methods=['GET', 'POST'])
def request_tyrantdb_server_event():
    return rebase_tyrantdb_response()

@app.route('/identify', methods=['GET', 'POST'])
def request_tyrantdb_server_identify():
    return rebase_tyrantdb_response()

@app.route('/alias', methods=['GET', 'POST'])
def request_tyrantdb_server_alias():
    return rebase_tyrantdb_response()

@app.route('/page', methods=['GET', 'POST'])
def request_tyrantdb_server_page():
    return rebase_tyrantdb_response()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
