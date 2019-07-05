# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    ranger = []
    while stop > start:
        ranger.append(int(start))
        start = start + step
    return ranger



def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    sth = []
    while stop > start:
        sth.append(int(start))
        start = start + step
    return sth


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    two_step_ranger = []
    step = 2
    while stop > start:
        two_step_ranger.append(int(start))
        start = start + step
    return two_step_ranger
   


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    lower = int(low)
    higher = int(high)
    bound = False

    while not bound:
        guess = int(input())
        if guess > higher:
            print('ded')
        elif guess < lower:
            print('ded')
        else:
            bound = True
            print('Noice')
    return guess

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    import random

def not_number_rejector(message):
    while True:
        try: 
            value = int(value)
            return value
        except:
            value = input(message)


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    print("Guess a number!")
    lower_bound = int(low)
    higher_bound = int(high) 
    bounded = False 

    while not bounded:
        guess = str(input("Guess A Number: "))
        if guess.isdigit():
            if int(guess) < lower_bound:
                    print ("Higher Lad")
            elif int(guess) > higher_bound:
                    print ("Lower Mate")
            else:
                    bounded = True
                    print("Wrong... Jokes")
        else:
            print("Definitely Wrong")
    return guess


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
