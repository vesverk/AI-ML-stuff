# manupilation of dict

person = {"name" : "vaibhav" , "age" : 20}

if "age" in person:
    del person["age"]

print(person)


def reverse_and_remove_duplicates(lst):
    lst = lst[::-1]
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 1]

print("Original List:", numbers)
print("Result:", reverse_and_remove_duplicates(numbers))