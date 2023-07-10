"""
indent text
"""

def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    replaced_text = text.replace(":", ".\n\n").replace(".", ".\n\n").replace("?","?\n\n")

    print(replaced_text)
