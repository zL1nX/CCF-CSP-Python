num = int(input())
sales =list(map(int, input().split()))

res = 0
delta = []
for i in range(1,num-1):
    if((sales[i-1] > sales[i] and sales[i] < sales[i+1]) or (sales[i-1] < sales[i] and sales[i] > sales[i+1])):
           res += 1

print(res)
