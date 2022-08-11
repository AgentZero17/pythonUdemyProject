print("How many kilometers did you cycle today?")
kms = float(input())

print(f"Ok, you said {kms} kilometers")

convertToMile = kms / 1.60934

print(f"You cycled {round(convertToMile,2)} miles")
