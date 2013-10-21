class Factorial {
public:
	int fact(int n) {
		if (n <= 1) return 1;
		return n * this->fact(n - 1);
	}
};

