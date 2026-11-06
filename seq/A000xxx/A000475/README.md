# A000475

> Rencontres numbers: number of permutations of [n] with exactly 4 fixed points.
> — [OEIS A000475](https://oeis.org/A000475)

Offset 4: 1, 0, 15, 70, 630, 5544, 55650, 611820, 7342335, 95449640, …

### Python 3 — 69 bytes

```python
import math
a=1;n=4
while[print(a)]:n+=1;a=n*a+(-1)**n*math.comb(n,4)
```

**How it works**

- Choose the 4 fixed points, then derange the remaining n−4
  elements: a(n)=C(n,4)·D(n−4), where D(m) is the
  derangement number and D(0)=1.
- Use D(m)=m·D(m−1)+(−1)ᵐ and
  (n−4)C(n,4)=n·C(n−1,4). This gives

  **a(n)=n·a(n−1)+(−1)ⁿ·C(n,4).**

- Initialize n=4, a=1, the identity on 4 elements.
  Increment n before the update, then multiply the previous term
  by the new n and apply the alternating correction.
- The first update gives a(5)=0: a permutation cannot
  have just one nonfixed point. The next gives
  a(6)=C(6,4)=15, since
  the remaining two elements must be exchanged.

- `math.comb(n,4)` computes the correction as an exact integer.
  Keeping the binomial coefficient avoids manually expanding
  four factors and their denominator.

**Notes**

- Exact integer arithmetic from the derangement recurrence. Only
  the current term and its index are stored, rather than a list
  of all derangement numbers.
- [A000449](../A000449/) is the same construction with
  three fixed points. The correction's
  sign changes with the parity of the fixed-point count because
  (−1)^(n−k)=(−1)ⁿ(−1)ᵏ.
- Factorial growth eventually meets Python 3.11+'s default
  4300-digit integer-to-string limit, an interpreter limit rather
  than a failure of the recurrence.
- The b-file has 97 terms (indices 4 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 70 | first entry |
| 2026-11-06 | Python 3 | 69 | import math for a single comb call |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000475), CC BY-SA 4.0.
