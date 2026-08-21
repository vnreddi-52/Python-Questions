list_num = [10,20,10,30,20,40,30]
new_list=[]

for num in list_num:
    if num not in new_list:
        new_list.append(num)

print(new_list)

