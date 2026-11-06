# A000377

> Expansion of f(-q^3) * f(-q^8) * chi(-q^12) / chi(-q) in powers of q
> where chi(), f() are Ramanujan theta functions.
> — [OEIS A000377](https://oeis.org/A000377)

Offset 0: 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 0, 2, 2, 1, 0, 1, 0, …

### Python 3 — 73 bytes

```python
r=[0]
for n in r:r+=n+1,;print(sum(d//12%-2|1for d in r if 1==d%6%4>n%d))
```

**How it works**

- The OEIS page gives a(n) = Σ_{d|n} (−6/d) for n ≥ 1 (Kronecker symbol;
  the PARI program there), and a(0) = 1. Equivalently, the Möbius transform
  of a is the period-24 sequence that is 1 for d ≡ 1, 5, 7, 11, −1 for
  d ≡ 13, 17, 19, 23 (mod 24) and 0 otherwise.
- So the program counts the divisors d of n prime to 6, with sign +1 when
  d mod 24 < 12 and −1 when d mod 24 > 12.
- `d%6%4` is 1 exactly when d is prime to 6 (d mod 6 = 1 or 5) and 0, 2 or
  3 otherwise. The chain `1==d%6%4>n%d` adds "d divides n" (n mod d < 1);
  for d = 0 its first link is already false, so `n%0` is never evaluated.
- `d//12%-2|1` is the sign: d//12 mod −2 is 0 or −1 (odd and even halves
  of the period), and `|1` turns it into +1 or −1.
- The loop is the growing list of [A000203](../A000203/): r is 0, 1, …,
  n + 1 at step n. For n ≥ 1 the extra n + 1 never divides n. At n = 0
  every d divides 0, and d = 1 is the only one prime to 6, so a(0) = 1
  comes out with no special case.

**Notes**

- Exact integers; correctness for every n rests on the divisor-sum formula.
  It is Dirichlet's formula for discriminant −24, whose two reduced forms
  x² + 6y² and 2x² + 3y² together represent n ≥ 1 in 2·Σ_{d|n} (−24/d)
  ways, combined with the OEIS expansion a(n) = (#{x² + 6y² = n} +
  #{2x² + 3y² = n})/2; for d prime to 6, (−24/d) = (−6/d). It matches
  Somos's multiplicative description on the OEIS page (a(pᵉ) = e + 1 for
  p ≡ 1, 5, 7, 11 and (1 + (−1)ᵉ)/2 for p ≡ 13, 17, 19, 23 (mod 24),
  a(2ᵉ) = a(3ᵉ) = 1).
- 74 bytes each: the sign as `1-d//12%2*2`, the prime-to-6 test as
  `d*d%24`, and a `while` loop over `range(1,n+2)` (where d = n + 1 is the
  divisor 1 of n = 0).
- Counting representations, a(n) = (#{x² + 6y² = n} + #{2x² + 3y² = n})/2
  (also on the OEIS page), is longer and quadratic in n.
- The whole b-file (10001 terms) prints in about 10 s; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000377), CC BY-SA 4.0.
