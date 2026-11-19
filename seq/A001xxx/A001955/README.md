# A001955

> Beatty sequence of 1 + 1/sqrt(11).
> — [OEIS A001955](https://oeis.org/A001955)

Offset 1: 1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16, 18, 19, …

### Python 3 — 44 bytes

```python
n=t=1
while[print(n+t-1)]:n+=1;t+=11*t*t<n*n
```

**How it works**

- a(n) = ⌊n(1 + 1/√11)⌋ = n + b(n) with b(n) = ⌊n/√11⌋.
- 1/√11 ≈ 0.30 < 1, so b(n) is b(n − 1) or b(n − 1) + 1, the larger
  exactly when t = b(n − 1) + 1 ≤ n/√11, that is 11t² ≤ n². Equality
  would make √11 rational, so the test is `11*t*t<n*n`.
- The loop keeps t = b + 1 (starting from b(1) = 0) and adds the bool to
  it; it prints n + t − 1 = n + b(n).

**Notes**

- Exact integer arithmetic, with no floats or square roots, so the
  program is right for every n.
- As the OEIS entry recalls from Fraenkel's article, the complement is
  ⌊n(1 + √11)⌋ (Beatty's theorem: 1/(1 + 1/√11) + 1/(1 + √11) = 1).
- The whole b-file (10000 terms) comes in about a tenth of a second; the
  bar is the whole b-file in 60 s.
- `n+math.isqrt(n*n//11)` makes 56 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001955), CC BY-SA 4.0.
