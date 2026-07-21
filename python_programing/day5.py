#strings 
first = "hello"
second = "world"

result = first + second

# print(result)

# regex


import re

text = "contact me at 123-456-789"

digit = re.findall(r"\d+", text )

print(digit)

updated_text = re.sub(r"\d+" , "x" , text)
print(updated_text)

#create a text cleaner 

import re 


def clean_test(text):
    text = re.sub(r"[\w\s]" , "" , text)
    text = " ".join(text.split())
    return text.lower()

input_text = " hello     world !!! welcome to java..."
clened_Text = clean_test(input_text)
print(clened_Text)