a = [1,2,3,2,4,1,5]
dic={}
for i in a:
    dic[i]=dic.get(i,0)+1
count=0
for i in dic.values():
    if i>=2:
        count+=1
print(count)
