
# Create the script problem1.py, which gets some arguments from user using the sys module and prints the name of the script, the number of arguments and the values of the arguments in the following format:
# “Script name: problem1.py” “Number of arguments: 3” “Argument values: 1 “asd” True



import sys 

script_name = sys.argv[0]
arguments = sys.argv[1:]
number_of_arguments = len(sys.argv[1:])
print('Script name: ', script_name)
print('Number of arguments: ', number_of_arguments)
print('Argument values: ', arguments)
