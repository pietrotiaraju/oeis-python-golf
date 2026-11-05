# A000167

> Nearest integer to modified Bessel function K_n(2).
> — [OEIS A000167](https://oeis.org/A000167)

Offset 0: 0, 0, 0, 1, 2, 9, 49, 306, 2188, 17810, …

### Python 3 — 69 bytes

```python
y=z=n=0;G=1
while[print(~-z//G+1>>1)]:n+=1;y,z=z,n*(~-n*(y+z)^1);G*=n
```

**How it works**

- At z = 2 the logarithm in the series for K_n (DLMF 10.31.1) vanishes,
  ln(z/2) = 0, and it splits into a finite rational part and a small tail:
  K_n(2) = u_n/2 + t_n with
  u_n = Σ_{k=0..n−1} (−1)^k (n−1−k)!/k! and
  t_n = (−1)^n·½·Σ_{k≥0} (ψ(k+1)+ψ(n+k+1))/(k!(n+k)!).
- For n ≥ 3, (n−1)!·u_n is an integer that (n−1)! does not divide: the
  k = n−1 term is ±1/(n−1)! and every other term has a denominator
  dividing (n−2)!. So u_n/2 is at least 1/(2(n−1)!) away from every
  half-integer.
- The tail is smaller than that. All terms of the sum are positive for
  n ≥ 2, ψ(x) < ln x, and n(n+1)⋯(n+k) ≥ n^(k+1) give
  2(n−1)!·|t_n| < (2/n)·e^(1/n)·(ln(n+1) + 1/(n(n+1))), which is below 1
  for n ≥ 5 and decreasing; for n = 2, 3, 4 the exact value is 0.51, 0.41
  and 0.35. Hence K_n(2) and u_n/2 round to the same integer for n ≥ 2
  (u_2 = 0, and |t_2| < ½). For n = 1, u_1/2 = ½ while K_1(2) ≈ 0.14,
  and K_0(2) ≈ 0.11 with u_0 = 0, so a(n) is u_n/2 rounded with halves
  going down, for every n.
- Integers: z_n = n!·u_n. From u_{n+1} = n·u_n + u_{n−1} + (−1)^n/n!
  (split (n−k)! = (n−k)·(n−1−k)! in the sum) comes
  z_n = n·((n−1)(z_{n−1}+z_{n−2}) + (−1)^(n−1)).
- The inner product (n−1)(z_{n−1}+z_{n−2}) has the parity of n−1 (the
  quotient z_m/m has the parity of m, by induction from z_1 = 1), so
  adding (−1)^(n−1) is `^1` on it, as for the derangement numbers.
- With G = n!, halves-down rounding of z/(2G) is ⌊(⌊(z−1)/G⌋ + 1)/2⌋:
  `~-z//G+1>>1`.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (201 terms) prints at once; the program stops after a(1559), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000167), CC BY-SA 4.0.
