list_num = [1,2,3,4]

largest=float('-inf')
smallest=float('inf')

for num in list_num:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print(smallest)
print(largest)