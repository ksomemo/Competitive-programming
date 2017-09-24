class Fib {
public:
	int fibonacciNumber(int n) {
		if (n <= 1) return n;
		return this->fibonacciNumber(n - 1) + this->fibonacciNumber(n - 2);
	}
};

