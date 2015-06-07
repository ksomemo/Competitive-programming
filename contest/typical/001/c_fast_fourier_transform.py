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

def f(price):
	type_num = 0
	for i in range(1, price):
		m_price = i
		s_price = price - i
		if m_price > N or s_price > N:
			continue
		type_num += mains[m_price-1] * subs[s_price-1]
	return type_num

for k in range(1, 2 * N + 1):
	type_num = f(k)
	print(type_num)

