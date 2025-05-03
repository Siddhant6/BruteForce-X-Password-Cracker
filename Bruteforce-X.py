import itertools
import string
import time

print("hello")
chars = string.printable

password = '123'  # Specify nos. max to 4 to get pass in no time

max_length = 10   # Max length Specified 

start_time = time.time()

for length in range(1, max_length +1):
    for combination in itertools.product(chars, repeat=length):
        candidate = "".join(combination)
        print("Trying password:", candidate)
        if candidate == password:
            end_time = time.time()
            print("Habibi Got Ur Password:", candidate)
            time_taken = end_time - start_time
            print("Time taken:", time_taken, "seconds")
            raise SystemExit
    
