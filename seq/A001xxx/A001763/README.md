# A001763

> a(n) = (3n+3)!/(2n+3)!.
> — [OEIS A001763](https://oeis.org/A001763)

Offset -1: 1, 1, 6, 72, 1320, 32760, 1028160, 39070080, 1744364160, 89513424000, …

### Python 3 — 48 bytes

```python
a=u=1
while[print(a)]:a=a*u*-~u*9//(4*u+14);u+=3
```

**How it works**

- a(n) = (3n+3)!/(2n+3)!, so
  a(n)/a(n−1) = (3n+3)(3n+2)(3n+1)/((2n+3)(2n+2)) = 3(3n+1)(3n+2)/(2(2n+3)).
- The update that makes a(n) uses u = 3n + 1, applied before `u+=3`:
  3n + 2 = u + 1 and 2(2n+3) = (4u+14)/3, so the ratio is
  9u(u+1)/(4u+14) and the step is `a=a*u*-~u*9//(4*u+14)`. The quotient is
  the integer a(n), so the floor division is exact.
- Updating before the increment lets the loop start with `a=u=1`: a(−1) = 1
  is printed first, and the first step (u = 1) gives a(0) = 1.

**Notes**

- Exact integer arithmetic, correct for every n. a(1234) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program.
- Incrementing first needs `a=1;u=-2` (51 bytes). With j = 3n + 4,
  (3n+3)!/(2n+3)! = P(j, n+1)/j, and
  `from math import*` / `j=1` / `while[print(perm(j,j//3)//j)]:j+=3` is
  56 bytes.
- The b-file has 102 terms (a(−1) to a(100)); the bar is the whole b-file
  in 60 s, which prints instantly. [A001762](../A001762/) is the unrooted
  count.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001763), CC BY-SA 4.0.
