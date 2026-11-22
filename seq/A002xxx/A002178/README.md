# A002178

> Numerators of Cotesian numbers (not in lowest terms): A002176*C(n,1).
> — [OEIS A002178](https://oeis.org/A002178)

Offset 1: 1, 4, 3, 32, 75, 216, 3577, 5888, 15741, 106300, 13486539, …

### Python 3 — 213 bytes

```python
from math import*
n=f=1
while 1:r=range(n+1);M=f*n+f;K=n*len(bin(n));B=1<<K;L=[sum((P>>K*i&B-1)*(M:=-M)//~i for i in r)*comb(n,k)for k in r if[P:=prod(j+n*B for j in r if j-k)]];print(L[-2]//gcd(M*f,*L));n+=1;f*=n
```

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
- **Signs and the symmetric node.** `(M:=-M)` flips M at every digit, and
  `//~i` divides by −(i + 1); this gives the (−1)^i, and because the flips
  run on across the k loop, `L[k]` equals the true numerator times
  (−1)^(nk). For k = 1 that would be (−1)^n, so the program reads
  k = n − 1 instead: the substitution t → n − t maps node k to node n − k,
  so C(n,1) = C(n,n−1), and (−1)^(n(n−1)) = +1 because n(n−1) is even.
  `L[-2]` is therefore A002176(n)·C(n,1) times g, with the right sign for
  every n, without assuming the weight is positive. For n = 1 it is
  `L[0]`, and C(1,0) = C(1,1) = 1/2.
- `M*f` in the gcd is read after the comprehension, when M may be
  −(n+1)!; `gcd` ignores signs.

**Notes**

- The b-file is the entry's 21 terms (n = 1 to 21), the bar, in a fraction
  of a second; the program keeps going (100 terms in about 7 reference
  seconds, as for A002177).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 213 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002178), CC BY-SA 4.0.
