# Create the script ​problem3.py, ​which gets ​text ​as a positional argument and prints all-lowercase and all-uppercase versions of the ​text ​in the following format:
# “The given string: ​A sAmpLe stRING.”​ “All lowercase: ​a sample string​.”
# “All uppercase: ​A SAMPLE STRING​.”



import argparse



parser = argparse.ArgumentParser()



parser.add_argument('some_text', help ='My mixed string that needs to be lowercase and uppercase',type = str)



args = parser.parse_args()



print('My text: ',args.some_text)
print('Lowercase text: ',args.some_text.lower())
print('Uppercase text: ',args.some_text.upper())

