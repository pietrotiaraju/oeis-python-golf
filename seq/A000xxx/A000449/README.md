# A000449

> Rencontres numbers: number of permutations of [n] with exactly 3 fixed points.
> — [OEIS A000449](https://oeis.org/A000449)

Offset 3: 1, 0, 10, 40, 315, 2464, 22260, 222480, 2447445, 29369120, …

### Python 3 — 59 bytes

```python
a=1;n=3
while[print(a)]:n+=1;a=n*a-(-1)**n*n*(n-1)*(n-2)//6
```

**How it works**

- Choose the 3 fixed points, then derange the remaining n−3
  elements: a(n)=C(n,3)·D(n−3), where D(m) is the
  derangement number and D(0)=1.
- Use D(m)=m·D(m−1)+(−1)ᵐ and
  (n−3)C(n,3)=n·C(n−1,3). This gives

  **a(n)=n·a(n−1)−(−1)ⁿ·C(n,3).**

- Initialize n=3, a=1, the identity on 3 elements.
  Increment n before the update, then multiply the previous term
  by the new n and apply the alternating correction.
- The first update gives a(4)=0: a permutation cannot
  have just one nonfixed point. The next gives
  a(5)=C(5,3)=10, since
  the remaining two elements must be exchanged.

- `n*(n-1)*(n-2)//6` expands C(n,3) without an import.
  The signed product is always divisible by 6, including when
  it is negative, so floor division makes no rounding error.

**Notes**

- Exact integer arithmetic from the derangement recurrence. Only
  the current term and its index are stored, rather than a list
  of all derangement numbers.
- [A000475](../A000475/) is the same construction with
  four fixed points. The correction's
  sign changes with the parity of the fixed-point count because
  (−1)^(n−k)=(−1)ⁿ(−1)ᵏ.
- Factorial growth eventually meets Python 3.11+'s default
  4300-digit integer-to-string limit, an interpreter limit rather
  than a failure of the recurrence.
- The b-file has 98 terms (indices 3 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000449), CC BY-SA 4.0.
