function main()
    """ver. 0.5.0

    ref:
        https://qiita.com/phigasui/items/2db20b36fb85e161e0ae
        https://nbviewer.jupyter.org/github/bicycle1885/Julia-Tutorial/blob/master/Julia%E3%82%AF%E3%83%83%E3%82%AF%E3%83%96%E3%83%83%E3%82%AF.ipynb
        https://nbviewer.jupyter.org/github/bicycle1885/Julia-Tutorial/blob/master/Julia%E9%AB%98%E9%80%9F%E3%83%81%E3%83%A5%E3%83%BC%E3%83%88%E3%83%AA%E3%82%A2%E3%83%AB.ipynb
    """
    const S = readline() |> chomp
    const ans = f(S)

    @assert ans == ans
    println(ans)
end

function f(S::String)
    const n = length(S)
    # Int: Int64
    const aa = zeros(Int, n)
    const cc = zeros(Int, n)
    const q = [0 for _ = 1:n]
    aa[1] = convert(Int, S[1] == 'A')
    cc[1] = convert(Int, S[1] == 'C')
    q[1]  = convert(Int, S[1] == '?')
    for i = 2:n
        aa[i] = aa[i - 1] + Int(S[i] == 'A')
        cc[i] = cc[i - 1] + Int(S[i] == 'C')
        q[i]  = q[i - 1]  + Int(S[i] == '?')
    end

    ans = 0
    const MOD = 10^9 + 7
    for i = 2:n - 1
        a = aa[i - 1]
        c = cc[n] - cc[i]
        l = q[i - 1] 
        r = q[n] - q[i]
        # ABC の作り方
        # AB?: ? 1つをCに割り当てる
        # ?BC: ? 1つをAに割り当てる
        # ?B?: ? 2つをACに割り当てる
        if S[i] == 'B' || S[i] == '?'
            ac = a * c * powermod(3, l + r, MOD)
            (aq, qc, qq) = (0, 0, 0)
            if l + r - 1 >= 0
                p = powermod(3, l + r - 1, MOD)
                aq = a * r * p
                qc = l * c * p
            end
            if l + r - 2 >= 0
                qq = l * r * powermod(3, l + r - 2, MOD)
            end
            # println(a, c, l, r, (ac, aq, qc, qq))
            ans += ac + aq + qc + qq
            ans = ans % MOD
        end
    end

    return ans
end

main()
