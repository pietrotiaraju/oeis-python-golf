# A000460

> Eulerian numbers (Euler's triangle: column k=3 of A008292, column k=2 of A173018).
> — [OEIS A000460](https://oeis.org/A000460)

Offset 3: 1, 11, 66, 302, 1191, 4293, 14608, 47840, 152637, 478271, …

### Python 3 — 50 bytes

```python
n=3
while 1:print(3**n-(n+1)*2**n+n*(n+1)//2);n+=1
```

**How it works**

- With the zero-based descent convention, an Eulerian number
  A(n,r) counts permutations with exactly r positions i such that
  p_i>p_(i+1). This page uses r=2; column numbering in
  other Eulerian triangles can be shifted by one.
- Eulerian inclusion-exclusion gives
  A(n,r)=Σⱼ₌₀ʳ⁺¹ (−1)ʲ C(n+1,j)(r+1−j)ⁿ.
  At n≥3 the last term is zero, leaving

  **a(n)=3ⁿ−(n+1)2ⁿ+C(n+1,2).**

- Expand the small binomial coefficients directly in integers.

  `n*(n+1)//2` is C(n+1,2), always an integer because
  one of two consecutive integers is even.

- The smallest possible size is n=3, when only the
  decreasing permutation has 2 descents. The initial
  output is therefore 1, with no earlier zeros printed.

**Notes**

- Exact integer powers and products; divisibility of the binomial
  products makes the floor divisions exact, including after
  applying the expression's subtraction signs.
- [A000498](../A000498/) is the adjacent Eulerian
  column. The direct formula avoids storing an expanding row
  of the full Eulerian triangle.
- There is a constant number of integer temporaries. The terms
  grow exponentially and eventually reach Python 3.11+'s default
  4300-digit output conversion limit, an interpreter limit.
- The b-file has 998 terms (indices 3 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000460), CC BY-SA 4.0.
