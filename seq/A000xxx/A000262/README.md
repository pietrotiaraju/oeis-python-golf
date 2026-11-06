# A000262

> Number of "sets of lists": number of partitions of {1,...,n} into any number of lists, where a list means an ordered subset.
> — [OEIS A000262](https://oeis.org/A000262)

Offset 0: 1, 1, 3, 13, 73, 501, 4051, 37633, 394353, 4596553, …

### Python 3 — 46 bytes

```python
a=c=1;n=0
while[print(a)]:c=a+n*c;a=c+n*a;n+=1
```

**How it works**

- The e.g.f. is y = exp(x/(1−x)), so (1−x)²·y′ = y. Reading off the
  coefficient of xⁿ/n! gives a(n+1) − 2n·a(n) + n(n−1)·a(n−1) = a(n), that is
  a(n+1) = (2n+1)·a(n) − n(n−1)·a(n−1) for n ≥ 1, the OEIS recurrence.
- Written directly, with two terms of state, it costs 51 bytes
  (`a,b=b,b*(n-~n)-n*~-n*a`). Instead the program splits it into two
  first-order steps with an auxiliary c(n) = a(n+1) − n·a(n):
  c(n) = a(n) + n·c(n−1) and a(n+1) = c(n) + n·a(n).
  The second is the definition of c; substituting the definition into the
  first gives back exactly the recurrence above, so the two steps are
  equivalent to it. Each step is one multiply-add, `c=a+n*c;a=c+n*a`.
- c(n) is [A002720](https://oeis.org/A002720) (1, 2, 7, 34, 209, …), the
  denominators of Peter Bala's continued fraction for a(n+1) on the OEIS
  page; the program never prints it.
- At n = 0 both steps multiply the old values by 0, so c(0) = a(0) = 1 and
  a(1) = c(0) = 1 whatever c held before: the start `a=c=1;n=0` only needs c
  to exist.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (445 terms) prints at once; the program stops after a(1548), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000262), CC BY-SA 4.0.
