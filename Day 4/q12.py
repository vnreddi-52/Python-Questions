num = int(input())

if num<=1:
    print("Not a Prime Number")
else:
    for i in range(2,num//2):
        if num%i==0:
            print("Not a Prime Number")
    print("Prime Number")