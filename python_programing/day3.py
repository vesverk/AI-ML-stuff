# # create funtion to calculate factorial of a funtion

# def faactotial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * faactotial(n-1)
    

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b


#to check is no is even or odd

def num_check(n):
    if n > 0 and n%2==0:
        print(f"the {n} is even no")
    else:
        print(f"the {n} is odd no")

def print_no(n):
    result = num_check(n)

print_no(5)


# stings practive

def reverse_string(text):
    reverse = text[::-1]

def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    
    return count

def palindrome(text):
    if text == text[::-1]:
        print("the text is palindrome")
    else:
        print("not a prindrome")