# #file handlaing

# # import os


# # with open("sample.txt" , "r") as file:
# #     content = file.read()
# #     print(content)


# # with open("sample1.txt" , "w") as file:
# #     file.write("hello world")
# #     file.writelines(["aline" , "bob"])


# # with ensure the file are proparly closed after the operation even an error occured

# #exception handaling 
# # try - expect block

# try:
#     with open("sample.txt" , "r") as file:
#         content  = file.read()
# except FileNotFoundError:
#     print("file not found")


# # ex 1:
# def count_words(filename):
#     try:
#         with open(filename, "r") as file:
#             lines = file.readline()
#             line_count = len(lines)
#             word_count = sum(len(line.split()) for line in lines)
#     except FileNotFoundError:
#         print("file not found") 


#ex 2: write and read the list of item
 
def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")

def read_item_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.read()
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print("file not found")


fruits = ["apple" , "tomato"]

write_item_to_file("sample2.txt", fruits)
read_item_from_file("sample2.txt")