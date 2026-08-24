s = "Python is very easy to learn"
words=s.split(" ")

count=0
for word in words:
    count+=1;
print("No of words are" + str(count))

converted_S=s.upper()
print(converted_S)

words[3]="powerful"
print(words[3])