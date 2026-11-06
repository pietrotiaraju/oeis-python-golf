# A000257

> Number of rooted bicubic maps: a(n) = (8*n-4)*a(n-1)/(n+2) for n >= 2, a(0) = a(1) = 1.
> — [OEIS A000257](https://oeis.org/A000257)

Offset 0: 1, 1, 3, 12, 56, 288, 1584, 9152, 54912, 339456, 2149888, 13891584, …

### Python 3 — 41 bytes

```python
a=k=1
while[print(a)]:a=a*8*k//(k+5);k+=2
```

**How it works**

- The recurrence is (n+2)·a(n) = (8n−4)·a(n−1). With k = 2n−1 the ratio
  (8n−4)/(n+2) becomes 8k/(k+5), so `k` steps by 2 from 1 and `a=k=1` sets
  both at once. The loop prints a(n−1) and then moves to a(n).
- n = 1 is the one step where the recurrence does not hold: it would give
  4/3, but a(1) = 1. Floor division gives `1*8*1//6` = 1, so the same line
  covers it with no special case. From n = 2 on, a(n−1)·(8n−4) =
  (n+2)·a(n) exactly, so `//` loses nothing.
- Longer forms: with m = n+2 the step is a(n) = 8a − 20a/m, but
  `8*a-20*a//m` floors only the fraction and gives 2 at n = 1;
  `-20*a//m+8*a` floors the whole value and works, at 43 bytes because of
  the start `a=1;m=3`. Two counters, `a=a*k//j;k+=8;j+=1`, save a byte in
  the loop and lose four in `a=1;k=4;j=3`.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (201 terms) prints at once; the program stops after a(4771), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000257), CC BY-SA 4.0.
