# A001260

> Number of permutations of length n with 4 consecutive ascending pairs.
> — [OEIS A001260](https://oeis.org/A001260)

Offset 1: 0, 0, 0, 0, 1, 5, 45, 385, 3710, 38934, 444990, 5506710, 73422855, 1049946755, 16035550531, 260577696015, …

### Python 3 — 49 bytes

```python
e=m=-1
while[print(e*(m*m-1)//24)]:m+=1;e=(e^1)*m
```

**How it works**

- A permutation of [n] with exactly k successions (i directly followed
  by i + 1) is built from one with none: glue each succession into a
  block. That gives C(n−1, k)·S(n−k), where S(j) counts the permutations
  of [j] without successions, and S(j) = D(j) + D(j−1) = D(j+1)/j
  ([A000255](../../A000xxx/A000255/)). For k = 4 this simplifies to
  a(n) = (n−1)(n−2)(n−3)·D(n−3)/24.
- `e` is m·D(m−1), with m = n − 2. The update `e=(e^1)*m` uses the
  derangement recurrence D(j) = j·D(j−1) + (−1)ʲ. The `^1` is the
  ±1 because j·D(j−1) is even exactly when j is even, which is the
  [A000313](../../A000xxx/A000313/) trick. So the term is
  e·(m² − 1)/24.
- `e=m=-1` gives n = 1. The factor m² − 1 = 0 hides the junk value of
  `e`, m = 0 resets `e` to 0, and the first terms 0, 0, 0, 0, 1 follow.

**Notes**

- The whole b-file (200 terms) prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001260), CC BY-SA 4.0.
