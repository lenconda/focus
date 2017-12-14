#! /usr/bin/python3

from ProjectLib import *
from dbIO import *

def TimerStart(username = '', token = ''):
    print('In \'TimerStart(username, token):\'');
    #1 set user.userid = username
    user = User(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
    user.userid = username;
    #1 set end
    status = GetCurrentClass(username, token);
    if not status['status']:
        return {'status': 1, 'message': 'Class not on now'};
    else:
        #2 user.read(this_start)
        user.this_start = user.query_thisstart();
        print('read', 'user.this_start', user.this_start); #debug
        #2 read end
        if user.this_start == -1:
            #3 user.write(this_class_start)
            user.this_class_start = class_begin[int(status['time'][1:3])];
            print('write', 'user.this_class_start', user.this_class_start); #debug
            user.save_thisclassstart();
            #3 write end
            #4 user.write(this_class_end)
            user.this_class_end = class_end[int(status['time']) % 100];
            print('write', 'user.this_class_end', user.this_class_end); #debug
            user.save_thisclassend();
            #4 write end
        #5 user.write(this_start)
        user.this_start = GetRelTime()[0];
        print('write', 'user.this_start', user.this_start); #debug
        user.save_thisstart();
        #5 write end
        return {'status': 1, 'message': 'Started successfully'};
    return {'status': 0, 'message': 'Unknown error'};

def TimerStop(username = '', token = ''):
    print('In \'TimerStop(username, token):\'');
    #1 set user.userid = username
    user = User(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
    user.userid = username;
    #1 set end
    now = GetRelTime()[0];
    #2 user.read(this_class_end)
    user.this_class_end = user.query_thisclassend();
    print('read', 'user.this_class_end', user.this_class_end); #debug
    #2 read end
    #3 user.read(this_start)
    user.this_start = user.query_thisstart();
    print('read', 'user.this_start', user.this_start); #debug
    #3 read end
    if user.this_start == -1:
        return {'status': 1, 'message': 'Timer not on now'};
    if user.this_class_end > now:
        t = now - user.this_start;
        #4 user.add(this_study, t)
        user.this_study = user.query_thisstudy();
        user.this_study += t;
        print('add', 'user.this_study', user.this_study - t, '->', user.this_study); #debug
        user.save_thisstudy();
        #4 add end
        #5 user.write(this_start)
        user.this_start = -1;
        user.save_thisstart();
        print('write', 'user.this_start', user.this_start);
        #5 write end
        return {'status': 1, 'message': 'Stopped successfully'};
    else:
        t = user.this_class_end - user.this_start;
        #6 User.add(this_study, t);
        user.this_study = user.query_thisstudy();
        user.this_study += t;
        print('add', 'user.this_study', user.this_study - t, '->', user.this_study); #debug
        user.save_thisstudy();
        #6 add end
        #7 user.write(this_start)
        user.this_start = -1;
        user.save_thisstart();
        print('write', 'user.this_start', user.this_start);
        #7 write end
        Submit(username);
        return {'status': 1, 'message': 'Submitted successfully'};
    return {'status': 0, 'message': 'Unknown error'};

def Submit(username = ''):
    #1 set user.userid = username
    user = User(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
    user.userid = username;
    #1 set end
    #2 class_end = User.read(this_class_end)
    user.this_class_end = user.query_thisclassend();
    print('read', 'user.this_class_end', user.this_class_end); # debug
    #2 read end
    #3 class_start = User.read(class_start)
    user.this_class_start = user.query_thisclassstart();
    print('read', 'user.this_class_start', user.this_class_start); # debug
    #3 read end
    this_total = user.this_class_end - user.this_class_start;
    #4 User.add(total_time, this_total)
    user.total_time = user.query_totaltime();
    user.total_time += this_total;
    print('add', 'user.this_total', user.total_time - this_total, '->', user.total_time); # debug
    user.save_totaltime();
    #4 add end
    #5 User.add(total_study, this_study)
    user.this_study = user.query_thisstudy();
    user.total_study = user.query_totalstudy();
    user.total_study += user.this_study;
    print('add', 'user.total_study', user.total_study - user.this_study, '->', user.total_study); # debug
    user.save_totalstudy();
    #5 add end
    #6 total_time = User.read(total_time)
    user.total_time = user.query_totaltime();
    print('read', 'user.total_time', user.total_time);
    #6 read end
    #7 total_study = User.read(total_study)
    user.total_study = user.query_totalstudy();
    print('read', 'user.total_study', user.total_study);
    #7 read end
    user.percentage = float(user.total_study) / user.total_time;
    #8 User.write(percentage)
    user.save_percentage();
    print('write', 'user.percentage', user.percentage);
    #8 write end
    #9 User.write(this_study = 0, this_start = -1)
    user.this_start = -1;
    user.save_thisstart();
    print('write', 'user.this_start', user.this_start);
    user.this_study = 0;
    user.save_thisstudy();
    print('write', 'user.this_study', user.this_study);
    #9 write end
    return {'status': 1};

if __name__ == '__main__':
    TimerStart();
