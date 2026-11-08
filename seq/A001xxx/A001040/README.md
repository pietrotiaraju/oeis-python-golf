# A001040

> a(n+1) = n*a(n) + a(n-1) with a(0)=0, a(1)=1.
> — [OEIS A001040](https://oeis.org/A001040)

Offset 0: 0, 1, 1, 3, 10, 43, 225, 1393, 9976, 81201, 740785, 7489051, …

### Python 3 — 40 bytes

```python
a=b=n=1
while[print(a:=b-a)]:n-=1;b-=n*a
```

**How it works**

- Before the print of a(k), `a` = a(k−1) and `b` = a(k−1) + a(k), the sum of
  two neighbours (the [A000045](../A000045/) trick). The walrus `a:=b-a`
  leaves a(k) in `a` and prints it.
- The counter runs downwards: after `n-=1` it is −k, so `b-=n*a` adds
  k·a(k), and `b` becomes a(k−1) + a(k) + k·a(k) = a(k) + a(k+1). That is
  the invariant for the next pass, with only one variable updated and no
  tuple swap.
- The start is k = 0: a(−1) = 1 (from a(1) = 0·a(0) + a(−1)), so `a` = 1,
  `b` = a(−1) + a(0) = 1, and the counter must reach 0 on the first pass,
  so it starts at 1. All three are 1: `a=b=n=1`. Exact integers.

**Notes**

- Counting down is what makes the start values equal: the same loop with
  `b+=n*a;n+=1` needs n = 0 first (`a=b=1;n=0`, 42 bytes), and the tuple form
  `a=0;b=n=1` / `while[print(a)]:a,b=b,a+n*b;n+=1` is 42 too.
- A search over loops with a counter (print of `a`, `b` or a walrus
  difference, one or two in-place statements with multipliers `n`, `~n`,
  `-~n`, `~-n`, the counter step anywhere, start values solved exactly)
  found nothing shorter.
- The twin [A001053](../A001053/) (same recurrence, a(0) = 1, a(1) = 0) is
  this program with the walrus moved out of the print, 41 bytes.
- a(n) ~ I₀(2)·(n−1)!, so Python's 4300-digit int-to-str limit stops the
  program at a(1560), the first term with more than 4300 digits (4303),
  after printing a(0) to a(1559).
- The b-file has 451 terms (a(0) to a(450), 998 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001040), CC BY-SA 4.0.
