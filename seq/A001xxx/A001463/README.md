# A001463

> Partial sums of A001462; also a(n) is the last occurrence of n in A001462.
> — [OEIS A001463](https://oeis.org/A001463)

Offset 1: 1, 3, 5, 8, 11, 15, 19, 23, 28, 33, 38, 44, 50, 56, 62, 69, 76, 83, 90, 98, 106, …

### Python 3 — 47 bytes

```python
a=[0,1]
while[print(sum(a))]:a+=1+a[-a[a[-1]]],
```

**How it works**

- `a` is the list of [A001462](../A001462/) (Golomb's sequence) with a
  dummy 0 in front, built by Mallows' recurrence
  g(n) = 1 + g(n − g(g(n − 1))) exactly as on that page (where the
  recurrence is proved): `a[a[-1]]` is g(g(n − 1)) and the negative index
  `a[-k]` is g(n − k).
- Before appending g(n + 1), the list holds 0, g(1), …, g(n), so `sum(a)`
  is g(1) + … + g(n) = a(n), the n-th partial sum. Value k fills a block of
  g(k) places in Golomb's sequence, so this is also where the block of n
  ends, the second description in the title.

**Notes**

- `sum(a)` re-adds the whole list each time, about n²/2 additions for n
  terms; the 10000-term b-file still prints in about half a second. A
  running total, `s=0` with `print(s:=s+a[-1])`, is 55 bytes.
- Exact integer arithmetic. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001463), CC BY-SA 4.0.
