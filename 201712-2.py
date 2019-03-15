n,k = map(int,input().split())
kids = [0]*n
flag = [1]*n
kids[0] = 1
i = 0
last = n-1
left = n
while True:
    if flag[i]:
        kids[i] = kids[last] + 1
        last = i
        if kids[i]%k == 0 or kids[i]%10 == k:
            flag[i] = 0
            left -= 1 
        if left == 1:
            print(flag.index(1)+1)
            break
    i = (i+1)%n


'''n,k = map(int,input().split())
l = list(range(1,n+1))
 
num = 1
while len(l)>0:
    keys_del = []
    for key,value in enumerate(l):
        if(num%k == 0 or num%10 == k):
            #print("num ",num," del ",dic[key])
            keys_del.append(key)
        num +=1
    acount=0
    for key in keys_del:
        del l[key-acount]
        acount+=1
        if(len(l)==1):
            print(l[0])'''

    
        
