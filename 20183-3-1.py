#url
import re
m,n=map(int,input().split())
 
rules ={}
rlist ={}
querys =[]
 
for i in range(m):
    rule,name = input().split()
    rlist[rule] = rule.split("/")
    rules[rule] = name
    
for i in range(n):
    query = input()
    q = query.split("/")
    find=False
    for rule in rules.keys():
        r = rlist[rule]
        if(len(q)>=len(r)):
            print('r',r)
            args=[]
            match=0
            RightPath=False
            for j in range(len(r)):
                if(q[j]==r[j]):
                    print('1')
                    match+=1
                    
                elif(q[j].isdigit() and r[j]=="<int>"):
                    print('2')
                    args.append(str(int(q[j])))
                    match+=1
                    
                elif(r[j]=="<str>"):
                    if(q[j]==""):       #加了这个判断就100分了 ?!空字符串对应<str>
                        break
                    print('3')
                    args.append(q[j])
                    match+=1
                    
                    
                elif(r[j]=="<path>"):
                    print('4')
                    args.append("/".join(q[len(r)-1:]))
                    RightPath=True
                    match+=1
                    
                else:
                    break
            
            if(match == len(r) and (len(q)==len(r) or RightPath)):
                print(rules[rule]+" "+" ".join(args))
                find=True
                break
        else:
            continue
    if(not find):
        print("404")
