import sys

def input_str():
    return input().strip('\n')

def input_int():
    return int(input_str())

def input_str_l(sep=None):
    return input_str().split(sep)

def input_int_l(sep=None):
    return list(map(int, input_str_l(sep)))

