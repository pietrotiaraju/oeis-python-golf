# A000459

> Number of multiset permutations of {1, 1, 2, 2, ..., n, n} with no fixed points.
> — [OEIS A000459](https://oeis.org/A000459)

Offset 0: 1, 0, 1, 10, 297, 13756, 925705, 85394646, 10351036465, 1596005408152, …

### Python 3 — 66 bytes

```python
a=b=1;n=0
while[print(b)]:n+=1;a,b=b,n*((2*n-1)*b+2*(n-1)*a)-2*n+1
```

**How it works**

- Use the recurrence on the OEIS page,

  a(n)=n(2n−1)a(n−1)+2n(n−1)a(n−2)−(2n−1),
  with a(0)=1 and a(1)=0.

- At each print b is a(n), and a holds the preceding value once
  n≥1. Increase n, then assign `a,b=b,...` simultaneously, so
  both terms on the right still come from the old state.
- The expression `n*((2*n-1)*b+2*(n-1)*a)-2*n+1`
  groups the two recurrence terms sharing the factor n.
- Initially a=b=1. The first update multiplies the arbitrary
  preceding a by n−1=0, so b becomes 1−2+1=0 as required.
  The next update gives 2·(3·0+2·1)−4+1=1.

**Notes**

- A fixed position is defined relative to the reference arrangement
  1,1,2,2,…,n,n. Exchanging the two indistinguishable copies of
  a label does not create a new multiset permutation.
- The recurrence supplies exact integer values at every index using
  only two consecutive terms and a counter. Enumerating distinct
  permutations would instead require (2n)!/2ⁿ candidates before
  testing the fixed positions.
- Counts grow at factorial scale. Python 3.11+ eventually reaches
  its default 4300-digit output conversion limit, an interpreter limit.
- The b-file has 101 terms (indices 0 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000459), CC BY-SA 4.0.
