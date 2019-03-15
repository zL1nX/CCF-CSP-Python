n = int(input())
ticket = list(map(int,input().split()))
seats = [[0 for i in range(6)]for j in range(20)]

for i in range(20):
    seats[i][0] = 5


for i  in range(n):
    end = 0
    line = 0
    for j in range(20):
        count = 0
        if seats[j][0] < ticket[i]:
            continue
        
        for k in range(1,6):
            if seats[j][k] == 0:
                count += 1
                if count == ticket[i]:
                    end = k
                    line = j
                    seats[j][0] -= count
                    break
            else:
                count = 0

        if end:
            for k in range(end+1 - count, end+1):
                seats[j][k] = 1
                print(line * 5 + k, end = ' ')
            print()
            break
    if not end:
        for x in range(ticket[i]):
            flag = 0
            for j in range(20):
                if seats[j][0] >=1:
                    for k in range(1,6):
                        if seats[j][k] == 0:
                            seats[j][k] = 1
                            seats[j][0] -=1
                            flag = 1
                            print(j*5 + k, end=' ')
                            break
                if flag:break
        print()
                    
            
            


