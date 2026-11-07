# A000934

> Chromatic number (or Heawood number) Chi(n) of a closed orientable surface of genus n.
> — [OEIS A000934](https://oeis.org/A000934)

Offset 0: 4, 7, 8, 9, 10, 11, 12, 12, 13, 13, 14, 15, 15, 16, 16, 16, 17, 17, 18, 18, …

### Python 3 — 54 bytes

```python
import math
n=1
while[print(7+math.isqrt(n)>>1)]:n+=48
```

**How it works**

- Heawood's bound χ(n) ≤ ⌊(7+√(1+48n))/2⌋ for the orientable surface of
  genus n ≥ 1 is sharp by the Ringel–Youngs theorem (Kₖ embeds in the
  surface for that k); for n = 0 (the sphere) the formula gives 4, which is
  the four colour theorem (Appel–Haken).
- ⌊(7+x)/2⌋ = ⌊(7+⌊x⌋)/2⌋, so the integer square root is exact:
  `7+math.isqrt(n)>>1` with the loop variable holding 48n+1 directly
  (`n+=48`), so no multiplication in the call.
- `import math` plus `math.` is 1 byte under `from math import*`. A counter
  that steps χ while (χ−2)(χ−3) ≤ 12n is longer (57 B), because the jump
  4 → 7 at n = 1 needs a special first term or an inner loop (59 B).

**Notes**

- Exact integer arithmetic; correctness rests on the Ringel–Youngs theorem
  and the four colour theorem.
- About 140 000 terms per second.
- The b-file has 10001 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000934), CC BY-SA 4.0.
