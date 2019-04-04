def square_digits(num):
    """Takes a number, returns a new number with each inputted number squared
    result = [int(x) ** 2 for x in str(num)]
    return [print(x, end='') for x in result] - this is also an option"""
    new_list = []
    for x in str(num):
        new_list.append(int(x) ** 2)
    return int(''.join(map(str, new_list)))


print(square_digits(9119))
