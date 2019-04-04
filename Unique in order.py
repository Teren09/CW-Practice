from itertools import groupby


def unique_in_order(iterable):
    """Deletes char duplicates"""
    return [i for i, _ in groupby(iterable)]



unique_in_order('AAAABBBCCDAABBB')
