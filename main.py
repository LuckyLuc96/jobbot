## This is my crude way to make the process of applying for one off jobs technically repeatable and something that can be done over and over. I will refine this.
import time
num_attempts = int(input("How many applictions are you trying for?\n"))
counter = 0

while num_attempts > counter:
    counter = counter + 1
    remaining = num_attempts - counter
    print(f"There are {remaining} remaining attempts.")
    time.sleep(3)
