def is_isogram(string):
    """Determines whether entered string is an isogram"""
    unique_char = ''.join(dict.fromkeys(string.lower()))
    print(unique_char)
    if string.lower() == unique_char and unique_char.isalpha() or string == '':
        print(True)
    else:
        print(False)


is_isogram('ezj')
