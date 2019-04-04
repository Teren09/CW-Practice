def maskify(cc):
    """masks all symbols except last 4"""
    sliced_string = (cc[:-4])
    censor = len(sliced_string) * "#"
    print(cc.replace(sliced_string, censor))


maskify(input('Your input: '))
