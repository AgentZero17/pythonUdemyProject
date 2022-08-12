# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================

print(f"generated food: {food}")
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food == ("apple" or "grape"):
    print("fruit")
elif food == ("bacon" or "steak"):
    print("meat")
elif food == ("dirt" or "worm"):
    print("yuck")



# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^