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
def check(file):
    for line in file:
        words = split_line(line)
        #text_list.append(words)
        for word in words:
            key = word.upper()
            for i in range(len(dictionary_list)):
                #print(dictionary_list[i])
                if dictionary_list[i] == key:
                    break
            else:
                print(key, "not found.")

check(file)
print()
'''


#COULDN'T FIGURE OUT THE END OF BINARY

print("---Binary Search---")
file = open("AliceInWonderLand200.txt")
list = []
line_number = 0
upper_bound = len(list) - 1
lower_bound = 0
found = False
for line in file:
    line_number += 1
    words = split_line(line)
    for word in words:
        key = word
        while lower_bound <= upper_bound and not found:
            middle_position = (lower_bound + upper_bound) // 2

            if list[middle_position] < key.upper():
                lower_bound = middle_position + 1
            else:
                found = True
file.close()