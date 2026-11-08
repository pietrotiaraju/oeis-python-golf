# A001003

> Schroeder's second problem (generalized parentheses); also called super-Catalan numbers or little Schroeder numbers.
> — [OEIS A001003](https://oeis.org/A001003)

Offset 0: 1, 1, 3, 11, 45, 197, 903, 4279, 20793, 103049, 518859, 2646723, 13648869, …

### Python 3 — 55 bytes

```python
a=b=n=1
while[print(a)]:n+=1;a,b=b,6*b-a-3*(3*b-a)//-~n
```

**How it works**

- The little Schröder numbers satisfy (n+1)s(n) = 3(2n−1)s(n−1) −
  (n−2)s(n−2) for n ≥ 2, the D-finite recurrence of their algebraic g.f.
  σ = 1 + xσ(2σ − 1) (it is in the entry).
- The right side is (n+1)(6s(n−1) − s(n−2)) − 3(3s(n−1) − s(n−2)), so

  **s(n) = 6s(n−1) − s(n−2) − 3(3s(n−1) − s(n−2))/(n+1)**,

  where the quotient is an integer because everything else is; `//-~n`
  divides by n + 1 with no parentheses.
- `(a,b)` = (s(n−2), s(n−1)) and the program prints `a`; s(0) = s(1) = 1,
  so `a=b=n=1` is the start and the first pass computes s(2).

**Notes**

- Exact integer arithmetic; correct for every n by the recurrence.
- Thousands of terms per second; the bar is the whole b-file (1313 terms)
  in 60 s.
- The same recurrence written with t = 3s(n−1) − s(n−2) as the second
  state, `t=-b+3*(b:=3*b+t-3*t//m)`, ties at 55 bytes because it needs
  `b=1;t=m=2`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001003), CC BY-SA 4.0.
