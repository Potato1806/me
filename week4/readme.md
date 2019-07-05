TODO: Reflect on what you learned this week and what is still unclear.

#dictionary
my_dict = {"key": "value"} #use {} to define dictionary
my_dict["key"] #use [] to access dictionary
my_dict["name"] = Mark #another way to define

my_dict["degrees"] = {"something": "else", "wow":0}
my_dict["degrees"]["everything"] = [1, 2, 3, 4]
my_dict["key"]

[] to open a list
if there are nested lists, use [][] to open the list and then the list inside
to obtain a value in the list, use [0] to get the first term in the list, [1] for the second and so on
json is the internet version of a dictionary

http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=10  (defines condition)   &maxLength=1   (defines another condition)   &limit=1  (defines another condition)
? signals start of search and conditions
& signals additional condition

template = "http...
url = ...
r = request get(url)
if r.status_code == 200
    the_jsom = jsom.loads(r.texts)
    abil = the.jsom["abilities"]



append into a list