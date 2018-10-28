namespace MySpace
{
    public class MyClass
    {
        // https://twitter.com/meguru_comp/status/694207919517077504
        // https://twitter.com/meguru_comp/status/694547019885449216
        long mod = Math.pow(10, 9) + 7;

        /// <summary>
        /// コンビネーションの計算
        /// 愚直に計算するパターン
        /// かけた結果と割った結果を愚直に計算。最後に割った結果の逆元をかける
        /// 事前計算不要、O(b + log(mod))
        /// </summary>
        long getC_large(int a, int b)
        {
            long ans = 1;
            if (b > a / 2) return getC(a, a - b);
            long div = 1;
            for (int i = 0; i < b; i++)
            {
                ans *= a - i;
                ans %= mod;
                div *= i + 1;
                div %= mod;
            }
            ans *= powmod(div, mod - 2);
            return ans % mod;
        }

        // 階乗
        long[] fact;
        // 階乗の逆元
        long[] revFact;

        /// <summary>
        /// powmodといったら逆元
        /// 階乗と階乗の逆元を O(N + log(mod)) で求める
        /// <summary>
        void setFact(int N)
        {
            fact = new long[N];
            fact[0] = 1;
            for (int i = 1; i < N; i++)
            {
                fact[i] = fact[i - 1] * i;
                fact[i] %= mod;
            }

            revFact[N - 1] = pwmod(fact[N - 1], mod - 2);
            for (int i = N - 2; i >= 0; i--)
            {
                revFact[i] = revFact[i + 1] * (i + 1);
                revFact[i] %= mod;
            }

        }

        /// <summary>
	    /// 階乗の事前計算によるコンビネーションの計算
        /// 要setFact
        /// aCb = a! / (b! * (a - b)!) を使ってO(1)で求める方法
        /// 構築O(N),呼び出しO(1), N<=10^7
        /// </summary>
        long getC_medium(int a, int b)
        {
            long x = fact[a] * revFact[b] % mod;
            return x * revFact[a - b] % mod;
            // return (((fact[a] * revFact[b]) % mod) * revFact[a - b]) % mod;
        }

        /// <summary>
        /// パスカルの三角形によるコンビネーションの計算
        /// a段目b列目(0-indexed) = aCb になることを利用
        /// 構築O(N^2) 呼び出しO(1)  N>=3000
        /// </summary>
        void setPascal(int N)
        {
            C = new long[N, N];
            for (int i = 0; i < N; i++)
            {
                C[i, 0] = 1;
                for (int j = 1; j <= i; j++)
                {
                    C[i, j] = C[i - 1, j] + C[i - 1, j - 1];
                    if (C[i, j] >= mod) C[i, j] -= mod;
                }
            }
        }

        /// <summary>
        /// 累乗よりもbit演算のほうがかなり早いらしい
        /// </summary>
        long powmod(long a, long p)
        {
            long ans = 1;
            long mul = a;
            for (; p > 0; p >>= 1, mul = (mul * mul) % mod)
            {
                if ((p & 1) == 1)
                {
                    ans = (ans * mul) % mod;
                }
            }
        }
    }
}
