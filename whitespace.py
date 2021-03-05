import argparse
from pathlib import Path
import re

parser = argparse.ArgumentParser(description='Whitespace.py code compiler/decompiler')
parser.add_argument('mode', type=str, choices=('compile', 'decompile'))
parser.add_argument('filename', type=str, help='Name of the input file')
parser.add_argument('--character', '-c', type=str, help='Character that will be the basis for the whitespace code', default=' ')
parser.add_argument('--delimiter', '-d', type=str, help='inserted between the whitespace. Only used in compile mode.', default='a')

args = parser.parse_args()
input_filename = Path(args.filename)
output_file_extension = '.whitespace' if args.mode == 'compile' else '.py'
with input_filename.open('r') as input_file, input_filename.with_suffix(output_file_extension).open('w') as output_file:
    if args.mode == 'compile':
        for line in input_file:
            print(args.character)
            # Take each letter in the line and convert it to a number using ord.
            # Then multiply it with args.character to make a long string of the same character.
            # line.rstrip is included to ignore the \n at the end of the line
            output_file.write(''.join(ord(decoded_char) * args.character + args.delimiter for decoded_char in line.rstrip('\n')))
            output_file.write('\n')

    elif args.mode == 'decompile':
        for line in input_file:
            # Split the line into segments where there are characters that are not args.character
            # Ignore \n at the end of the line
            encoded_characters = re.split(f'[^{args.character}]+', line.rstrip('\n'))
            # Remove the '' that is created from re.split when a non-args.character is at the end of the line
            encoded_characters.remove('')
            # chr is the opposite of ord, i.e. it converts a number to a letter.
            decoded_line = ''.join(chr(len(whitespace_chr)) for whitespace_chr in encoded_characters)
            output_file.write(decoded_line + '\n')
