# A000142

> Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of permutations of n letters).
> — [OEIS A000142](https://oeis.org/A000142)

Offset 0: 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, …

### Python 3 — 31 bytes

```python
f=n=1
while[print(f)]:f*=n;n+=1
```

**How it works**

- `f` holds n! and `n` the next factor. Each round prints `f`, then
  multiplies by `n` and moves `n` on, so the output is 0! = 1, 1! = 1·1,
  2! = 1·2, …
- `while[print(f)]:` is one byte under `while 1:print(f);`: `print`
  returns `None`, but the list `[None]` is not empty, so it is true.

**Notes**

- The b-file (101 terms, 0! to 100!) prints in well under a second; the bar
  is the whole b-file in 60 s.
- 1558! is the last factorial with at most 4300 digits. Python 3.11+ refuses
  to print a longer int, so the program stops with a `ValueError` after
  1559 terms; that is the interpreter limit, not the program.
- Folding the counter into the product costs bytes: `f*=(n:=n+1)` is 11
  bytes against 9 for `f*=n;n+=1` (the parentheses are compulsory), and
  moving `n:=n+1` into the `while` list needs `f=1;n=0` at the start.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000142), CC BY-SA 4.0.
