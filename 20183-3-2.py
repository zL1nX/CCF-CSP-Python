n,m = map(int,input().split())
rules = {}
rlist = {}

for i in range(n):
    rule,res = input().split()
    rlist[rule] = rule.split('/')
    rules[rule] = res

for i in range(m):
    url = input().split('/')
    find = 0
    for rule in rules.keys():
        r = rlist[rule]
        if len(url)>=len(r):
            params = []
            match = 0
            pathfind = 0
            for j in range(len(r)):
                if url[j] == r[j]:
                    match += 1
                    
                elif r[j] == "<int>" and url[j].isdigit():
                    params.append(str(int(url[j])))
                    match += 1
                    
                elif r[j] == "<str>":
                    if url[j] == "":
                        break
                    params.append(url[j])
                    match += 1
                    
                elif r[j] == "<path>":
                    params.append("/".join(url[len(r)-1:]))
                    pathfind = 1
                    match += 1
                else:
                    break

            if match == len(r) and (len(url) == len(r) or pathfind):
                print(rules[rule] + " " + " ".join(params))
                find = True
                break
        else:
            continue
    if not find:
        print("404")


    
    
