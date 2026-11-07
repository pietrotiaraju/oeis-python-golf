# A000475

> Rencontres numbers: number of permutations of [n] with exactly 4 fixed points.
> — [OEIS A000475](https://oeis.org/A000475)

Offset 4: 1, 0, 15, 70, 630, 5544, 55650, 611820, 7342335, 95449640, …

### Python 3 — 51 bytes

```python
a=c=1;n=4
while[print(a)]:n+=1;c=c*n//(4-n);a=a*n+c
```

**How it works**

- Choose the 4 fixed points and derange the rest: a(n) = C(n,4)·D(n−4),
  with D the derangement numbers ([A000166](../A000166/)).
- D(m) = m·D(m−1) + (−1)ᵐ and (n−4)·C(n,4) = n·C(n−1,4) give
  a(n) = n·a(n−1) + (−1)ⁿ·C(n,4), starting from a(4) = 1.
- `c` carries the signed binomial (−1)ⁿ·C(n,4), so the update is a plain
  `a=a*n+c`. The step C(n,4) = C(n−1,4)·n/(n−4) becomes `c=c*n//(4-n)`:
  dividing by 4 − n instead of n − 4 flips the sign for free, and the
  floor division is exact because the quotient is ±C(n,4), an integer.

**Notes**

- `import math` with `a=n*a+(-1)**n*math.comb(n,4)` is 69 bytes. Tracking
  D(m) with the derangement parity trick (`d=d*m^1`, as in
  [A000166](../A000166/)) and printing `c*d` is 53 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 97 terms (up to a(100)); the bar is the whole b-file in
  60 s. It prints in a fraction of a second.
- a(n) first has more than 4300 digits at n = 1559, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 70 | first entry |
| 2026-11-06 | Python 3 | 69 | import math for a single comb call |
| 2026-11-07 | Python 3 | 51 | signed binomial carried with `c*n//(4-n)` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000475), CC BY-SA 4.0.
