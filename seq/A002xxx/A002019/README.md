# A002019

> a(n) = a(n-1) - (n-1)(n-2)a(n-2).
> — [OEIS A002019](https://oeis.org/A002019)

Offset 0: 1, 1, 1, -1, -7, 5, 145, -5, -6095, -5815, 433025, 956375, -46676375, -172917875, …

### Python 3 — 44 bytes

```python
a=b=n=1
while[print(a)]:a,b=b,b-n*~-n*a;n+=1
```

**How it works**

- The pair (a, b) is (a(n − 1), a(n)). Each pass prints a and moves on
  with b = a(n + 1) = a(n) − n(n − 1)·a(n − 1), which is the title's
  recurrence shifted by one; `~-n` is n − 1.
- It starts at n = 1 with a = b = 1 = a(0) = a(1). The coefficient
  n(n − 1) is 0 at n = 1, so the first step gives a(2) = a(1) = 1 as the
  data says, and one assignment `a=b=n=1` sets up everything.
- The e.g.f. is exp(arctan x): the recurrence is the coefficient form of
  (1 + x²)·y′ = y.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002019), CC BY-SA 4.0.
