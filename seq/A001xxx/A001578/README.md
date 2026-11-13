# A001578

> Smallest primitive prime factor of Fibonacci number F(n), or 1 if F(n) has no primitive prime factor.
> — [OEIS A001578](https://oeis.org/A001578)

Offset 1: 1, 1, 2, 3, 5, 1, 13, 7, 17, 11, 89, 1, 233, 29, 61, 47, 1597, 19, 37, 41, …

A prime p is a primitive prime factor of F(n) when it divides F(n) but no
earlier Fibonacci number F(1), …, F(n − 1).

### Python 3 — 108 bytes

```python
import math
a=b=L=d=1
while[print(d)]:
 a,b=b,a+b;Q=a//math.gcd(a,L**3);L*=a;d=2
 while Q%d:d=[Q,d+1][d*d<Q]
```

**How it works**

- `a,b=b,a+b` walks a = F(n) from F(1) = F(2) = 1, and `L` is the product
  F(1)·F(2)·…·F(n − 1). A prime factor of F(n) is not primitive exactly
  when it divides L.
- `Q=a//math.gcd(a,L**3)` strips those primes from F(n) completely, as long
  as L³ holds at least as many factors p as F(n) does (shown below). So Q
  is the product of the primitive prime powers of F(n), and a(n) is the
  smallest prime factor of Q, or 1 when Q = 1.
- Why the cube is enough. Let p | F(n) be non-primitive, z < n its entry
  point (the least z with p | F(z)); then z | n, t = n/z ≥ 2, and L
  contains F(z), F(2z), …, F((t − 1)z), each divisible by p. For odd p,
  Lucas's law v_p(F(mz)) = v_p(F(z)) + v_p(m) gives v_p(F(n)) = e + v_p(t)
  with e = v_p(F(z)) ≥ 1, while v_p(L) ≥ (t − 1)e ≥ e + v_p(t), since
  v_p(t) ≤ t − 2 for t ≥ 2. For p = 2 (z = 3), v₂(F(3m)) is 1 for odd m
  and v₂(m) + 2 for even m, and v₂(L) ≥ t − 1, so v₂(L³) ≥ 3(t − 1) ≥
  v₂(t) + 2. The cube is needed only at n = 6: F(6) = 8, but L = 30.
- Smallest prime factor by trial division: d starts at 2; while d does not
  divide Q it moves to d + 1 if d² < Q, and otherwise jumps to Q itself
  (no factor up to √Q, so Q is prime or 1), where `Q%d` is 0 and the loop
  ends. The first divisor found is prime, and Q = 1 ends with d = 1.
- `while[print(d)]:` prints a(1) = 1 from the starting d = 1 before the
  first pass. The 1s come out where F(n) has no primitive factor (n = 1,
  2, 6, 12 by Carmichael's theorem; the program does not use it).

**Notes**

- Exact for every n.
- Trial division up to the smallest primitive factor, or to √Q when Q is
  prime, dominates: a(82) arrives after about 7 s on the PC it was written
  on, but F(83) is prime and proving it so this way takes about 3·10⁸
  divisions. The bar is 80 terms in 60 s; the b-file has 1452.
- Every primitive prime factor p ≠ 5 of F(n) is ≡ ±1 (mod n), so trying
  only d ≡ ±1 (mod n) reaches 118 terms for about 20 more bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 108 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001578), CC BY-SA 4.0.
