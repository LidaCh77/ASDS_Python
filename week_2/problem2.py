import argparse

parser = argparse.ArgumentParser()


parser.add_argument('--age', help = 'Get the age of the user', type = int)  



args = parser.parse_args()


if args.age:
    print('Happy Birthday, you are already %d years old!' % args.age)




