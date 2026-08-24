sentence = "Python is easy and Python is powerful"

words = sentence.split()

python_count = 0

for word in words:
    if word == "Python":
        python_count += 1

print(words)
print(python_count)
