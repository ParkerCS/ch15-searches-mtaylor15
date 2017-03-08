# Made changes to linear search.
# I like the way you tried to use the function here.

# Your binary search did not work.  Check corrections.  There are a bunch.  One major problem was that you had two separate list for dictionary and you mixed them up.  Another thing was that you did not reset the upper and lower limits on every word.
'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


file = open("dictionary.txt", "r")
dictionary = []
for line in file:
    dictionary.append(line.strip())
file.close()

print("---Linear Search---")


'''
list = []
def check(file_name):
    file = open(file_name)
    for line in file:
        words = split_line(line)
        #text_list.append(words)
        for word in words:
            key = word.upper()
            for i in range(len(dictionary)):
                #print(dictionary_list[i])
                if dictionary[i] == key:
                    break
            else:
                print(key, "not found.")
    file.close()

check("AliceInWonderLand200.txt")
print()
'''


#COULDN'T FIGURE OUT THE END OF BINARY

print("---Binary Search---")
file = open("AliceInWonderLand200.txt")
line_number = 0
upper_bound = len(dictionary) - 1
lower_bound = 0
found = False
for line in file:

    line_number += 1
    words = split_line(line)
    for word in words:
        key = word
        upper_bound = len(dictionary) - 1
        lower_bound = 0
        found = False
        while lower_bound <= upper_bound and not found:
            middle_position = (lower_bound + upper_bound) // 2

            if dictionary[middle_position] < key.upper():
                lower_bound = middle_position + 1
            elif dictionary[middle_position] > key.upper():
                upper_bound = middle_position - 1
            else:
                found = True
        if not found:
            print(word, "not found")
file.close()