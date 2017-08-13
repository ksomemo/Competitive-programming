import sys

def input_str():
	return input().strip('\n')

def input_str_l(sep=None):
	return input_str().split(sep)

def input_int_l(sep=None):
	return map(int, input_str_l(sep))

N, Q = input_int_l()
par = list(range(N))
i_l_list = [input_int_l() for _ in range(Q)]

def root(x):
	if par[x] == x:
		return x
	par[x] = root(par[x])
	return par[x]

def same(x, y):
	return root(x) == root(y)

def unite(x, y):
	x = root(x)
	y = root(y)

	if x != y:
		par[y] = x

print(par)
for l in i_l_list:
	q_type, a, b = l
	if q_type == 0:
		unite(a, b)
		print(par, end='')
		print('concat')
	else:
		is_same = same(a, b)
		print(par, end='')
		print('judge:', end='')
		if is_same:
			print('Yes')
		else:
			print('No')

