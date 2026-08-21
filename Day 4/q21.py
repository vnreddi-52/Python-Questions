list_num = [10,20,20,30,40,40,50]

set_a=set()
set_duplicate=set()

for num in list_num:
    if num in set_a:
        set_duplicate.add(num)
    else:
        set_a.add(num)

print(set_duplicate)

