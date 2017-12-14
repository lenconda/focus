#! /usr/bin/python3

from GetAuth import *
from TimeProc import *
import requests
import json


infohost = 'weixin.ncuos.com';

def GetWeek(username = '', token = ''): # get week schedule
    dest = '/schedule/api/schedule';
    url = 'http://' + infohost + dest;
    headers = GenHeader(token = token);
    data = (json.dumps({'studentId': username})).encode('utf-8');
    week = requests.post(url = url, headers = headers, data = data);
    if(week.json()['data']):
        print('Have such student.');
    else:
        print('No such student!!');
    return week.json();

def GetClassInfo(username = '', password = '', coursename = ''): # get specific info about a class
    dest = '/schedule/api/schedule/exam';
    url = 'http://' + infohost + dest;
    headers = GenHeader(username, password);
    print('headers:', headers);
    data = json.dumps({'courseName': coursename}).encode('utf-8');
    print('searched course is:', data.decode('utf-8'));
    info = requests.post(url = url, headers = headers, data = data);
    return info.json();

def GetRawProfile(username = '', token = ''):
    dest = '/api/user/profile/basic';
    url = 'http://' + loginhost + dest;
    headers = GenHeader(token = token);
    print('headers:', headers);
    profile = requests.get(url = url, headers = headers);
    return profile.json();

def GetProfile(username = '', token = ''):
    profile = GetRawProfile(username, token);
    roll = requests.get(url = 'http://' + loginhost + '/api/user/profile/school_roll', headers = GenHeader(token)).json();
    return {'gender': profile['base_info']['xb']['mc'], 'name': profile['base_info']['xm'], 'school' : roll['school_roll'][0]['xy']};
    #return {'gender': profile['base_info']['xb']['mc']};

def GetCurrentClass(username = '', token = ''):
    print('In \'GetCurrentClass(username, token):\'');
    schedule = GetWeek(username, token);
    week = schedule['currentWeek'];
    schedule = schedule['data']['lessons'];
    for course in schedule:
        course['week'] = course['week'].split('-');
        if not (week >= int(course['week'][0]) and week <= int(course['week'][1])):
            continue;
        elif IsClassOn(course['time'], ClassTime()) :
            return {'courseName': course['name'], 'status': 1, 'time': course['time']};
    return {'courseName': '', 'status': 0};
