# A002128

> MacMahon's generalized sum of divisors function.
> — [OEIS A002128](https://oeis.org/A002128)

Offset 6: 1, 3, 9, 22, 42, 81, 140, 231, 351, 551, 783, 1134, …

### Python 3 — 128 bytes

```python
f=lambda n,k=3,j=1:sum(e//i*f(n-e,k-1,i+1)for i in range(j,n+1)for e in range(i,n+1,i))if k else n<1
n=6
while[print(f(n))]:n+=1
```

**How it works**

- MacMahon's function is the coefficient of qⁿ in
  Σ_{0<i<j<l} q^i/(1−q^i)² · q^j/(1−q^j)² · q^l/(1−q^l)², and
  q^i/(1−q^i)² = Σ_{x≥1} x·q^(x·i). So a(n) sums x·y·z over partitions
  of n with exactly three part sizes, used x, y and z times (the entry's
  "three designated summands": one copy of each size is marked).
- `f(n,k,j)` is that weighted count with k sizes, all at least j: the
  smallest size i ≥ j takes e = x·i ≤ n with weight `e//i` = x, and the
  rest is n − e with k − 1 sizes above i. With k = 0 only n = 0 is left,
  which `n<1` counts (n − e is never negative).
- `f(n)` = f(n, 3, 1); the loop starts at the offset, n = 6 = 1 + 2 + 3,
  and `while[print(…)]:` prints before each step.

**Notes**

- Integer arithmetic only, so it is correct for every n; the recursion is
  only three levels deep.
- A term costs about (n·ln n)³/6 calls. The b-file has 9995 terms; the
  bar is 100 terms in 60 s, about 20 s here. The same recursion with two
  sizes gives [A002127](../A002127/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 128 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002128), CC BY-SA 4.0.
