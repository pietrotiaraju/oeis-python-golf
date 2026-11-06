# A000498

> Eulerian numbers (Euler's triangle: column k=4 of A008292, column k=3 of A173018).
> — [OEIS A000498](https://oeis.org/A000498)

Offset 4: 1, 26, 302, 2416, 15619, 88234, 455192, 2203488, 10187685, 45533450, …

### Python 3 — 73 bytes

```python
n=4
while 1:print(4**n-(n+1)*3**n+n*(n+1)*2**(n-1)-(n-1)*n*(n+1)//6);n+=1
```

**How it works**

- With the zero-based descent convention, an Eulerian number
  A(n,r) counts permutations with exactly r positions i such that
  p_i>p_(i+1). This page uses r=3; column numbering in
  other Eulerian triangles can be shifted by one.
- Eulerian inclusion-exclusion gives
  A(n,r)=Σⱼ₌₀ʳ⁺¹ (−1)ʲ C(n+1,j)(r+1−j)ⁿ.
  At n≥4 the last term is zero, leaving

  **a(n)=4ⁿ−(n+1)3ⁿ+C(n+1,2)2ⁿ−C(n+1,3).**

- Expand the small binomial coefficients directly in integers.

  `n*(n+1)*2**(n-1)` is C(n+1,2)2ⁿ, with the factor
  2 in the denominator absorbed into the power. The final
  `(n-1)*n*(n+1)//6` is C(n+1,3).

- The smallest possible size is n=4, when only the
  decreasing permutation has 3 descents. The initial
  output is therefore 1, with no earlier zeros printed.

**Notes**

- Exact integer powers and products; divisibility of the binomial
  products makes the floor divisions exact, including after
  applying the expression's subtraction signs.
- [A000460](../A000460/) is the adjacent Eulerian
  column. The direct formula avoids storing an expanding row
  of the full Eulerian triangle.
- There is a constant number of integer temporaries. The terms
  grow exponentially and eventually reach Python 3.11+'s default
  4300-digit output conversion limit, an interpreter limit.
- The b-file has 197 terms (indices 4 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000498), CC BY-SA 4.0.
