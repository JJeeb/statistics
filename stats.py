from math import sqrt, ceil

def mean(v):
     """ 
     >>> mean([1, 3, 4.5, 5]) == (1 + 3 + 4.5 + 5) / 4.0
     True
     """
     return sum(float(e) for e in v) / len(v)


def variance(m, v):
    """
    >>> v = [1, 3, 4.5, 6.5]
    >>> m = mean(v)
    >>> (1.0 / 4) * sqrt((1 - m)**2 + (3 - m)**2 + (4.5 - m)**2 + (6.5 - m)**2)
    1.0077822185373186
    >>> variance(m, v)
    1.0077822185373186
    """
    return (1.0 / len(v)) * sqrt(sum((e - m)**2 for e in v))


def median(v):
    """
    >>> median([12, 5, 6, 89, 5, 2390, 1])
    6
    >>> median([12, 5, 6, 89, 5, 1])
    5.5
    """
    length = len(v)
    sorted_v = sorted(v)
    return sorted_v[length / 2] if length % 2 != 0 else mean([sorted_v[length/2 - 1], sorted_v[length/2]])


def quartil_1(v):
    """
    >>> v = [20, 11, 19, 24, 28, 1, 34, 37, 15, 47, 50, 57]
    >>> quartil_1(v)
    15
    """
    index = int(ceil(len(v) / 4)) - 1
    return sorted(v)[index]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
