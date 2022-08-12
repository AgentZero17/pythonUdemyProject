from random import choice, randint
number = randint(10, 100)
number = int(number)


sum = 0
sumofEven = 0
print(f"All odd numbers from 0 - {number} ")

for num in range(number+1):
    if num % 2 == 1:
        sum = sum + num
    else:
        sumofEven = sumofEven + num

print(f"Sum of odd numbers  between 0 - {number} is : {sum}")
print(f"Sum of even numbers  between 0 - {number} is : {sumofEven}")

