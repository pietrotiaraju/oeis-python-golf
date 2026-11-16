# A001808

> Expansion of 1/((1+x)*(1-x)^12).
> — [OEIS A001808](https://oeis.org/A001808)

Offset 0: 1, 11, 67, 297, 1068, 3300, 9076, 22748, 52834, 115126, 237590, 467842, …

### Python 3 — 46 bytes

```python
a=0;c=n=1
while[print(a:=c-a)]:c+=11*c//n;n+=1
```

**How it works**

- Multiplying the generating function by 1 + x leaves 1/(1 − x)¹², whose
  coefficients are the binomials C(n + 11, 11). So a(n) + a(n − 1) =
  C(n + 11, 11) for every n ≥ 0 (with a(−1) = 0): each term is the next
  binomial minus the term before, `a:=c-a`.
- `c` is C(n + 11, 11) for the term being printed; it starts at
  C(11, 11) = 1. Pascal's rule gives C(n + 11, 11) = C(n + 10, 11) +
  C(n + 10, 10), and the second binomial is C(n + 10, 11)·11/n. So
  `c+=11*c//n` moves c from n − 1 to n, and the floor division is exact
  because 11·c/n is that binomial, an integer. `n` starts at 1, the index
  of the next term.
- `a` starts at 0 = a(−1); the list `[…]` around the print is non-empty,
  so the loop never ends.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Partial fractions give a(n) = P(n) + (−1)ⁿ/2¹² with P a polynomial of
  degree 11; written with integer coefficients it is far longer than the
  recurrence.
- The family 1/((1 + x)(1 − x)ᵏ): [A001752](../A001752/) (k = 5),
  [A001753](../A001753/) (k = 6), [A001769](../A001769/) (k = 7),
  [A001779](../A001779/) (k = 8), [A001780](../A001780/) (k = 9),
  [A001781](../A001781/) (k = 10), [A001786](../A001786/) (k = 11),
  A001808 (k = 12).
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001808), CC BY-SA 4.0.
