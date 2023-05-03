# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def mutate_string(string,position,character):
    # since we have the position and the character as input we can print the string by joining the part before the wanted index then the character then the part after the wanted index.
    print(string[:position]+character+string[position:])
# we have to create the variables (string1,index,character1)
string1= "abracadabra"
index = 5
character1="k"
#running the function (mutate_string) to add the character into the specified index
mutate_string(string1,index,character1)
