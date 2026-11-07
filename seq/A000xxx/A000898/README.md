# A000898

> a(n) = 2*(a(n-1) + (n-1)*a(n-2)) for n >= 2 with a(0) = 1.
> — [OEIS A000898](https://oeis.org/A000898)

Offset 0: 1, 2, 6, 20, 76, 312, 1384, 6512, 32400, 168992, 921184, 5222208, …

### Python 3 — 44 bytes

```python
a=1;n=b=0
while[print(a)]:a,b=2*a+n*b,a;n+=2
```

**How it works**

- The defining recurrence a(n+1) = 2a(n) + 2n·a(n−1), with `a`, `b` =
  a(n), a(n−1).
- `n` holds 2n (it steps by 2), so the factor 2 of the second term is
  free: `2*a+n*b` instead of `2*(a+n*b)`, 2 bytes shorter.
- For n = 0 the second term is multiplied by 0, so `b` may start at any
  value: `a=1;n=b=0` gives a(1) = 2.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 2602, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000898), CC BY-SA 4.0.
