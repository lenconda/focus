#! /usr/bin/python3

import time


class_begin = {
    1: 7 * 3600 + 50 * 60,
    2: 8 * 3600 + 40 * 60,
    3: 9 * 3600 + 45 * 60,
    4: 10 * 3600 + 35 * 60,
    5: 11 * 3600 + 25 * 60,
    6: 13 * 3600 + 50 * 60,
    7: 14 * 3600 + 40 * 60,
    8: 15 * 3600 + 45 * 60,
    9: 16 * 3600 + 35 * 60,
    10: 17 * 3600 + 25 * 60,
    11: 19 * 3600 + 0 * 60,
    12: 19 * 3600 + 50 * 60,
    13: 20 * 3600 + 40 * 60,
    14: 24 * 3600 + 0 * 60
    };

class_end = {
    1: 8 * 3600 + 35 * 60,
    2: 9 * 3600 + 25 * 60,
    3: 10 * 3600 + 30 * 60,
    4: 11 * 3600 + 20 * 60,
    5: 12 * 3600 + 10 * 60,
    6: 14 * 3600 + 35 * 60,
    7: 15 * 3600 + 25 * 60,
    8: 16 * 3600 + 30 * 60,
    9: 17 * 3600 + 20 * 60,
    10: 18 * 3600 + 10 * 60,
    11: 19 * 3600 + 45 * 60,
    12: 20 * 3600 + 35 * 60,
    13: 21 * 3600 + 25 * 60
    };

def GetRelTime():
    t = time.localtime(time.time());
    current = -1;
    day = t[6] + 1;
    t = t[3] * 3600 + t[4] * 60 + t[5];
    return [t, day];

def IsClassOn(t = '', now = []): # t is time string, now contains [currentclass, currentweek]
    print('In \'IsClassOn(t, now):\'');
    day = int(t[0]);
    t = int(t[1:]);
    classes = [];
    while t:
        classes.append(t % 100);
        t = int(t / 100);
    # loads classes
    if not now[1] == day:
        return 0;
    if now[0] <= classes[0] and now[0] >= classes.pop():
        return 1;
    else:
        return 0;
    # returns whether class is on(1) or not(0)

def ClassTime(): # don't need parameters, just gets current time
    print('In \'ClassTime():\'');
    t = GetRelTime();
    day = t[1];
    t = t[0];
    # set the every first second each day as 0, use relative seconds
    for n in range(1, 14):
        if t >= class_begin[n] and t < class_begin[n+1]:
            current = n + 0.5;
            if t <= class_end[n]:
                current -= 0.5;
            break;
    return [current, day];
    # returns [#currentclass, currentday]

if __name__ == '__main__':
    ClassTime();
