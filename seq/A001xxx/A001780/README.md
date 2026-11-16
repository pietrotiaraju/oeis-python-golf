# A001780

> Expansion of 1/((1+x)*(1-x)^9).
> — [OEIS A001780](https://oeis.org/A001780)

Offset 0: 1, 8, 37, 128, 367, 920, 2083, 4352, 8518, 15792, 27966, 47616, …

### Python 3 — 45 bytes

```python
a=0;c=n=1
while[print(a:=c-a)]:c+=8*c//n;n+=1
```

**How it works**

- Multiplying the generating function by 1 + x leaves 1/(1 − x)⁹, whose
  coefficients are the binomials C(n + 8, 8). So a(n) + a(n − 1) =
  C(n + 8, 8) for every n ≥ 0 (with a(−1) = 0): each term is the next
  binomial minus the term before, `a:=c-a`.
- `c` is C(n + 8, 8) for the term being printed; it starts at
  C(8, 8) = 1. Pascal's rule gives C(n + 8, 8) = C(n − 1 + 8, 8) +
  C(n − 1 + 8, 7), and the second binomial is C(n − 1 + 8, 8)·8/n.
  So `c+=8*c//n` moves c from n − 1 to n, and the floor division is exact
  because 8·c/n is that binomial, an integer. `n` starts at 1, the index of
  the next term.
- `a` starts at 0 = a(−1); the list `[…]` around the print is non-empty, so
  the loop never ends.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Partial fractions give a(n) = P(n) + (−1)ⁿ/2⁹ with P a polynomial of
  degree 8, so a(n) = ⌊P(n) + 1/2⌋; written with integer coefficients it is
  longer than the recurrence here.
  Even in s = (n + 5)², where P has degree 4, it stays longer.
- The family 1/((1 + x)(1 − x)ᵏ): [A001752](../A001752/) (k = 5), [A001753](../A001753/) (k = 6), [A001769](../A001769/) (k = 7), [A001779](../A001779/) (k = 8), A001780 (k = 9), [A001781](../A001781/) (k = 10), [A001786](../A001786/) (k = 11).
- The b-file has 2001 terms (n = 0 to 2000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001780), CC BY-SA 4.0.
