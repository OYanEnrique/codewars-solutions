'''
Complete the function that accepts a string parameter,
and reverses each word in the string.
All spaces in the string should be retained.
Examples:
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text:str) -> str:
    final = ""
    placeholder = ""
    for char in text:
        if char.isspace():
            final += placeholder[::-1]
            final += char
            placeholder = ""
        else:
            placeholder += char
    final += placeholder[::-1]
    return final