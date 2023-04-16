import os
import docx2txt
import re
import sys

# Function that counts the number of words, the number of characters with spaces, and the number of punctuation marks in a docx file
def count_words_chars_punctuation(filepath):
    content = docx2txt.process(filepath)
    word_count = len(content.split())
    char_count_with_spaces = len(content)
    char_count_without_spaces = len(content.replace(' ', ''))
    punctuation_count = len(re.findall(r'[^\w\s]', content))
    return word_count, char_count_with_spaces, char_count_without_spaces, punctuation_count

file_path = sys.argv[1]
word_count, char_count_with_spaces, char_count_without_spaces, punctuation_count = count_words_chars_punctuation(file_path)

print(f'The number of words in the file {file_path}: {word_count}')
print(f'The number of characters with spaces in the file {file_path}: {char_count_with_spaces}')
print(f'The number of characters without spaces in the file {file_path}: {char_count_without_spaces}')
print(f'The number of punctuation marks in the file {file_path}: {punctuation_count}')
