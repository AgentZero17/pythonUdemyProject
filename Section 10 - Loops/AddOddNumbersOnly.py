from random import choice, randint
number = randint(0, 1000)
number = int(number)


sum_ofOdds = 0
sum_ofEven = 0
print(f"All odd numbers from 0 - {number} ")

for num in range(number+1):
    if num % 2 == 1:
        sum_ofOdds = sum_ofOdds + num
    else:
        sum_ofEven = sum_ofEven + num

print(f"Sum of odd numbers  between 0 - {number} is : {sum_ofOdds}")
print(f"Sum of even numbers  between 0 - {number} is : {sum_ofEven}")