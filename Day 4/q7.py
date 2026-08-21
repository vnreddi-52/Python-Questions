string = input()
reversed_string=""
for i in range(0,len(string),1):
    reversed_string += string[len(string)-i-1]
print(reversed_string)

if string==reversed_string:
    print("Palindrome")
else:
    print("Not Palindrome")

