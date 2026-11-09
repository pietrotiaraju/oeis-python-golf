# A001352

> a(0) = 1, a(1) = 6, a(2) = 24; for n>=3, a(n) = 4a(n-1) - a(n-2).
> — [OEIS A001352](https://oeis.org/A001352)

Offset 0: 1, 6, 24, 90, 336, 1254, 4680, 17466, 65184, 243270, 907896, 3388314, …

### Python 3 — 40 bytes

```python
a=b=-6
while[print((a:=a-b)or 1)]:b-=2*a
```

**How it works**

- The generating function is 1 + 6x/(1 − 4x + x²), so a(n) = 6·U(n) for
  n ≥ 1, where U = [A001353](../A001353/) = 0, 1, 4, 15, 56, … satisfies
  U(n+1) = 4·U(n) − U(n−1); only a(0) = 1 is off the recurrence (it
  would be 6·U(0) = 0).
- The loop is the A001353 program scaled by 6: `b` holds minus the first
  difference, so the walrus `a:=a-b` steps `a` from 6·U(n−1) to 6·U(n),
  and `b-=2*a` is the recurrence. Started at `a=b=-6` (one step before
  n = 0), it gives 0, 6, 24, 90, …, and `or 1` prints the 0 as a(0) = 1.

**Notes**

- Also 40 bytes: `a=0;b=6` / `while[print(a or 1)]:a+=b;b+=2*a`,
  `a=b=2` / `while[print(b-a or 1)]:a+=b;b+=2*a`, and
  `a,b=1,6` / `while[print(a)]:a,b=b,4*b-a+1&-2` (the `+1&-2` rounds the
  one odd value 4·6 − 1 = 23 up to 24; every later term is even).
- Some nonlinear touch is needed: a(0), a(1), a(2) = 1, 6, 24 already break
  the order-2 recurrence that every later term follows.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (a(0) to a(200)); the whole of it prints
  instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001352), CC BY-SA 4.0.
