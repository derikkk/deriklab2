#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    lc = [x for x in range(n + 1) if x % 2 == 0]
    return lc
