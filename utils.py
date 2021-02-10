import re
import string
import random
from config import FILE_ONE_TO_WRITE, FILE_TWO_TO_WRITE


def random_string_generator():
    random_str_list = [random.choice(string.ascii_uppercase+' '), 'CDS']
    r_str = ' '.join(random.choice(random_str_list) for _ in range(random.choice(range(100, 200))))
    return r_str


def random_choice(list_of_choice):
    return random.choice(list_of_choice)


def file_write(file_path, content):
    with open(file_path, 'a') as file_obj:
        file_obj.write(content)


def file_reader(file_path):
    with open(file_path, 'r+') as file_obj:
        content = file_obj.read()
    return content


def count_word(content, keyword):
    count = len(re.findall(r'(?<!\S)' + keyword + r'(?!\S)', content))
    return count


def random_writer():
    random_string = random_string_generator()
    file = random_choice([FILE_ONE_TO_WRITE, FILE_TWO_TO_WRITE])
    file_write(file, random_string)