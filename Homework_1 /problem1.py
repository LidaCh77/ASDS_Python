import argparse




parser = argparse.ArgumentParser()

parser.add_argument('text', help = 'some text', type = str)
parser.add_argument('first_word', help = 'text', type = str)
parser.add_argument('second_word', help = 'image', type = str)



arguments = parser.parse_args()



print('The given text: ', arguments.text)
print('First word: ', arguments.first_word)
print('First word: ', arguments.second_word)
print('Output string: ',arguments.text.replace( arguments.first_word,arguments.second_word))      






