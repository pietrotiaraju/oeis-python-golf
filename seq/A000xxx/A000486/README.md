# A000486

> One half of the number of permutations of [n] such that the differences have 4 runs with the same signs.
> — [OEIS A000486](https://oeis.org/A000486)

Offset 5: 16, 150, 926, 4788, 22548, 100530, 433162, 1825296, 7577120, 31130190, …

R(n,k) counts the permutations of [n] whose sequence of successive
differences has k maximal blocks of equal sign ("alternating runs"); a(n) is
R(n,4)/2. Complementing every entry flips all the signs and keeps the runs,
so R(n,k) is even.

### Python 3 — 52 bytes

```python
m=4
while[print(4**m-3**m*3+(5-m<<m)+2*m-5>>1)]:m+=1
```

**How it works**

- a(n) = (4ⁿ⁻¹ − 3ⁿ + (6 − n)·2ⁿ⁻¹ + 2n − 7)/2, and with m = n − 1 the
  numerator is `4**m-3**m*3+(5-m<<m)+2*m-5`. `(5-m<<m)` is (5 − m)·2ᵐ,
  also for m > 5, where the left shift of a negative number is still a
  product.
- Where the formula comes from: André's recurrence
  R(n,k) = k·R(n−1,k) + 2R(n−1,k−1) + (n−k)·R(n−1,k−2) (checked here
  against brute force for n ≤ 9) gives R(n,2) = 2ⁿ − 4, then R(n,3) and
  R(n,4) as combinations of 4ⁿ, 3ⁿ, 2ⁿ, n·2ⁿ, n and 1. Such a
  combination solves a fixed linear recurrence of order 6, so it is pinned
  by six consecutive values; fitting a(5), …, a(10) gives the formula,
  which is also Colin Barker's generating function
  2x⁵(24x² − 29x + 8)/((1−x)²(1−2x)²(1−3x)(1−4x)) on the OEIS page.
- The numerator is 2a(n), so `>>1` halves it exactly; `>>` binds more
  loosely than `+` and `-`, so the whole sum is shifted.

**Notes**

- The six-term recurrence of that generating function with a(5), …,
  a(10) stored in a list was 114 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 996 terms (up to a(1000)); the bar is the whole b-file in
  60 s. It prints in a fraction of a second.
- a(n) first has more than 4300 digits at n = 7144, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |
| 2026-11-07 | Python 3 | 52 | closed form in m = n − 1, halved with `>>1` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000486), CC BY-SA 4.0.
