'''num = int(input())
time1,time2 = [],[]
for i in range(num):
    time1.append(list(map(int,input().split())))
for i in range(num):
    time2.append(list(map(int,input().split())))
res = 0
for i in range(num):
    for j in range(num):
        if(time1[i][0] < time2[j][1] and time1[i][1] > time2[j][0]):
            res += min(time2[j][1],time1[i][1]) - max(time1[i][0],time2[j][0])
    
print(res)'''

num = int(input())
MAX = 1000000
timeline = [0]*MAX
res = 0
dur = 0
for i in range(2*num):
    temp = list(map(int,input().split()))
    timeline[temp[0]] += 1
    timeline[temp[1]] -= 1

for i in range(MAX):
    res += timeline[i]
    dur += (res == 2)
    
print(dur)


