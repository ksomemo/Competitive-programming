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
	max_p = N if price > N else price
	for i in range(1, max_p+1):
		m_price = i
		s_price = price - i
		if 1 <= m_price <= max_p and 1 <= s_price <= max_p:
			type_num += mains[m_price-1] * subs[s_price-1]
	return type_num

for k in range(1, 2 * N + 1):
	type_num = f(k)
	print(type_num)

