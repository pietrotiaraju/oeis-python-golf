# A002176

> a(n) = LCM of denominators of Cotesian numbers {C(n,k), 0 <= k <= n}.
> — [OEIS A002176](https://oeis.org/A002176)

Offset 1: 2, 6, 8, 90, 288, 840, 17280, 28350, 89600, 598752, …

### Python 3 — 207 bytes

```python
from math import*
n=f=1
while 1:r=range(n+1);M=f*n+f;K=n*len(bin(n));B=1<<K;print(M*f//gcd(M*f,*[sum((P>>K*i&B-1)*(M:=-M)//~i for i in r)*comb(n,k)for k in r if[P:=prod(j+n*B for j in r if j-k)]]));n+=1;f*=n
```

**How it works**

- **Cotesian numbers.** C(n,k) are the weights of the closed Newton–Cotes
  rule with nodes 0, 1, …, n, scaled to sum 1:
  C(n,k) = (1/n)·∫₀ⁿ ∏_(j≠k) (t − j)/(k − j) dt (the Lagrange basis
  integrated; the entry's PARI program solves the same Vandermonde system).
  Putting t = nx and using ∏_(j≠k) (k − j) = (−1)^(n−k)·k!·(n−k)!,
  C(n,k) = (−1)^k·binom(n,k)/n! · ∫₀¹ g_k(x) dx with
  g_k(x) = ∏_(j≠k) (j − nx).
- **Kronecker substitution.** g_k(−y) = ∏_(j≠k) (j + ny) has nonnegative
  integer coefficients d₀ … d_n, each at most their sum
  ∏_(j≠k) (j + n) ≤ (2n)!/n! < (2n)ⁿ. With K = n·len(bin(n)) (the bit
  length of n plus 2, which exceeds log₂ 2n) every d_i is below B = 2^K, so
  `P=prod(j+n*B for j in r if j-k)` holds them as its base-B digits and
  `P>>K*i&B-1` reads d_i with a shift and a mask.
- **The integral.** ∫₀¹ g_k = Σ_i (−1)^i·d_i/(i + 1). With M = (n+1)!
  every M/(i + 1) is an integer, so `d*M//~i` (floor division by
  −(i + 1)) is exact. `(M:=-M)` flips the sign of M at every digit, which
  supplies the (−1)^i; since it keeps flipping across the k loop, the k-th
  sum comes out multiplied by (−1)^((n+1)k), a sign the gcd ignores.
- **Common denominator.** Each C(n,k) is N_k/Q with Q = M·n! = (n+1)!·n!
  and N_k = ±binom(n,k)·Σ_i (−1)^i·d_i·M/(i + 1). Its reduced denominator
  is Q/gcd(Q, N_k), and the LCM of these divisors of Q is
  Q/gcd(Q, N₀, …, N_n), one `gcd` call (Python 3.9+ takes many arguments).
- **Bookkeeping.** `f` is n!, updated by `n+=1;f*=n`, and M = f·n + f;
  `M*f` is read before the comprehension flips M. `if[P:=…]` binds the
  node polynomial for each k inside the comprehension.

**Notes**

- The b-file has 100 terms (n = 1 to 100), and the bar is the whole b-file
  in 60 s; it takes about 7 reference seconds. The per-k products are
  the cost; dividing one full product by k + nB instead is faster and
  7 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 207 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002176), CC BY-SA 4.0.
