#! /usr/bin/python3

import requests
import chardet
import json

global username, password;
loginhost = 'os.ncuos.com';

def GetAccuont(): # get student's basic info
    # currently unable to work on this field. Will try later.
    pass;

def GetAuth(username = '', password = ''): # get "Authorization" token
    dest = '/api/user/token';
    url = 'https://' + loginhost + dest;
    headers = {'Content-Type': 'application/json'};
    data = '{"username": "' + username + '", "password": "' + password + '"}';
    # print('headers: ', headers);
    # print('data: ', data);
    # print('url: ', url);
    AuthToken = requests.post(url = url, headers = headers, data = data).json();
    if(AuthToken['status']):
        print('Login success, token is', AuthToken['token']);
    else:
        print('Login error!');
    return AuthToken;

def GenHeader(token = ''): # generate headers for API post requests
    header = {
        'Authorization': 'passport ' + token,
        'Content-Type': 'application/json'
        };
    return header;

if __name__ == '__main__':
    GetAuth();
