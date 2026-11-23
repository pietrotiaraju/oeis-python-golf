# A002179

> Numerators of Cotesian numbers (not in lowest terms): A002176*C(n,2).
> — [OEIS A002179](https://oeis.org/A002179)

Offset 2: 0, 1, 3, 12, 50, 27, 1323, −928, 1080, −48525, −3237113, …

### Python 3 — 217 bytes

```python
from math import*
n=f=1
while 1:r=range(n+1);M=f*n+f;K=n*len(bin(n));B=1<<K;L=[sum((P>>K*i&B-1)*(M:=-M)//~i for i in r)*comb(n,k)for k in r if[P:=prod(j+n*B for j in r if j-k)]];print([*L,0][2]//gcd(M*f,*L));n+=1;f*=n
```

**Offset.** The entry's offset is 2, but its terms are A002176(n)·C(n,2)
for n = 1, 2, 3, …: the first term is 0 because there is no node 2 when
n = 1 (the entry's PARI `nk(n,k)` returns 0 for k > n), then 1 for
Simpson's rule (1, 4, 1)/6, 3 for the 3/8 rule (1, 3, 3, 1)/8 and 12 for
Boole's rule (7, 32, 12, 32, 7)/90. The program follows the data: it
starts at n = 1 and its m-th line is A002176(m)·C(m,2), which the b-file
lists at index m + 1.

**How it works**

- **Same core as [A002176](../A002176/) and [A002177](../A002177/).** For
  the closed Newton–Cotes rule on nodes 0, …, n,
  C(n,k) = (−1)^k·binom(n,k)/n! · ∫₀¹ ∏_(j≠k) (j − nx) dx. The node
  polynomial ∏_(j≠k) (j + ny) is packed into one integer in base
  B = 2^K, K = n·len(bin(n)): its coefficients are nonnegative and sum to
  at most (2n)!/n! < (2n)ⁿ < B, so they are exactly its base-B digits,
  read back with `P>>K*i&B-1`. With M = (n+1)!, Σ_i (−1)^i·d_i·M/(i + 1)
  is M times the integral, an integer (each i + 1 ≤ n + 1 divides M).
- **The list.** `L[k]` is ±binom(n,k) times that sum, so
  C(n,k) = ±L[k]/Q with Q = (n+1)!·n!. The reduced denominator of each
  C(n,k) is Q/gcd(Q, L[k]), so their LCM is A002176(n) = Q/g with
  g = gcd(Q, L[0], …, L[n]), and A002176(n)·C(n,k) = ±L[k]/g.
- **Signs.** `(M:=-M)` flips M at every digit, and `//~i` divides by
  −(i + 1); this gives the (−1)^i of the integral, and because the flips
  run on across the k loop, `L[k]` equals the true signed numerator times
  (−1)^(nk). For k = 2 that factor is +1 for every n, so `L[2]//g` is
  A002176(n)·C(n,2) with its sign (it is negative for n = 8 and for
  n = 10 to 21 in the data).
- **n = 1.** `[*L,0][2]` appends a 0, which is read only when `L` has two
  entries, that is for n = 1, where C(1,2) = 0.
- `M*f` in the gcd is read after the comprehension, when M may be
  −(n+1)!; `gcd` ignores signs.

**Notes**

- The b-file is the entry's 21 terms (n = 1 to 21), the bar, in a fraction
  of a second; the program keeps going (100 terms in about 7 reference
  seconds, as for A002177).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 217 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002179), CC BY-SA 4.0.
