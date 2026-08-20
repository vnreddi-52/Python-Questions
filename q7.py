n=583246
even_no=0;
while (n!=0):
    digit =n%10;
    if n%2==0:
        even_no += 1;
    n = n // 10;
print(even_no)
