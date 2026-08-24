s = "hello123"
vowels=0
consonants=0
digits=0

for ch in s:
    if ch in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
 
print("Vowels",vowels)
print("Consonants",consonants)
print("Digits",digits)