import time

Rows = input("How many rows would you like for the star pattern? \n")

print("Loading algorithim...")
time.sleep(1)

print("Getting ready...")
time.sleep(1)

print("Getting ready to print...")
time.sleep(1)

starmain = "*"

for i in range(int(Rows)):
    space = " " * (int(Rows) - i - 1)
    stars = starmain * (2 * i + 1)
    print(space + stars + space)
    time.sleep(0.1)

print("Star Pattern finished! Closing in 3 seconds.")

print(1)
time.sleep(1)

print("2...")
time.sleep(1)

print("Goodbye!")
time.sleep(1)