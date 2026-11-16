# A001844

> Centered square numbers: a(n) = 2*n*(n+1)+1. Sums of two consecutive squares. Also, consider all Pythagorean triples (X, Y, Z=Y+1) ordered by increasing Z; then sequence gives Z values.
> — [OEIS A001844](https://oeis.org/A001844)

Offset 0: 1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265, 313, 365, …

### Python 3 — 31 bytes

```python
k=1
while[print(k*k//2+1)]:k+=2
```

**How it works**

- With k = 2n + 1, k² = 4n² + 4n + 1, so 2n(n + 1) + 1 = (k² + 1)/2, and
  since k² is odd this is ⌊k²/2⌋ + 1. `k` runs over the odd numbers.
- The centered squares are also the crystal ball sequence of the square
  lattice, (1 + x)²/(1 − x)³; the higher dimensions are
  [A001845](../A001845/) to [A001849](../A001849/).

**Notes**

- `2*n*-~n+1` with n = 0, 1, … is 32 bytes, and the running sum
  a(n) = a(n−1) + 4n is 33.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001844), CC BY-SA 4.0.
