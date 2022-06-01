# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
from os import abort

import click
from flask import Flask, redirect, url_for, make_response, json, jsonify

app = Flask(__name__)

print(__name__);


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
# @app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


@app.route('/hello')
def hello():
    # return '<h1>Hello, Flask!</h1>'
    # return '', 302, {'Location': 'https://www.bilibili.com/'}
    return redirect(url_for('say_hello'))


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command('say-hello')
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')


@app.route('/404')
def not_found():
    abort(404)


@app.route('/foo')
def foo():
    data = {
        'name': 'Grey Li',
        'gender': 'male'
    }
    # response = make_response(json.dumps(data))
    # response.mimetype = 'application/json'
    # return response
    # return jsonify(name='Grey Li01', gender='male01')
    return jsonify(message='Error!'), 500


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response
