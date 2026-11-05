# A000037

> Numbers that are not squares (or, the nonsquares).
> — [OEIS A000037](https://oeis.org/A000037)

Offset 1: 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, …

### Python 3 — 39 bytes

```python
n=r=1
while[print(n+r)]:n+=1;r+=r*r+r<n
```

**How it works**

- The OEIS formula is **a(n) = n + round(√n)**: between r² and (r+1)² lie
  the 2r nonsquares r² + 1 … r² + 2r, which are n + r for
  n = r² − r + 1 … r² + r, and those are exactly the n with round(√n) = r.
- So r = round(√n) only has to go up by one when n passes r² + r. The body
  does `n+=1`, then `r+=r*r+r<n` adds the comparison (`True` is 1). No square
  root is ever taken, so the arithmetic is exact for every n.
- The loop condition `[print(n+r)]` is a non-empty list, so always true, as in
  [A000027](../A000027/); it prints a(1) = 1 + 1 = 2 before the body first
  runs.

**Notes**

- `k=s=1` + `while[s*s>k!=print(k)]:k+=1;s+=s*s<k` (42 bytes) walks the
  integers instead, keeping s = ⌈√k⌉ and skipping the k with s² = k.
- `n=1` + `while[print(n+round(n**.5))]:n+=1` is 37 bytes but uses floats:
  at n = 1125900007505922 = r² + r with r = 2²⁵ + 1 it prints the square
  (r + 1)² instead of (r + 1)² − 1, so the rules do not accept it.
- The exact `math.isqrt` versions cost the import: `isqrt(k)**2<k` as a
  filter is 57 bytes and n + (isqrt(4n) + 1)/2 is 60.
- The whole b-file (10 000 terms) prints instantly; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000037), CC BY-SA 4.0.
