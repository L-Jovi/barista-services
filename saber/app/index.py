#!/usr/bin/env python
# coding: utf-8

import json
from flask import Flask, request, render_template, make_response
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

@app.route('/download', methods=['GET'])
def get_js():
    with open('static/demo.js') as f:
        content = f.read()
        
    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=demo.js"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
