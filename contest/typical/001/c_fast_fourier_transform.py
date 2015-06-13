def input_str():
	return input().strip('\n')

def input_int():
	return int(input_str())

def input_str_l(sep=None):
	return input_str().split(sep)

def input_int_l(sep=None):
	return map(int, input_str_l(sep))

N = input_int()
mains = []
subs = []
for m, s in [input_int_l() for _ in range(N)]:
	mains.append(m)
	subs.append(s)

def multiply(g, h):
    f = [0 for _ in range(len(g) + len(h)- 1)]
    for i in range(len(g)):
        for j in range(len(h)):
            f[i+j] += g[i] * h[j]
    return f

answers = multiply(mains, subs)
print(0)
print('\n'.join(map(str, answers)))
