list_num = [10,20,30,40]
largest=0;
sec_largest=0;

for num in list_num:
    if (num>largest):
        sec_largest=largest
        largest=num
    if sec_largest>largest:
        sec_largest=num

print(sec_largest)
