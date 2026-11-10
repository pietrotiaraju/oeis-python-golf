# A001464

> Expansion of e.g.f. exp(-x - (1/2)*x^2).
> — [OEIS A001464](https://oeis.org/A001464)

Offset 0: 1, -1, 0, 2, -2, -6, 16, 20, -132, -28, 1216, -936, -12440, 23672, 138048, …

### Python 3 — 42 bytes

```python
a=1;b=n=0
while[print(a)]:a,b=n*b-a,a;n-=1
```

**How it works**

- The e.g.f. f = exp(−x − x²/2) satisfies f′ = −(1 + x)·f. Comparing the
  coefficients of xⁿ/n! gives **a(n+1) = −a(n) − n·a(n−1)**, with
  a(0) = 1.
- The counter runs downwards: when a(k+1) is computed, `n` holds −k, so
  `n*b-a` = −k·a(k−1) − a(k) = a(k+1). `a` and `b` hold a(k) and
  a(k−1), and the pair shifts with `a,b=n*b-a,a`.
- At k = 0 the old `b` is multiplied by 0, so any start value works:
  `a=1;b=n=0`.

**Notes**

- Counting up, `a,b=-a-n*b,a;n+=1`, is 43 bytes: the negative counter
  absorbs one minus sign.
- (−1)ⁿ·a(n) has e.g.f. exp(x − x²/2): it is the number of involutions
  of n points with an even number of 2-cycles minus those with an odd
  number (see [A001465](../A001465/)).
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at a(2848).
- The b-file has 808 terms (n = 0 to 807); all of them print in well under
  a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001464), CC BY-SA 4.0.
