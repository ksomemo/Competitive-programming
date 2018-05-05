# benchmark
## reference
<http://www.itmedia.co.jp/enterprise/articles/0908/22/news001.html>

## 全探索の限界
### 全通り
`2^26 < 10^8 < 2^27`

```python
m = 10 ** 8
for i in range(32):
    print(i, 2 ** i, 2 ** i < m, sep="\t")
```

### 全並べ方
`11! < 10^8 < 12!`

```python
m = 10 ** 8
for i in range(15):
    x = math.factorial(i)
    print(i, x, x < m, sep="\t")
```