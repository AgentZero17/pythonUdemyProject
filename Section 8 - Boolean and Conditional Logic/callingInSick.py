# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE
if sick_days:
    if actually_sick:
        calling_in_sick = True
        print(f"Actually sick:{actually_sick}")
        print(f"You have {sick_days} days available")
        sick_days = sick_days - 1
        print(f"You are calling sick today. You have {sick_days} sick days remaining")
    elif kinda_sick and hate_your_job:
        print(f"Kinda sick:{kinda_sick}")
        print(f"Hate your job:{hate_your_job}")
        calling_in_sick = True
        print(f"You have {sick_days} days available")
        sick_days = sick_days - 1
        print(f"You are calling sick today. You have {sick_days} sick days remaining")
    else:
        print(f"Kinda sick:{kinda_sick}")
        print(f"Hate your job:{hate_your_job}\n")

        print(f"You are not calling off today.\n")
        sick_days = sick_days - 1

else:
    calling_in_sick = False
    print(f"You have {sick_days} sick days available. You wont be able to calling sick!!")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
