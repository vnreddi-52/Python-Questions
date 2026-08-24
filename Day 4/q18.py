tuple_num=(10,20,30,40)

total_sum=0
largest=float('-inf')
smallest=float('inf')

for num in tuple_num:
    total_sum+=num

    if num>largest:
        largest=num

    if num<smallest:
        smallest=num

print(total_sum)
print(largest)
print(smallest)