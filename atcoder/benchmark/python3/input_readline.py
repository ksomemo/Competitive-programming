import sys
import time
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    sub = parser.add_subparsers()

    sys_parser = sub.add_parser('sys')
    input_parser = sub.add_parser('input')
    data_parser = sub.add_parser('data')

    sys_parser.set_defaults(func=benchmark_sys_readline)
    input_parser.set_defaults(func=benchmark_input)
    data_parser.set_defaults(func=echo_data)

    args = parser.parse_args()
    args.func(args.p)


def echo_data(p):
    for x in range(10 ** p):
        print(x)


def benchmark_sys_readline(p):
    """
    % python input_readline.py 7 data | time python input_readline.py 7 sys
    start p=7, sys
    end p=7, sys: 7533.890008926392
    python input_readline.py 7 sys  4.73s user 0.23s system 62% cpu 7.889 total
    """
    t = time.time()
    print("start p={}, sys".format(p))
    for _ in range(10 ** p):
        _ = sys.stdin.readline().strip()
    t_diff = (time.time() - t) * 1000
    print("end p={}, sys: {}".format(p, t_diff))


def benchmark_input(p):
    """
    % python input_readline.py 7 data | time python input_readline.py 7 input
    start p=7, input
    end p=7, input: 56780.75075149536
    python input_readline.py 7 input  43.77s user 12.71s system 98% cpu 57.133 total
    """
    t = time.time()
    print("start p={}, input".format(p))
    for _ in range(10 ** p):
        _ = input()
    t_diff = (time.time() - t) * 1000
    print("end p={}, input: {}".format(p, t_diff))


if __name__ == '__main__':
    main()
