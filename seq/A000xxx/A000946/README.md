# A000946

> Euclid-Mullin sequence: a(1) = 2, a(n+1) is the largest prime factor of 1 + Product_{k=1..n} a(k).
> — [OEIS A000946](https://oeis.org/A000946)

Offset 1: 2, 3, 7, 43, 139, 50207, 340999, 2365347734339, 4680225641471129, 1368845206580129, …

### Python 3 — 75 bytes

```python
P=1
while 1:
 m=P+1;d=2
 while d*d<=m:d+=m%d>0 or(m:=m//d)*0
 print(m);P*=m
```

**How it works**

- m = P+1, where `P` is the product of the terms so far, and d runs over
  trial divisors while d·d ≤ m. `d+=m%d>0 or(m:=m//d)*0` adds 1 to d when
  d ∤ m; when d | m it divides one factor d out of m and adds 0, so d stays
  until all its powers are gone. (The space in `0 or` is needed: `0o` would
  start an octal literal.) This is 1 byte under `m//=d**(m%d<1);d+=m%d>0`.
- When d·d > m, m has no divisor in 2…d−1 and none ≤ √m, so m is prime. Every
  factor taken out was ≤ m at that time (it was ≤ √m before the division), so
  this m is the largest prime factor.

**Notes**

- Exact trial division; no probable-prime test.
- 8 terms in about 1 s. For a(9), 1 + P = 17 · 127770091783 ·
  4680225641471129, so trial division would have to reach 1.3·10¹¹. Pollard
  rho with Miller–Rabin on the first 13 prime bases (proved correct below
  3.3·10²⁴) would give a(9) and a(10), but a(11) has 33 digits and needs a
  real primality proof. The bar is 8 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000946), CC BY-SA 4.0.
