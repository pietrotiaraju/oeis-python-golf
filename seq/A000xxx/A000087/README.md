# A000087

> Number of unrooted nonseparable planar maps with n edges and a distinguished face.
> — [OEIS A000087](https://oeis.org/A000087)

Offset 1: 2, 1, 2, 4, 10, 37, 138, 628, 2972, 14903, 76994, 409594, 2222628, 12281570, …

### Python 3 — 160 bytes

```python
from math import*
F=lambda k:4*comb(3*k,k)//(9*k*~-k+2)**(k*2>n)
n=1
while[print((-~n*F(n)+sum(F(gcd(j,n))for j in range(n))+n%2*n*F(m:=-~n//2)*m)//12//n)]:n+=1
```

**How it works**

- Liskovets' formula from the OEIS page, with c(k) = C(3k, k):
  a(n) = (1/(3n))·[(n+2)·c(n)/((3n−2)(3n−1)) + Σ_{k|n, k<n} φ(n/k)·c(k)] + q(n),
  where q(n) = 0 for even n and, for odd n = 2m − 1,
  q(n) = 2(n+1)·c(m)/(3(3n−1)(3n+1)).
- The fractions all have the same shape. Let **F(k) = 4·c(k)/((3k−1)(3k−2))**.
  This is an integer: it is 3·r(k), where r(k) = 2(3k−3)!/(k!(2k−1)!)
  counts rooted nonseparable maps ([A000139](https://oeis.org/A000139)).
  With 3n−1 = 2(3m−2) and 3n+1 = 2(3m−1), q(n) = m·F(m)/12, and the whole
  formula becomes
  **12n·a(n) = (n+2)·F(n) + 4·Σ_{k|n, k<n} φ(n/k)·c(k) + [n odd]·n·m·F(m)**.
- The φ sum is a gcd sum: as j runs over 0 … n−1, gcd(j, n) takes each
  divisor k of n exactly φ(n/k) times, with j = 0 giving k = n.
- One lambda does both kinds of term. It divides by (3k−1)(3k−2) only when
  2k > n, which holds for k = n and k = m = (n+1)/2 but for no proper
  divisor of n, since those are at most n/2. So
  `sum(F(gcd(j,n))for j in range(n))` is F(n) + 4·Σ φ(n/k)·c(k), and
  `-~n*F(n)` adds the n+1 missing copies of F(n). `9*k*~-k+2` is
  (3k−1)(3k−2) = 9k(k−1) + 2, and `**(k*2>n)` raises it to the power 1 or 0.
- `n%2*n*F(m:=-~n//2)*m` is the q term: m = (n+1)//2, and `n%2` zeroes it
  for even n.
- `while[print(…)]:n+=1` prints and loops forever, because `[None]` is a
  non-empty list. It is a byte shorter than `n=0` with `while n:=n+1:`.

**Notes**

- Exact integer arithmetic, so the program is right for every n, as far as
  Liskovets' formula is: every `//` divides an exact multiple. F(k) is an
  integer, and 12n·a(n) is a multiple of 12n because a(n) is an integer.
- The whole b-file (200 terms) prints in about a tenth of a second. The bar
  is the whole b-file in 60 s.
- a(n) ~ 3/(8·√(3π))·(27/4)ⁿ·n^(−5/2) (Lorand), so a(5199) is the first term
  whose decimal form passes Python's 4300-digit int-to-str limit. The
  program prints 5198 terms and stops there.
- With sympy, `binomial(3*k,k)/…` stays an exact rational, so `4*` and
  `//12//n` turn into `/3/n`. But `from sympy import*`, `binomial` and
  `igcd` cost as much as that saves, and it ties at 160 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 160 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000087), CC BY-SA 4.0.
