def event_sort(event, num):
    for i in range(2*num-1):
        for j in range(2*num-1-i):
            if event[j][0] > event[j+1][0]:
                a = event[j][0]
                b = event[j][1]
                event[j][0] = event[j+1][0]
                event[j][1] = event[j+1][1]
                event[j+1][0] = a
                event[j+1][1] = b
            elif event[j][0] == event[j+1][0]:
                if event[j][1] < 0:
                    a = event[j][0]
                    b = event[j][1]
                    event[j][0] = event[j+1][0]
                    event[j][1] = event[j+1][1]
                    event[j+1][0] = a
                    event[j+1][1] = b
                elif event[j][1] > 0 and event[j+1][1] >0 and event[j][1] > event[j+1][1]:
                    a = event[j][0]
                    b = event[j][1]
                    event[j][0] = event[j+1][0]
                    event[j][1] = event[j+1][1]
                    event[j+1][0] = a
                    event[j+1][1] = b

def return_key(keys, key_no,num):
    for i in range(num):
        if keys[i] == 0:
            keys[i] = key_no
            break

def borrow_key(keys,key_no,num):
    for i in range(num):
        if keys[i] == key_no:
            keys[i] = 0
            break

def wrap_up():
    class_num, teacher_num = map(int,input().split())
    keys = list(range(1,class_num+1))
    event = [[0 for i in range(2)]for j in range(2*teacher_num)]
    i = 0
    while i<2*teacher_num:
        key_no, start,duration = map(int,input().split())
        event[i][0] = start
        event[i][1] = -key_no
        i+=1
        event[i][0] = start+duration
        event[i][1] = key_no
        i+=1
    event_sort(event, teacher_num)
    for i in range(2*teacher_num):
        if event[i][1] > 0:
            return_key(keys,event[i][1],class_num)
        elif event[i][1] < 0:
            borrow_key(keys,-event[i][1],class_num)

    for i in range(class_num):
        print(keys[i], end = ' ')

wrap_up()
