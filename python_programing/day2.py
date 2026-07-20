# check if no is prime no or not

num = int(input("enter the number: "))

if num>1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(f"the {num} is not a prime no ")
            break
    else:
        print(f"the {num} is prime no")
else:
        print("the no is not a prime no")

#  to fine the largest no in a list using a loop

numbers = (1,2,3,4,54)

result = max(numbers)
print(result)


# to find factorial of a number

number = int(input("enter the number: "))

factoial = 1

while number > 0:
    fact *= number
    number -= 1

