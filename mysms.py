#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import Form
from dysms_python import sms_send
from dysms_python import sms_query
import json
import uuid

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('alert.html', IsAlert=1)

@app.route('/alert')
def alert():
    return render_template('alert.html', IsAlert=1)

@app.route('/alertEnd')
def alertEnd():
    return render_template('alertEnd.html', IsAlertEnd=1)

@app.route('/change')
def change():
    return render_template('change.html', IsChange=1)

@app.route('/changeEnd')
def changeEnd():
    return render_template('changeEnd.html', IsChangeEnd=1)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    __business_id = uuid.uuid1()
    name=request.form['name']
    time=request.form['time']
    context=request.form['context']
    unit=request.form['unit']
    phoneNum=request.form['phoneNum']
    print name
    params = {'name': name, 'time': time, 'coontext':context,'unit':unit }
    params_j = json.dumps(params, encoding='UTF-8', ensure_ascii=False)
    print(sms_send.send_sms(__business_id, "18600687990", "航天云网运维中心", "SMS_141616866",params_j))
    return render_template('test.html', name=name,time=time,context=context,phoneNum=phoneNum)

@app.route('/userGuid')
def userGuid():
    return render_template('userGuid.html',)

@app.route('/login')
def login():
    isLogin=1
    return render_template('index1.html', IsLogin=1)

def checkLogin():
    return 1



if __name__ == '__main__':
    app.run(host='0.0.0.0')
