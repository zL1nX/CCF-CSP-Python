import json
n,m = map(int,input().split())
json_str = ''
for i in range(n):
    json_str += input()
my_json = json.loads(json_str)
for i in range(m):
    target_list = list(input().split('.'))
    res = my_json
    try:
        for j in range(len(target_list)):
            if res[target_list[j]] is not None:
                res = res[target_list[j]]
    except Exception:
        res = None
    if type(res) == str:
        print("STRING",res)
    elif type(res) == dict:
        print("OBJECT")
    else:
        print("NOTEXIST")

    
        
    
        
