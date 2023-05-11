#!/bin/env python
#coding=utf-8

import json
import sys
sys.path.append('.')
from query_parser import QueryParser
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/s", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        if 'query' in request.form:
            query = request.form['query']
        else:
            query = request.args.get('query')
    else:
        query = request.args.get('query')
    qp = QueryParser()
    ret = qp.parse_query(query)
    res = {'query': query, 'answer': ret}
    return render_template('result.html', result=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008, debug=True)
