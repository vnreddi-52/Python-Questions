# file = open("practice1_1.py","w")

# file.write("from datetime import datetime \n"
# "date_today = datetime.now() \n"
# "print(date_today)")
# file.close()

# file =open("practice1_1.py","a")
# file.write("added a new line")
# file.close()

# file = open("practice1_1.py","r")
# content = file.read()
# print(content)

# Delete operation

import os
# os.unlink("x.txt")
# os.remove("xx.txt")

# if os.path.exists("hello.txt"):
#     os.remove("hello.txt")
# else:
#     print("File not founc")

# delete an empty folder
os.rmdir("New_Folder")
# delete folder and everything inside it
# import shutil
# shutil.rmtree("New_Folder")
