s=input()
count=0
for words in s:
    if words in "aeiou":
        count=count+1
print(count)