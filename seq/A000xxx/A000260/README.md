# A000260

> Number of rooted simplicial 3-polytopes with n+3 nodes; or rooted 3-connected triangulations with 2n+2 faces; or rooted 3-connected trivalent maps with 2n+2 vertices.
> — [OEIS A000260](https://oeis.org/A000260)

Offset 0: 1, 1, 3, 13, 68, 399, 2530, 16965, 118668, 857956, 6369883, …

Tutte's count: a(n) = 2·(4n+1)! / ((n+1)!·(3n+2)!).

### Python 3 — 62 bytes

```python
import math
m=3
while[print(math.comb(m,m>>2)*6//m//~-m)]:m+=4
```

**How it works**

- **The variable.** `m` runs through 3, 7, 11, …, so on the pass that prints
  a(n) it is 4n + 3, and `m>>2` is n.
- **The formula.** C(4n+3, n) = (4n+3)! / (n!·(3n+3)!). Dividing by
  m(m−1) = (4n+3)(4n+2) leaves (4n+1)! on top, and (3n+3)! = 3(n+1)·(3n+2)!
  below, so 6·C(4n+3, n) / ((4n+3)(4n+2)) = 2·(4n+1)! / ((n+1)!·(3n+2)!),
  which is a(n). `~-m` is m − 1.
- **Why this binomial.** Any C(4n+c, n+d) differs from a(n) by a rational
  factor with two linear factors left in the denominator. Choosing
  C(4n+3, n) makes those two factors 4n+3 and 4n+2, that is m and m − 1 of a
  single variable, with n itself reachable as `m>>2`.
- **Exactness.** For positive integers p and q, ⌊⌊x/p⌋/q⌋ = ⌊x/(pq)⌋, so
  `//m//~-m` is the floor of the exact quotient, which is the integer a(n),
  even when the first quotient is not exact.
- **The loop.** `print` sits in the loop condition: it returns `None`, and
  `[None]` is a non-empty list, so the loop never ends (the
  [A000007](../A000007/) loop). `import math` with `math.comb` once is 1 byte
  shorter than `from math import*` with `comb`.

**Notes**

- Other versions that print the same terms:
  - C(4n+2, n)·8 / ((4n+2)(4n+4)) with `m=2` and `m+=4`,
    `math.comb(m,m>>2)*8//m//(m+2)`: 64 bytes;
  - a(n) = C(4n+2, n) / ((n+1)(2n+1)) in n itself, `n=0` and
    `math.comb(4*n+2,n)//-~n//(n-~n)`: 66 bytes;
  - the D-finite recurrence from the entry,
    (n+1)(3n+1)(3n+2)·3·a(n) = 8(4n+1)(4n−1)(2n−1)·a(n−1), written as
    `a=a*4*(4*n-2)*(16*n*n-1)//(3*n+1)//(3*n+2)//(3*n+3)`: 80 bytes
    (the ratio is cubic over cubic with nothing to cancel, unlike
    [A000139](../A000139/)).
- Exact integer arithmetic; correctness for every n rests only on the
  factorial formula. The values were checked against
  2·(4n+1)!/((n+1)!·(3n+2)!) for every term printed. The program prints
  a(0) to a(4411) and then stops with a `ValueError` at a(4412), the first
  term with more than 4300 digits (Python's int-to-str limit).
- The b-file has 201 terms (up to a(200)) and all of them print in well
  under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000260), CC BY-SA 4.0.
