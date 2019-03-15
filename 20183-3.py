def process(rule):
    rules = []
    if 'path' in rule:
        cell_rule = rule.split('/')[1:]
    else:
        cell_rule = rule.split('/')[1:]
    for i in range(len(cell_rule)):
        rules.append(cell_rule[i])
    return rules

def project(url,rules,results):
    url_s = url
    for i in range(len(rules)):
        flag = 0
        res_param = []
        res_str = []
        if len(rules[i]) != len(url):
            if '<path>' in rules[i]:
                rules[i] = rules[i][:-1]
                url_s = url[:len(rules[i])]
                flag = 1
            else:
                continue
        wrong = 0
        for cell,cell_rule in zip(url_s,rules[i]):
            if cell_rule == cell:
                pass
            elif cell_rule == '<int>' and cell.isdigit():
                res_param.append(str(int(cell)))
            elif cell_rule == '<str>':
                if cell == "":
                    wrong = 1
                    break
                res_param.append(cell)
            else:
                wrong = 1
                break
        if not wrong:#找到了这条规则
            res_str.append(results[i])
            if flag:
                left = url[len(rules[i]):]
                res_param.append("/".join(left))
            return res_str+res_param
    return ['404']
                

def find(urls,rules,results):
    url_res = []
    for url in urls:
        if url[-1] == '/':
            url = url.split('/')[1:]
        else:
            url = url.split('/')[1:]
        url_res.append(project(url,rules,results))
    return url_res
            
def wrap_up():
    url_rules = []
    url_res = []
    urls = []
    n,m = map(int,input().split())
    for i in range(n):
        url_rule, url_r = input().split()
        url_rules.append(process(url_rule))
        url_res.append(url_r)

    for i in range(m):
        urls.append(input())

    res = find(urls,url_rules,url_res)
    for item in res:
        print(" ".join(map(str,item)))

wrap_up()
