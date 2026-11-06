# A000238

> Number of oriented trees with n nodes.
> — [OEIS A000238](https://oeis.org/A000238)

Offset 1: 1, 1, 3, 8, 27, 91, 350, 1376, 5743, 24635, 108968, 492180, …

The g.f. is R(x) − R(x)², where R(x) is the g.f. of the rooted oriented trees,
[A000151](../A000151/).

### Python 3 — 119 bytes

```python
W=[n:=-1,2]
while[print(sum(map(int.__mul__,W,W[::-1]))//-4)]:W+=sum(d*W[-d]*sum(W[d:0:d])for d in range(n,0))//n,;n-=1
```

**How it works**

- Rooted at a vertex there are R(x) oriented trees, rooted at an edge there
  are R(x)²: cutting the root edge u → v leaves a rooted tree at u and one
  at v, and the arrow says which is which. No automorphism can swap the two
  ends of an arrow, so the dissymmetry count of unrooted trees is just
  A = R − R² (the OEIS formula), with no R(x²) term.
- Doubling turns R into something easier. T = 2R satisfies
  T(x) = 2x·exp(Σₖ T(xᵏ)/k), so with T = Σ t(m)xᵐ the logarithmic
  derivative gives the same recurrence as for [A000081](../A000081/), with no
  factor 2 and the seed t(1) = 2:

  m·t(m+1) = Σ_{d=1..m} d·t(d)·(t(m+1−d) + t(m+1−2d) + ⋯).

- Shifting by one makes the answer a square. With W = T − 1,
  1 − W² = 2T − T² = 4R − 4R² = 4A, so for m ≥ 1

  a(m) = −(W₀W_m + W₁W_{m−1} + ⋯ + W_mW₀)/4, with W₀ = −1 and W_k = t(k).

  `sum(map(int.__mul__,W,W[::-1]))//-4` is that sum. Keeping R itself
  (with R₀ = 0) and printing `R[-1]-sum(map(int.__mul__,R,R[::-1]))` is
  121 bytes.
- `W` holds −1, t(1), …, t(m), and `n` is −m; the starting −1 does double
  duty as W₀ and as n. With d = −m, …, −1, `W[-d]` is t(|d|) and
  `W[d:0:d]` is t(m+1−|d|), t(m+1−2|d|), …; the stop `0` keeps W₀ = −1 out
  of the recurrence. Both the d's and n are negative, so `//n` gives t(m+1)
  with the right sign.

**Notes**

- Exact integer arithmetic, so the program is right for every n: the sum is
  m·t(m+1) before `//n`, and 4·a(m) before `//-4`.
- A term costs about m·log m big-integer additions and m products, so the
  whole b-file (1000 terms) prints in about 2 s and about 2600 terms come out
  in a minute on a laptop. The bar is the whole b-file in 60 s.
- a(n) grows like 5.65ⁿ, so it reaches Python's 4300-digit int-to-str limit
  near n = 5700; the program is correct beyond that once the limit is lifted.
- `math.sumprod(W,W[::-1])` saves 13 bytes on the product but the import
  costs 18.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 119 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000238), CC BY-SA 4.0.
