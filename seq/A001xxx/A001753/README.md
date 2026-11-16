# A001753

> Expansion of g.f. 1/((1+x)*(1-x)^6).
> — [OEIS A001753](https://oeis.org/A001753)

Offset 0: 1, 5, 16, 40, 86, 166, 296, 496, 791, 1211, 1792, 2576, 3612, 4956, …

### Python 3 — 45 bytes

```python
a=0;c=n=1
while[print(a:=c-a)]:c+=5*c//n;n+=1
```

**How it works**

- Multiplying the generating function by 1 + x leaves 1/(1 − x)⁶, whose
  coefficients are the binomials C(n + 5, 5). So a(n) + a(n − 1) =
  C(n + 5, 5) for every n ≥ 0 (with a(−1) = 0): each term is the next
  binomial minus the term before, `a:=c-a`.
- `c` is C(n + 5, 5) for the term being printed; it starts at
  C(5, 5) = 1. Pascal's rule gives C(n + 5, 5) = C(n − 1 + 5, 5) +
  C(n − 1 + 5, 4), and the second binomial is C(n − 1 + 5, 5)·5/n.
  So `c+=5*c//n` moves c from n − 1 to n, and the floor division is exact
  because 5·c/n is that binomial, an integer. `n` starts at 1, the index of
  the next term.
- `a` starts at 0 = a(−1); the list `[…]` around the print is non-empty, so
  the loop never ends.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Partial fractions give a(n) = P(n) + (−1)ⁿ/2⁶ with P a polynomial of
  degree 5, so a(n) = ⌊P(n) + 1/2⌋; written with integer coefficients it is
  longer than the recurrence here.
  For even k the polynomial is odd in m = 2n + 7 and its numerator does
  not split into short factors (7680·P = m(m⁴ − 30m² + 149)).
- The family 1/((1 + x)(1 − x)ᵏ): [A001752](../A001752/) (k = 5), A001753 (k = 6), [A001769](../A001769/) (k = 7), [A001779](../A001779/) (k = 8), [A001780](../A001780/) (k = 9), [A001781](../A001781/) (k = 10), [A001786](../A001786/) (k = 11).
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001753), CC BY-SA 4.0.
