import datetime
import time

def time_clear(mission_time):
    week = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for m in range(len(mission_time)):
        for i in range(12):
            mission_time[m] = mission_time[m].replace(month[i],str(i+1))
        for i in range(7):
            mission_time[m] = mission_time[m].replace(week[i],str(i))
        if ',' in mission_time[m] or '-' in mission_time[m]:
            temp = list(mission_time[m].split(','))
            mission_time[m] = []
            for j in range(len(temp)):
                if '-' in temp[j]:
                    start,end = map(int,temp[j].split('-'))
                    temp[j] = list(map(str,list(range(start,end+1))))
            for j in temp:
                if type(j) == list:
                    for k in j:
                        mission_time[m].append(k)
                else:
                    mission_time[m].append(j)
    return mission_time


def time_comp(current_time,mission_time):
    current_time_tab = [current_time.minute, current_time.hour,current_time.day,current_time.month,(current_time.weekday()+1)%7]
    #match = 0
    for current,mission in zip(current_time_tab,mission_time):
        current = str(current)
        if mission == '*':
            pass#match += 1
        elif (type(mission) == list and current in mission) or (type(mission) == str and current == mission):
            pass#match += 1
        else:
            return 0
    return 1

def wrap_up():
    missions_time = []
    missions = []
    date_form = "%Y%m%d%H%M"
    n,s,t = input().split()
    start_time = datetime.datetime.strptime(s,date_form)
    end_time = datetime.datetime.strptime(t,date_form)
    for i in range(int(n)):
        item = input().split()
        missions_time.append(item[:len(item)-1])
        missions.append(item[-1:])

    for i in range(len(missions_time)):
        missions_time[i] = time_clear(missions_time[i])

    current_time = start_time
    time_delta = datetime.timedelta(minutes=1)
    while current_time < end_time:
        for i in range(len(missions_time)):
            if time_comp(current_time,missions_time[i]):
                form_current_time = current_time.strftime(date_form)
                print(form_current_time,missions[i][0])
        current_time += time_delta

wrap_up()

        
