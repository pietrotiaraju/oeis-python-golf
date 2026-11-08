# A001053

> a(n+1) = n*a(n) + a(n-1) with a(0)=1, a(1)=0.
> — [OEIS A001053](https://oeis.org/A001053)

Offset 0: 1, 0, 1, 2, 7, 30, 157, 972, 6961, 56660, 516901, 5225670, …

### Python 3 — 41 bytes

```python
a=b=n=1
while[print(a)]:n-=1;b-=n*a;a=b-a
```

**How it works**

- When a(k) is printed, `a` = a(k) and `b` = a(k−1) + a(k), the sum of two
  neighbours.
- The counter runs downwards: after `n-=1` it is −k, so `b-=n*a` adds
  k·a(k), and `b` becomes a(k−1) + a(k) + k·a(k) = a(k) + a(k+1). Then
  `a=b-a` leaves a(k+1), and the pair has the same shape one step on.
- The start is k = 0: a(−1) = 0 (from a(1) = 0·a(0) + a(−1)), so `a` =
  a(0) = 1, `b` = a(−1) + a(0) = 1, and the counter must reach 0 on the
  first pass, so it starts at 1: `a=b=n=1`. Exact integers.

**Notes**

- This is the [A001040](../A001040/) program (same recurrence, a(0) = 0,
  a(1) = 1, 40 bytes) with the difference taken after the print instead of
  inside it. The walrus form `while[print(a:=b-a)]:n-=1;b-=n*a` would need
  a = a(−1) = 0 and b = 1 here (`a=0;b=n=1`, 42 bytes), so for this start
  the plain print is one byte shorter.
- Counting up ties: `a=b=n=1` / `while[print(a)]:a=b-a;b+=n*a;n+=1` (41).
  The tuple form `a=n=1;b=0` / `while[print(a)]:a,b=b,a+n*b;n+=1` is 42.
- A search over loops with a counter (print of `a`, `b` or a walrus
  difference, one or two in-place statements with multipliers `n`, `~n`,
  `-~n`, `~-n`, the counter step anywhere, start values solved exactly)
  found nothing shorter.
- a(n) ~ I₁(2)·(n−1)!, so Python's 4300-digit int-to-str limit stops the
  program at a(1560), the first term with more than 4300 digits (4303),
  after printing a(0) to a(1559).
- The b-file has 101 terms (a(0) to a(100), 157 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001053), CC BY-SA 4.0.
