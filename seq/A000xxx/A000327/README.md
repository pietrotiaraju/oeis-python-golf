# A000327

> Number of partitions into non-integral powers.
> — [OEIS A000327](https://oeis.org/A000327)

Offset 3: 1, 5, 12, 23, 39, 62, 91, 127, 171, 228, 294, 370, 461, 561, …

### Python 3 — 101 bytes

```python
n=3
while[print(sum((n**3-x*x-y*y)**3>=27*(n*x*y)**2*n for y in range(n*n)for x in range(1,y)))]:n+=1
```

**How it works**

- As the OEIS comment puts it, a(n) counts the pairs of distinct integers
  1 ≤ x < y with x^(2/3) + y^(2/3) ≤ n (Agarwala and Auluck's partitions
  of n into two distinct parts k^(2/3), counted with ≤). It is
  [A000148](../A000148/), which allows x = y, without the diagonal: the
  entry's formula a(n) = A000148(n) − ⌊(n/2)^(3/2)⌋ removes exactly the
  pairs x = y.
- So the program is the A000148 program with x running over 1, …, y − 1
  (`range(1,y)`, 1 byte shorter than A000148's `range(-y,0)` for
  1, …, y) and starting at n = 3. y < n² is enough because y^(2/3) ≤ n − 1
  forces y ≤ (n − 1)^(3/2).
- The test is exact (the A000148 page has the details). With
  u = x^(2/3), v = y^(2/3) and s = u + v, s³ = x² + y² + 3uv·s, and
  t³ − 3uv·t increases for t ≥ √(uv) ≤ s/2, so s ≤ n exactly when
  m = n³ − x² − y² ≥ 3n·uv; cubing both sides gives the integer test
  m³ ≥ 27n³x²y², which also fails correctly when m < 0.

**Notes**

- Round n tries about n⁴/2 pairs, so the program prints about 53 terms in
  60 s of the 998 in the b-file. The bar is 40 terms in 60 s.
- Counting x = 0 as well (`range(y)`) and subtracting ⌊n^(3/2)⌋ for those
  pairs is longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 101 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000327), CC BY-SA 4.0.
