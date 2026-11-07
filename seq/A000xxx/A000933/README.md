# A000933

> Genus of complete graph on n nodes.
> — [OEIS A000933](https://oeis.org/A000933)

Offset 1: 0, 0, 0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 8, 10, 11, 13, 16, 18, 20, 23, …

### Python 3 — 40 bytes

```python
k=2
while[print(-(k*~k//12)*(k<1))]:k-=1
```

**How it works**

- Ringel–Youngs theorem (Map Color Theorem, 1968): the genus of Kₙ is
  ⌈(n−3)(n−4)/12⌉ for n ≥ 3. For n = 1, 2 the graph is planar, genus 0,
  but the formula would give 1.
- With k = 3−n the product is (n−3)(n−4) = k(k+1), and `k*~k` = −k(k+1),
  so `-(k*~k//12)` is the ceiling without a `+11`.
- k starts at 2 and counts down; the factor `(k<1)` zeroes the two terms
  n = 1, 2 (k = 2, 1), where the formula does not apply.

**Notes**

- Exact integer arithmetic; correctness rests on the Ringel–Youngs theorem.
- Hundreds of thousands of terms per second.
- The b-file has 1000 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000933), CC BY-SA 4.0.
