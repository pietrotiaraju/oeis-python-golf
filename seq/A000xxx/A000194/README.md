# A000194

> n appears 2n times, for n >= 1; also nearest integer to square root of n.
> — [OEIS A000194](https://oeis.org/A000194)

Offset 0: 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, …

### Python 3 — 37 bytes

```python
n=k=0
while[print(k)]:n+=1;k+=n>k*k+k
```

**How it works**

- k ≥ 1 fills the block n = k² − k + 1, …, k² + k (Wolfdieter Lang's
  formula on the OEIS page), which has 2k entries, and a(0) = 0. So the value
  moves from k to k + 1 exactly when n passes k(k + 1).
- The loop prints a(n), steps n and adds the test `n>k*k+k` to k. Since n
  only ever goes one past k(k + 1), one comparison per step is enough, and
  with n = k = 0 the first line is a(0) = 0.
- A counter beats every closed form here: `isqrt(4*n)+1>>1` needs
  `from math import*`, the float `round(n**.5)` is not exact for large n, and
  printing each block at once (`f'{k}\n'*2*k`, an `exec` string or a list
  comprehension) costs 44 bytes or more because the lone 0 needs a special
  case.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (1001 terms) prints at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000194), CC BY-SA 4.0.
