import sys

def input_str():
    return input().strip('\n')

def input_int():
    return int(input_str())

def input_str_l(sep=None):
    return input_str().split(sep)

def input_int_l(sep=None):
    return list(map(int, input_str_l(sep)))

def input_str_l_all(sep=None):
    return [l.strip('\n').split(sep) for l in sys.stdin]

def input_int_l_all(sep=None):
    return [list(map(int, l.strip('\n').split(sep))) for l in sys.stdin]

