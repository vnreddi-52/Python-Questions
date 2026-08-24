try:
    total=int(open("score.txt").read())
except FileNotFoundError:
    print("File is missing")
except ValueError:
    print("file is no answer")
else:
    print(f"Total is {total}")
finally:
    print("Done checking")