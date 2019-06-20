"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#assigns the words what,does,this,line,do,? to "some_words"
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #define list aswaht, does, this, line, do, ?
#all words in the function sonme_word will be printed
for word in some_words:
    print(word) #prints all the words in some_words
#will do the same as the previous command
for x in some_words:
    print(x) #prints all the words in some_words
#prints all words in some_words all at once
print(some_words) #prints the function out again aka ['what', 'does', 'this', 'line', 'do', '?']
#if length of the string is greater than 3 then print some_words contains more than 3 words
if len(some_words) > 3:
    print('some_words contains more than 3 words') #the if statement was correct, so it was printed
#reset usefulFuntion to have no words in it's list
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()#prints out computer specs prints the platform information
