# A002020

> a(n+1) = a(n) - n*(n-1)*a(n-1), with a(n) = 1 for n <= 3.
> — [OEIS A002020](https://oeis.org/A002020)

Offset 0: 1, 1, 1, 1, -5, -17, 83, 593, -2893, -36101, 172195, 3421285, -15520165, -467129785, …

### Python 3 — 50 bytes

```python
a=b=n=1
while[print(a)]:a,b=b,b-n*~-n*a*(n>2);n+=1
```

**How it works**

- The recurrence a(n + 1) = a(n) − n(n − 1)·a(n − 1) starts at n = 3:
  a(0) = a(1) = a(2) = a(3) = 1 (with the recurrence at n = 2, a(3) would
  be −1).
- The pair (a, b) is (a(n − 1), a(n)); each pass prints a and sets
  b = a(n + 1) = a(n) − n(n − 1)·a(n − 1)·[n > 2]. The factor `(n>2)` is
  False for the first two steps, so a(2) = a(1) and a(3) = a(2), and True
  from then on.
- A polynomial coefficient cannot replace it: one that equals n(n − 1) for
  every n ≥ 3 is n(n − 1) itself, which is 2, not 0, at n = 2. Printing
  the first terms separately costs more than the 6 bytes of `*(n>2)`.

**Notes**

- Same loop as [A002019](../A002019/), which has the recurrence from the
  start.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002020), CC BY-SA 4.0.
