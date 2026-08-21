s=input("Enter the sentence :")
words=s.split()
dic={}
for i in words:
    dic[i]=dic.get(i,0)+1
print(dic)