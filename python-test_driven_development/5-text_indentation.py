"""
indent text
"""

def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for c in range(len(text)):
        line += text[c]
        if text[c] in ".?:":
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end='')
