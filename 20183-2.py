n,l,t = list(map(int,input().split()))
ball = list(map(int,input().split()))
move = [1]*n
crash = [1]*n
for i in range(t):
    crash = [0]*n
    for j in range(n):
        if ball[j] == 0 or ball[j] == l:
            move[j] = -move[j]
        for k in range(n):
            if ball[k] == ball[j] and crash[k] == 0 and crash[j] == 0 and k != j:
                crash[j] = 1
                crash[k] = 1
                move[k] = -move[k]
                move[j] = -move[j]
                break;
        if crash[j] == 0:
            continue
    for j in range(n):
        ball[j] += move[j]

for i in range(n):
    print(ball[i],end=' ')


