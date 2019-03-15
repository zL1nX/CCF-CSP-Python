stu_num = int(input())
times = int(input())
stu = [i for i in range(1,stu_num+1)]
for t in range(times):
    stu_no,move = map(int,input().split())
    place = stu.index(stu_no)
    if move >= 0:
        for j in range(place,place+1+move):
            if j == place+move:
                stu[j] = stu_no
            else: stu[j] = stu[j+1]          
    else:
        for j in range(place,place+move-1,-1):
            if j == place + move:
                stu[j] = stu_no
            else: stu[j] = stu[j-1]

for i in range(stu_num):
    print(stu[i], end = ' ')
