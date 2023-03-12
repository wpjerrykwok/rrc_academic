# COMP2040 Python Essentials With Data Analysis
# Topic Challenge - Module 6A - Working With TXT Files
# Wai Ping KWOK
# Create functions to read from a txt file, search and replace some lines 
# and overwrite to the original txt file
# Created on 2023 02 07
# sample .txt input:
# Amethyst #9966cc
# Apricot #fbceb1
# Aqua #00ffff
# Blond #faf0be
# sample .txt output:
# Amethyst #9966cc
# Apricot #fbceb1
# Azure #007fff
# Blond #faf0be

def read_search_in_file(txt_file_name: str,
                        word_to_search: str,
                        word_to_replace: str) -> str:
    """
    read the text file into a string, one line at a time and search for
    the line containing the word to search and replace with the word
    to replace\n
    args:
        txt_file_name (str): the name of the text file
        word_to_search (str): the word to be searched
        word_to_replace (str): the word to replace
    returns:
        modified_text (str): the string with the modified content
    """
    modified_text = ""
    with open(txt_file_name, "r") as myfile:
        for line_to_check in myfile:
            if word_to_search in line_to_check:
                modified_text += word_to_replace + "\n"
            else:
                modified_text += line_to_check
    return modified_text


def overwrite_file(txt_file_name: str, modified_text: str):
    """
    overwrite the text file with the modificed text\n
    args:
        txt_file_name (str): the name of the text file
        modified_text (str): the string containing the content
        to be written into the text file
    returns:
        empty
    """
    with open(txt_file_name, "w") as myfile:
        myfile.write(modified_text)


txt_file_name = "topic_challenge_module_6a_color_list.txt"
word_to_search = "Aqua"
word_to_replace = "Azure #007fff"
# word_to_search = "Azure"
# word_to_replace = "Aqua #00ffff"

new_text = read_search_in_file(txt_file_name, word_to_search, word_to_replace)
overwrite_file(txt_file_name, new_text)
