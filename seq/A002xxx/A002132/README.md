# A002132

> Generalized sum of divisors function.
> — [OEIS A002132](https://oeis.org/A002132)

Offset 4: 1, 2, 4, 8, 14, 18, 28, 40, 52, 70, 88, 104, …

The entry gives no definition beyond its name. The data are MacMahon's
C₂: the coefficient of qⁿ in Σ q^i/(1−q^i)² · q^j/(1−q^j)² over odd
i < j, the analogue of [A002127](../A002127/) with odd part sizes
(offset 4 = 1 + 3). This reading matches all 9997 terms of the b-file.

### Python 3 — 122 bytes

```python
r=[1]
for n in r:r+=n+1,;n<4or print(sum(u//i*(n-u)//j for i in r[::2]for u in range(i,n,i)for j in r[i+1::2]if(n-u)%j<1))
```

**How it works**

- q^i/(1−q^i)² = Σ_{x≥1} x·q^(x·i), so a(n) is the sum of x·y over odd
  sizes i < j and multiplicities x, y ≥ 1 with x·i + y·j = n.
- `r` is the list being looped over, and each pass appends n+1 to it, so
  the `for` never ends and r holds 1, …, n+1 (the loop of
  [A000203](../../A000xxx/A000203/)). `r[::2]` is 1, 3, 5, …, and
  `r[i+1::2]` is i+2, i+4, …, the odd sizes j > i. u = x·i runs over the
  multiples of i below n, `if(n-u)%j<1` keeps the j dividing n − u, and
  the weight `u//i*(n-u)//j` is x·y (exact: j divides n − u).
- `n<4or print(…)` skips n = 1, 2, 3: the offset is 4.

**Notes**

- Integer arithmetic only, so it is correct for every n.
- A term costs about n²·ln n/4 steps. The b-file has 9997 terms; the bar
  is 620 terms in 60 s, about 20 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 122 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002132), CC BY-SA 4.0.
