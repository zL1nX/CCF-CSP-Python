red,yellow,green=list(map(int,input().split()))
light = [red,green,yellow]
num = int(input())
used_time = 0
for i in range(num):
    kind,time = map(int,input().split())
    if kind == 0:
        used_time += time
    else:
        if kind == 1:
            kind = 0
        elif kind == 3:
            kind = 1  
        if used_time - time > 0:
            time = used_time - time
            while time - light[(kind+1)%3] >= 0:
                kind  = (kind + 1)%3
                time -= light[kind]
            kind = (kind+1)%3
            time = light[kind] - time
                
        elif used_time - time <= 0 :
            time = time - used_time
            
        if kind == 0:
            used_time += time
        elif kind == 2:
            used_time += time + light[0]

print(used_time)
