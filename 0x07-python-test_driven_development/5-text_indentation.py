#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these 
characters: ., ? and :"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ''
    i = 0
    while i < len(text):
        string += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            string = string.strip()
            print(string)
            print()
            try:
                if text[i + 1] == ' ':
                    i += 1
            except IndexError:
                pass
            string = ''
        i += 1

    if len(string) > 0:
        print(string, end='')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
