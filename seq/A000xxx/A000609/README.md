# A000609

> Number of threshold functions of n or fewer variables.
> — [OEIS A000609](https://oeis.org/A000609)

Offset 0: 2, 4, 14, 104, 1882, 94572, 15028134, 8378070864, …

### Python 3 — 247 bytes

```python
import math
n=0
while 1:
 R=range(2**n);V=[[0]];exec('V=[v+[a+c for a in v]for v in V for c in range(math.isqrt((n+1)**-~n)+2**n>>n)];'*n)
 print(len({tuple(f[p^s]for p in R)for f in{(*map(t.__lt__,v),)for v in V for t in v+[-1]}for s in R}));n+=1
```

**What is counted**

- A threshold function of n variables is f(x) = [w·x > t] for real weights
  w₁,…,wₙ and a threshold t; "n or fewer" means that f may ignore some
  inputs, so a(n) counts all of them on {0,1}ⁿ, constants included. Every
  threshold function has a realization with integer weights.
- Weight bound (Muroga, Toda and Takasu, 1961; Muroga, *Threshold Logic and
  Its Applications*, 1971): every threshold function of n variables has an
  integer realization with |wᵢ| ≤ (n+1)^((n+1)/2)/2ⁿ. The program uses
  B = ⌊√((n+1)^(n+1))⌋ >> n, which is that bound rounded down, computed with
  `isqrt`, so there is no floating point.
- Negating input i replaces wᵢ by −wᵢ and t by t − wᵢ. So every threshold
  function is a positive one, with all weights in 0…B, with some of its inputs
  negated.

**How it works**

- `exec` runs the doubling step n times: appending a weight c to a value list
  `v` gives `v+[a+c for a in v]`. After n steps `V` holds, for each weight
  vector in {0,…,B}ⁿ, the list of the 2ⁿ sums w·x, indexed by x read as a
  binary number. `math.isqrt((n+1)**-~n)+2**n>>n` is B + 1.
- For one list v the functions [v > t] for all integers t are the cuts at
  the values of v (t = max gives the constant 0) and t = −1 (the constant 1,
  since every sum is ≥ 0). `(*map(t.__lt__,v),)` is the truth table as a
  tuple; the inner set holds the distinct positive threshold functions.
- `f[p^s]` is f with the inputs in the mask s negated, so the outer set is
  every threshold function of n variables, and its size is a(n).

**Notes**

- Correctness for every n rests on the Muroga–Toda–Takasu weight bound
  above; the enumeration itself is exhaustive and exact.
- There are (B+1)ⁿ weight vectors: 7⁵ = 16 807 lists for n = 5 (about 4 s),
  but 15⁶ ≈ 11 million lists of 64 sums for n = 6, and its 15 028 134 truth
  tables would not fit in memory either. The bar is the 6 terms n = 0 to 5 in
  60 s; the b-file has 10 (n = 0 to 9).
- The same frame gives [A000615](../A000615/) (exactly n variables), and with
  sorted weights [A000617](../A000617/) and [A000619](../A000619/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 247 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000609), CC BY-SA 4.0.
