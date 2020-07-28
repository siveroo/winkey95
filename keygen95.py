import random

print("How many keys do you want to be generated?")
value = input("")

def generate(val):
    for i in range(0, val):
        key1 = random.randint(0, 999)
        key2 = random.randint(0, 9999999)
        while (key2 % 7 != 0):
            key2 = random.randint(0, 9999999)
        print('{:03}'.format(key1) + "-" + '{:07}'.format(key2))

#Filter the input (integer only)
try:
    val = int(value)
    if (val > 0):
        generate(val)
    else:
        print("Error : Input is not a positive integer!")
except ValueError:
    print("Error : Input is not a positive integer!")