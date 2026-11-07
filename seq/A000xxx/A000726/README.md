# A000726

> Number of partitions of n in which no parts are multiples of 3.
> — [OEIS A000726](https://oeis.org/A000726)

Offset 0: 1, 1, 2, 2, 4, 5, 7, 9, 13, 16, 22, 27, 36, 44, 57, 70, 89, 108, 135, 163, …

### Python 3 — 85 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0)if d%3)//n,
```

**How it works**

- The g.f. is Π 1/(1 − xᵏ) over k not divisible by 3: the Euler transform
  of b(k) = [3 ∤ k]. Its log derivative gives
  **N·a(N) = Σ_{3∤d} d·Σ_j a(N − dj)** over d ≤ N and j ≥ 1 with dj ≤ N
  (the divisor sums of A046913 grouped by d).
- This is the [A000041](../A000041/) program with the filter `if d%3`
  on the divisor loop. `n` is −N, `d` runs over −N…−1 (a negative d is a
  multiple of 3 exactly when `d%3` is 0), the slice `a[d::d]` is
  a(N − |d|), a(N − 2|d|), …, and `//n` divides −N·a(N) by −N exactly.
- The filter is 6 bytes; a weight `*(d%3>0)` would be 8.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 0.91·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 2·10⁷.
- Term N costs N Python steps plus about (2/3)·N·ln N additions inside the
  slice sums: the whole b-file (5001 terms) prints in about 15 s here, and
  the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000726), CC BY-SA 4.0.
