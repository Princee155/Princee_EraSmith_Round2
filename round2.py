import random
from array import *

MAX_LEN = int(input("\nEnter maximum length of the password = "))

#taking input
input_string1 = input("\nEnter some digits separated by comma = ")
DIGITS  = input_string1.split(",")

input_string2 = input("\nEnter some lower case characters separated by comma = ")
LOCASE_CHARACTERS  = input_string2.split(",")

input_string3 = input("\nEnter some upper case characters separated by comma = ")
UPCASE_CHARACTERS  = input_string3.split(",")

input_string4 = input("\nEnter some SYMBOLS separated by comma = ")
SYMBOLS  = input_string4.split(",")

#combining above arrays
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# random selection
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
 
# combine randomly selected characters
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
  
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    
print("\n")
print("Generated Password is as follows : ")
print(temp_pass)