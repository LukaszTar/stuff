from tkinter import *


def regex_search(file_content, pattern):
    search_result = ''
    file_content = file_content.splitlines()
    my_regex_pattern = pattern.rstrip()
    regex = re.compile(my_regex_pattern)
    for line in file_content:
        match = regex.search(line)
        if match:
            search_result += line + '\n'
    return search_result
