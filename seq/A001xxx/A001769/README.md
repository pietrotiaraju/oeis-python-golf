# A001769

> Expansion of 1/((1+x)*(1-x)^7).
> — [OEIS A001769](https://oeis.org/A001769)

Offset 0: 1, 6, 22, 62, 148, 314, 610, 1106, 1897, 3108, 4900, 7476, 11088, …

### Python 3 — 45 bytes

```python
a=0;c=n=1
while[print(a:=c-a)]:c+=6*c//n;n+=1
```

**How it works**

- Multiplying the generating function by 1 + x leaves 1/(1 − x)⁷, whose
  coefficients are the binomials C(n + 6, 6). So a(n) + a(n − 1) =
  C(n + 6, 6) for every n ≥ 0 (with a(−1) = 0): each term is the next
  binomial minus the term before, `a:=c-a`.
- `c` is C(n + 6, 6) for the term being printed; it starts at
  C(6, 6) = 1. Pascal's rule gives C(n + 6, 6) = C(n − 1 + 6, 6) +
  C(n − 1 + 6, 5), and the second binomial is C(n − 1 + 6, 6)·6/n.
  So `c+=6*c//n` moves c from n − 1 to n, and the floor division is exact
  because 6·c/n is that binomial, an integer. `n` starts at 1, the index of
  the next term.
- `a` starts at 0 = a(−1); the list `[…]` around the print is non-empty, so
  the loop never ends.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Partial fractions give a(n) = P(n) + (−1)ⁿ/128 with P a polynomial of
  degree 6. With s = (n + 4)², 5760·P = 2s(s − 4)(2s − 17) − 45, so
  a(n) = ⌊s(s − 4)(2s − 17)/2880⌋, but as a program,
  `m=4\nwhile[print((s:=m*m)*(s-4)*(2*s-17)//2880)]:m+=1`, that is
  52 bytes. For k = 5 the same idea wins: [A001752](../A001752/), 37 bytes.
- The family 1/((1 + x)(1 − x)ᵏ): [A001752](../A001752/) (k = 5), [A001753](../A001753/) (k = 6), A001769 (k = 7), [A001779](../A001779/) (k = 8), [A001780](../A001780/) (k = 9), [A001781](../A001781/) (k = 10), [A001786](../A001786/) (k = 11).
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001769), CC BY-SA 4.0.
