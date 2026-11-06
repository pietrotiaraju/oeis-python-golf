# A000330

> Square pyramidal numbers: a(n) = 0^2 + 1^2 + 2^2 + ... + n^2 = n*(n+1)*(2*n+1)/6.
> — [OEIS A000330](https://oeis.org/A000330)

Offset 0: 0, 1, 5, 14, 30, 55, 91, 140, 204, 285, 385, 506, 650, 819, …

### Python 3 — 33 bytes

```python
s=n=0
while[print(s:=s+n*n)]:n+=1
```

**How it works**

- The name's own sum: s collects 0², 1², 2², …, and the walrus adds n² to s
  inside `print`, so each pass prints the new partial sum.
- s and n both start at 0, so one chained assignment sets them, and the first
  pass prints 0 + 0² = a(0).
- `print(…)` runs in the loop condition; it returns `None`, and `[None]` is a
  non-empty list, so the loop never stops and the body only steps n.

**Notes**

- Exact integers, so every term is right.
- `while[print(s)]:n+=1;s+=n*n` is the same length. The closed forms cost
  more: with m = 2n + 1 the term is (m³ − m)/24, and
  `m=1` + `while[print((m**3-m)//24)]:m+=2` is 35 bytes;
  `n*~n*~(n+n)//6` with a plain counter is 37. `m**3//24` alone is not exact:
  it is (m³ − m)/24 + ⌊m/24⌋, wrong from m = 25 on.
- The b-file has 10001 terms (n = 0 to 10000) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000330), CC BY-SA 4.0.
