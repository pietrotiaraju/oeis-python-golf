# A000704

> Number of degree-n even permutations of order dividing 2.
> — [OEIS A000704](https://oeis.org/A000704)

Offset 0: 1, 1, 1, 1, 4, 16, 46, 106, 316, 1324, 5356, 18316, 63856, 272416, 1264264, …

### Python 3 — 58 bytes

```python
a=b=n=1;c=d=0
while[print(a)]:a,b,c,d=b,b+n*c,d,d+n*a;n+=1
```

**How it works**

- These are the involutions (with the identity) made of an even number of
  transpositions. Let E(n) and O(n) count the involutions of n points with
  an even and an odd number of transpositions.
- Point n is either fixed (the rest is any involution of n−1 points, same
  parity) or swapped with one of the other n−1 points, which adds one
  transposition and flips the parity of what is left on n−2 points:
  E(n) = E(n−1) + (n−1)·O(n−2) and O(n) = O(n−1) + (n−1)·E(n−2).
  This is the involution recurrence of [A000085](../A000085/) split by
  parity.
- The four variables hold E(m), E(m+1), O(m), O(m+1) with `n` = m+1; the
  start is E(0) = E(1) = 1, O(0) = O(1) = 0.

**Notes**

- Exact integer arithmetic, O(1) multiplications per term.
- The whole b-file (201 terms) prints in well under a second; it is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000704), CC BY-SA 4.0.
