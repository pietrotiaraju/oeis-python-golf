# A002174

> Values taken by reduced totient function psi(n).
> — [OEIS A002174](https://oeis.org/A002174)

Offset 1: 1, 2, 4, 6, 8, 10, 12, 16, 18, 20, 22, 24, …

psi is Carmichael's λ: the exponent of the group of units modulo n.

### Python 3 — 120 bytes

```python
from math import*
P=v=1;s=[1]
while[lcm(*(gcd(v,d*(d+1)**v)for d in s if v%d<1))<v or print(v)]:v+=1;P*=v*v;s+=P%-~v*[v]
```

**How it works**

- **λ on prime powers.** λ(n) is the lcm of λ(p^k) over the prime
  powers p^k ∥ n, with λ(2) = 1, λ(4) = 2, λ(2^k) = 2^(k−2) for k ≥ 3,
  and λ(p^k) = (p − 1)·p^(k−1) for odd p.
- **Test.** For v ≥ 1 let L(v) be the lcm, over the divisors d of v with
  d + 1 prime, of c_d = d·(d + 1)^e, e the exponent of d + 1 in v.
  Then v is a value of λ exactly when L(v) = v:
  - every c_d divides v (d | v, (d + 1)^e | v, and the two are
    coprime), and every c_d is a λ of a prime power: c_1 = 2^e is
    λ(2^(e+2)) for e ≥ 1 and λ(2) for e = 0, and for d ≥ 2,
    c_d = λ(p^(e+1)) with p = d + 1. These prime powers have distinct
    primes, so L(v) = λ(their product) is a value, and L(v) | v;
  - if λ(n) = v, then each λ(p^k) with p^k ∥ n divides v: for odd p,
    d = p − 1 divides v and p^(k−1) divides v, so λ(p^k) | c_d; for
    p = 2, λ(2^k) is a power of 2 dividing v, so it divides c_1. Hence
    v | L(v) | v.
- **c_d in code.** `gcd(v,d*(d+1)**v)`: as d | v and
  gcd(d, d + 1) = 1, this is d·gcd(v/d, (d + 1)^v) = c_d, because the
  exponent e of d + 1 in v/d is below v. `lcm(…)<v or print(v)` prints v
  when L(v) = v (L(v) divides v, so it can't be larger).
- **The list `s`** holds every d ≤ v with d + 1 prime. `P` = (v!)²,
  and by Wilson's theorem `P%-~v` (P mod v + 1) is 1 when v + 1 is prime
  and 0 when it is composite (36 ≡ 0 mod 4 too), so `s+=P%-~v*[v]`
  appends v exactly when v + 1 is prime. It starts as `[1]` (2 is
  prime).

**Notes**

- Wilson's theorem and exact integers: right for every n.
- Each v scans the primes up to v + 1 once (`v%d<1` picks the
  divisors), and the powers (d + 1)^v have up to v·log₂(v + 1) bits:
  5000 terms (v ≤ 17444) arrive in 15 reference seconds (25 s here).
  The exponent `v//d` instead of `v` is 5 bytes longer and fast enough
  for the whole b-file (10000 terms) in about 15 s here. The bar is
  5000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 120 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002174), CC BY-SA 4.0.
