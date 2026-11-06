# A000267

> Integer part of square root of 4n+1.
> — [OEIS A000267](https://oeis.org/A000267)

Offset 0: 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, …

### Python 3 — 37 bytes

```python
n=c=2
while[print(c-1)]:n+=4;c+=c*c<n
```

**How it works**

- `c` holds a(n)+1 and `n` holds 4n+2. When n goes up by one, ⌊√(4n+1)⌋
  goes up by at most one (consecutive squares from 4 on are at least 5
  apart), and it does so exactly when (a+1)² ≤ 4n+1.
- Squares are 0 or 1 mod 4, so (a+1)² ≤ 4n+1 is the same as
  (a+1)² < 4n+2: the strict test `c*c<n` against 4n+2 needs no `=`.
- Holding a+1 instead of a makes the square just `c*c`, and it lets both
  counters start at 2, so `n=c=2` is one assignment. Printing `c-1` costs
  two bytes, but `~k*~k<=n` with `k` = a(n) costs three more than `c*c<n`
  and needs `n=k=1` with `<=` (38 bytes).
- `while[print(c-1)]:` loops forever (a one-element list is truthy) and is a
  byte under `while 1:print(c-1);`.

**Notes**

- Integer arithmetic only, no `math.isqrt` and no floats, so it is correct
  for every n. It prints the whole b-file (10001 terms) at once; the bar is
  the whole b-file in 60 s.
- Other routes tried: the A000196 counter `n=k=1` / `k+=~k*~k<=n` and the
  negated counter `n=d=-2` / `print(~d)` / `d-=d*d<-n` are 38 bytes;
  printing each value k ⌈k/2⌉ times with `exec("print(k);"*(k+1>>1))`
  is 42; `math.isqrt(n)` over n = 1, 5, 9, … is 49.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000267), CC BY-SA 4.0.
