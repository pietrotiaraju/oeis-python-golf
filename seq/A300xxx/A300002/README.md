# A300002

> Lexicographically earliest sequence of positive integers such that no k+2
> points fall on any polynomial of degree k.
> — [OEIS A300002](https://oeis.org/A300002)

Offset 1: 1, 2, 4, 3, 6, 5, 9, 16, 14, 20, 7, 15, 8, 12, 18, 31, …

As the OEIS entry notes, a(n) is the smallest positive integer that is not the
value at x = n of any polynomial interpolating a nonempty subset of the
earlier points. Both programs try all 2ⁿ⁻¹ subsets with exact arithmetic.

### Python 3 + sympy — 152 bytes

```python
from sympy import*
a=[]
while 1:n=len(a);print(v:=min({*range(1,2<<n)}-{interpolate({i:a[i]for i in range(n)if m>>i&1},n)for m in range(1,2**n)}));a+=v,
```

### Python 3 — 209 bytes

```python
from math import*
from fractions import*
a=[]
while 1:r=range(n:=len(a));print(v:=min({*range(2<<n)}-{sum(a[i]*prod(Fraction(n-j,i-j)for j in r if m>>j&(i!=j))for i in r if m>>i&1)for m in range(2**n)}));a+=v,
```

**How it works**

- Bit i of `m` says whether point i is in the subset. Points are (i, a[i])
  with x counted from 0, and the new point sits at x = n = `len(a)`.
- sympy's `interpolate` takes a dict {x: y} and returns the exact value at
  `n`. It fails on an empty dict, hence the `1,` in both ranges.
- The plain version evaluates the Lagrange formula with `Fraction`. The empty
  subset (`m=0`) sums to 0, so 0 is always forbidden and the candidate range
  can start at 0. `m>>j&(i!=j)` tests "j is in the subset and j ≠ i".
- There are at most 2ⁿ forbidden values, so `range(2<<n)` always has a free one.
- Floats are not an option: a value like 26.999999 could block a valid 27.

**Notes**

- Each term doubles the work. The plain version prints about 18 terms in
  150 s, the sympy one about 11 (sympy is shorter but much slower). The OEIS
  lists 33 terms; a(28)–a(33) were found in 2024.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 + sympy | 152 | first entry |
| 2026-11-05 | Python 3 | 209 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A300002), CC BY-SA 4.0.
