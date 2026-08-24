# Code 1 - Without Custom Exception
 
entriesList = list(map(int, input().split()))
 
class EmptyLogError(Exception):
    pass
 
def show_log(entries):
    if not entries:
        print("No log entries to display.")
    for entry in entries:
        print(entry)
try:
    show_log(entriesList)
except EmptyLogError as e:
    print(f"Error: {e}")

# Code 2 - With Custom Exception

# entries_list = list(map(int,input().split()))
# class EmptyLogError(Exception):
#     pass

# def show_log(entries):
#     if not entries:
#         raise EmptyLogError("No log entries to display")
#     for entry in entries:
#         print(entry)

# try:
#     show_log(entries_list)
# except EmptyLogError as e:
#     print(f"Error: {e}")

# print(show_log(entries_list))