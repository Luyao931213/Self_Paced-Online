#!/usr/bin/env python3
# katafourteen.py
# Coded by LouReis

# Take a text file as input and for each set of 3 words, make the first two words keys.

print('This program takes a file and creates a dictionary.\n')
print('Here are the files you have to choose from in this directory:\n\n')
import pathlib
pth = pathlib.Path('./')
# pth.is_dir()
pth.absolute()
# The above command should return: PosixPath('/home/america/gitrepo/Self_Paced-Online/students/LouReis/Lesson04')
for f in pth.iterdir():
    print(f)

# Prompt the user to specify a text file to process.
filename = input("Please enter a filename: \n\n")
print("You chose:", filename)
# The following lines open the text file & process it creating keys, values for a dictionary.
kata = {}
count = 1
key = ''
value = []
with open(filename,'r') as f:
    for line in f:
        for word in line.split():
            if count == 1:
                key = word
                count = count + 1
            elif count == 2:
                key = key + ' ' + word
                count = count + 1
            elif count == 3:
                if key in kata:
                    value = [word]
                    kata[key] = kata[key] + [word]
                    value = []
                    count = 1
                    key = ''
                else:
                    kata.update({key:[word]})
                    count = 1
                    key = ''
for k, v in kata.items():
    print(k, "=>", v)

"""
The output from the following line of text should be as follows:

I wish I may I wish I might

You might generate:

"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]

"""
