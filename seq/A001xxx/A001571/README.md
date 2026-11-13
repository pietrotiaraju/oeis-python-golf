# A001571

> a(n) = 4*a(n-1) - a(n-2) + 1, with a(0) = 0, a(1) = 2.
> — [OEIS A001571](https://oeis.org/A001571)

Offset 0: 0, 2, 9, 35, 132, 494, 1845, 6887, 25704, 95930, 358017, 1336139, …

### Python 3 — 35 bytes

```python
a=b=0
while[print(a)]:b+=a-~a;a-=~b
```

**How it works**

- `b` holds a(n) − a(n−1) − 1 when a(n) is printed. The recurrence gives
  a(n+1) − a(n) − 1 = 3a(n) − a(n−1) = (a(n) − a(n−1) − 1) + 2a(n) + 1,
  so `b+=a-~a` (a−~a = 2a+1) moves `b` one step, and then `a-=~b` adds
  b + 1, which makes a = a(n+1).
- The start: the recurrence run backwards gives a(−1) = 4·0 − 2 + 1 = −1,
  so b = 0 − (−1) − 1 = 0, and `a=b=0`.

**Notes**

- 2a(n) + 1 = [A001834](https://oeis.org/A001834)(n) = 1, 5, 19, 71, … satisfies the
  homogeneous recurrence x(n) = 4x(n−1) − x(n−2); printing half of it,
  `a=b=1` / `while[print(b//2)]:a+=b;b+=2*a`, is 36 bytes, and the plain
  tuple `a,b=0,2` / `a,b=b,4*b-a+1` is 37. A search over two-variable
  programs (one or two in-place statements, tuple updates, walrus prints)
  found nothing below 35.
- The entry carries the keyword "changed"; its name and its data
  (0, 2, 9, 35, …) agree, and the program follows both.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001571), CC BY-SA 4.0.
