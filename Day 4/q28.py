list_num=[10,20,30,40]

def find_largest(list_num):
    largest=0;
    for i in list_num:
        if i>largest:
            largest=i

    return largest

print(find_largest(list_num))

