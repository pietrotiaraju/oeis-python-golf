# A002177

> Numerators of Cotesian numbers (not in lowest terms): A002176(n)*C(n,0).
> — [OEIS A002177](https://oeis.org/A002177)

Offset 1: 1, 1, 1, 7, 19, 41, 751, 989, 2857, 16067, 2171465, …

### Python 3 — 212 bytes

```python
from math import*
n=f=1
while 1:r=range(n+1);M=f*n+f;K=n*len(bin(n));B=1<<K;L=[sum((P>>K*i&B-1)*(M:=-M)//~i for i in r)*comb(n,k)for k in r if[P:=prod(j+n*B for j in r if j-k)]];print(L[0]//gcd(M*f,*L));n+=1;f*=n
```

**How it works**

- **Same core as [A002176](../A002176/).** For the closed Newton–Cotes rule
  on nodes 0, …, n, C(n,k) = (−1)^k·binom(n,k)/n! · ∫₀¹ ∏_(j≠k) (j − nx) dx.
  The node polynomial ∏_(j≠k) (j + ny) is packed into one integer with base
  B = 2^K, K = n·len(bin(n)) (its coefficients sum to at most
  (2n)!/n! < (2n)ⁿ < B, so each is a base-B digit), the digits d_i are read
  back with `P>>K*i&B-1`, and Σ_i (−1)^i·d_i·M/(i + 1) with M = (n+1)! is
  the exact integral times M. See that page for the details.
- **The list.** `L[k]` is binom(n,k) times the k-th sum, so
  C(n,k) = ±L[k]/Q with Q = (n+1)!·n!, and A002176(n) = Q/g with
  g = gcd(Q, L[0], …, L[n]). Hence A002176(n)·C(n,k) = ±L[k]/g.
- **Signs.** `(M:=-M)` flips M at every digit and keeps flipping across the
  k loop, so `L[k]` carries a sign (−1)^(nk) relative to the true numerator
  (the (−1)^k of the formula times (−1)^((n+1)k) from the flips). For k = 0
  it is +1, so `L[0]//g` is A002176(n)·C(n,0) with its sign (always
  positive, as the data show, but the program does not rely on that).
- `M*f` in the gcd is read after the comprehension, when M may be −(n+1)!;
  `gcd` ignores the sign.

**Notes**

- The b-file has 100 terms (n = 1 to 100), and the bar is the whole b-file
  in 60 s; it takes about 7 reference seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 212 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002177), CC BY-SA 4.0.
