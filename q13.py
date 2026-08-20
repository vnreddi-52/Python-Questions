numbers =[12,5,8,21,4,15,10]
largest=0
smallest=float("inf")
sum=0
for i in numbers:
    if i>largest:
        largest=i;
    if i<smallest:
        smallest=i;
    sum+=i;

print(largest)
print(smallest)
print(sum)