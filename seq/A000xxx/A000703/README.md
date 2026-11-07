# A000703

> Chromatic number (or Heawood number) of nonorientable surface with n crosscaps.
> — [OEIS A000703](https://oeis.org/A000703)

Offset 0: 4, 6, 7, 7, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, …

### Python 3 — 55 bytes

```python
n=2
while[print(sum(j*-~j<n for j in range(n))+3)]:n+=6
```

**How it works**

- The OEIS formula is a(n) = ⌊(7 + √(1+24n))/2⌋, the Heawood number
  (the terms follow it for every n, including a(2) = 7 for the Klein
  bottle).
- Write s = √(24n+1). Only ⌊s⌋ matters, and ⌊(7+s)/2⌋ = 3 + ⌊(1+⌊s⌋)/2⌋,
  which is 3 plus the number of odd j ≤ s. With j = 2i+1,
  (2i+1)² ≤ 24n+1 ⇔ i(i+1) ≤ 6n, so
  a(n) = 3 + #{i ≥ 0 : i(i+1) ≤ 6n}.
- The loop keeps N = 6n+2 in `n`. Since i(i+1) is even, i(i+1) ≤ 6n ⇔
  i(i+1) < 6n+2, which is the test `j*-~j<n` (`-~j` is j+1). Every i that
  passes is below N, so `range(n)` is a large enough search range; for
  n = 0 it is {0, 1} and counts only i = 0, giving 4.

**Notes**

- Exact integer comparisons, no square root at all.
- `from math import*` with `7+isqrt(n)>>1` and n stepping by 24 from 1 is
  57 bytes.
- Each term costs O(n) comparisons; the whole b-file (1001 terms) prints
  in under a second, and it is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000703), CC BY-SA 4.0.
