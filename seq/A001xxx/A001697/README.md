# A001697

> a(n+1) = a(n)*(a(0) + ... + a(n)), a(0) = 1.
> — [OEIS A001697](https://oeis.org/A001697)

Offset 0: 1, 1, 2, 8, 96, 10368, 108615168, 11798392572168192, …

### Python 3 — 31 bytes

```python
a=s=1
while[print(a)]:a*=s;s+=a
```

**How it works**

- The loop keeps a = a(n) and s = a(0) + ⋯ + a(n). It prints a, then
  a → a·s = a(n+1) and s → s + a(n+1). Both start at 1 (a(0) = 1, and the
  sum of the first term is 1).

**Notes**

- Exact integers, so the program is right for every n. a(15) has 4115
  digits; a(16) is over Python's 4300-digit limit for printing ints, where
  the program stops with a ValueError.
- The b-file (13 terms) prints at once; the bar is the whole b-file in
  60 s.
- The partial sums are [A001696](../A001696/), whose program is this loop
  printing s instead.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001697), CC BY-SA 4.0.
