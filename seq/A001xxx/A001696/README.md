# A001696

> a(n) = a(n-1)*(1 + a(n-1) - a(n-2)), a(0) = 0, a(1) = 1.
> — [OEIS A001696](https://oeis.org/A001696)

Offset 0: 0, 1, 2, 4, 12, 108, 10476, 108625644, 11798392680793836, …

### Python 3 — 33 bytes

```python
a=1;s=0
while[print(s)]:s+=a;a*=s
```

**How it works**

- **Work with the differences.** Let t_n = a(n+1) − a(n). The recurrence
  gives a(n+1) − a(n) = a(n)·(1 + a(n) − a(n−1)) − a(n) =
  a(n)·(a(n) − a(n−1)), that is t_n = a(n)·t_(n−1), with t_0 = a(1) − a(0) = 1.
- So the loop keeps s = a(n) and a = t_n: it prints s, then s → s + t_n =
  a(n+1) and t → t·a(n+1) = t_(n+1). It starts from s = a(0) = 0, t_0 = 1.
- The t_n are [A001697](../A001697/) (t_(n+1) = t_n·(t_0 + ⋯ + t_n)), so
  this also shows a(n) = A001697(0) + ⋯ + A001697(n−1).

**Notes**

- Exact integers, so the program is right for every n. a(16) has 4115
  digits; a(17) is over Python's 4300-digit limit for printing ints, where
  the program stops with a ValueError.
- The b-file (14 terms) prints at once; the bar is the whole b-file in
  60 s.
- The recurrence as written, `a,b=0,1` / `while[print(a)]:a,b=b,b*(1+b-a)`,
  is 39 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001696), CC BY-SA 4.0.
