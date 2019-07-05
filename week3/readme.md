TODO: Reflect on what you learned this week and what is still unclear.
This stuff is hard :/
import random

def not_number_rejector(message):
    while True:
        try: 
            value = int(value)
            return value
        except:
            value = input(message)
#this code is to make sure the values are number values
not_number_rejector is the command variable to make sure the input typed is a number and not letters
in ex3, it is used instead of int() because it is our new int() command with more features