from functools import reduce
import operator

a = input()
b, c = input().split(" ")
s = input()

sum = reduce(operator.add, map(int, [a, b, c]))
print(str(sum) + " " + s)

