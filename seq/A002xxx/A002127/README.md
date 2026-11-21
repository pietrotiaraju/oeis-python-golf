# A002127

> MacMahon's generalized sum of divisors function.
> — [OEIS A002127](https://oeis.org/A002127)

Offset 3: 1, 3, 9, 15, 30, 45, 67, 99, 135, 175, 231, 306, …

### Python 3 — 114 bytes

```python
r=[1]
for n in r:r+=n+1,;n<3or print(sum(u//i*(n-u)//j for i in r for u in range(i,n,i)for j in r[i:]if(n-u)%j<1))
```

**How it works**

- MacMahon's function is the coefficient of qⁿ in
  Σ_{0<i<j} q^i/(1−q^i)² · q^j/(1−q^j)², and q^i/(1−q^i)² = Σ_{x≥1} x·q^(x·i).
  So a(n) is the sum of x·y over the pairs of sizes i < j and
  multiplicities x, y ≥ 1 with x·i + y·j = n: partitions with exactly two
  part sizes, each weighted by the product of the multiplicities (the
  entry's "two designated summands": one copy of each size is marked).
- `r` is the list being looped over, and each pass appends n+1 to it, so
  the `for` never ends and r holds 1, …, n+1 (the loop of
  [A000203](../../A000xxx/A000203/)). u = x·i runs over the multiples of i
  below n, `r[i:]` over the sizes j > i, and `if(n-u)%j<1` keeps the j
  dividing n − u; the weight `u//i*(n-u)//j` is x·y (the second floor
  division is exact because j divides n − u).
- `n<3or print(…)` skips n = 1, 2: the offset is 3.

**Notes**

- Integer arithmetic only, so it is correct for every n.
- A term costs about n²·ln n steps. The b-file has 9998 terms; the bar
  is 440 terms in 60 s, about 20 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002127), CC BY-SA 4.0.
