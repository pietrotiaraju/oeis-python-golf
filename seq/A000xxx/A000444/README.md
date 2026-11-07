# A000444

> Number of partially labeled rooted trees with n nodes (3 of which are labeled).
> — [OEIS A000444](https://oeis.org/A000444)

Offset 3: 9, 64, 326, 1433, 5799, 22224, 81987, 293987, 1031298, 3555085, …

A partially labeled rooted tree has n nodes, 3 of which carry the labels
1, 2, 3 while the rest are unlabeled; trees are counted up to isomorphisms
that keep the labels.

### Python 3 — 174 bytes

```python
R=[2,1,1];n=3
while 1:S=B=9**n;[S:=S*B+c for c in R];U=pow(1-S*B,-1,B**-~n)-1;print(U**3*(3*U*U+10*U+9)//B**n%B);R=[sum(d*R[d]*sum(R[~d::-d])for d in range(-n,0))//-n]+R;n+=1
```

**How it works**

- Let T(x) = Σ t(k)xᵏ = x + x² + 2x³ + 4x⁴ + … count unlabeled rooted
  trees ([A000081](../A000081/)). The generating function on the OEIS
  page is T³(9 − 8T + 2T²)/(1 − T)⁵. With U = T/(1 − T), so that
  T = U/(1 + U) and 1/(1 − T) = 1 + U, it is
  U³(9 − 8T + 2T²)(1 + U)² = U³(9(1 + U)² − 8U(1 + U) + 2U²)
  = U³(3U² + 10U + 9), the polynomial in the program.
- R lists t(n), t(n−1), …, t(1), newest first. The Euler-transform
  recurrence n·t(n+1) = Σ_{e=1..n} e·t(e)·Σ_{j≥1} t(n+1−je) gives the
  next one: for d = −e, `R[d]` is t(e) and `R[~d::-d]`, which is
  `R[e-1::e]`, is t(n+1−e), t(n+1−2e), …; the minus signs of `d` and
  `//-n` cancel, and the division is exact. The new value goes in front.
- Packing: x ↦ B = 9ⁿ is a ring map from power series modulo x^(n+1) to
  the integers modulo B^(n+1). The Horner walrus over R, started at
  S = B, leaves S = B^(n+1) + Σ t(k)B^(k−1), so S·B ≡ T(B). Since
  1 − S·B ≡ 1 (mod B) it is invertible, `pow(1-S*B,-1,B**-~n)` is
  1/(1 − T) at B, and U is that minus 1. Then U³(3U² + 10U + 9) ≡
  Σ_{j≤n} a(j)Bʲ modulo B^(n+1), and `//B**n%B` reads digit n, as long as
  no coefficient up to xⁿ reaches B.
- No carries: rooted trees are at most plane rooted trees, so
  t(k) ≤ C_{k−1} < 4^(k−1), and at x = 1/9 the series give
  T ≤ (1/9)/(1 − 4/9) = 1/5, U ≤ 1/4 and U³(3U² + 10U + 9) ≤ 187/1024
  < 1. All the coefficients are nonnegative, so a(j) < 9ʲ ≤ B for j ≤ n.
- Starting S at B (`S=B=9**n`) costs no more than `n=S=3`, which would
  let S carry over from the previous term: that leftover also vanishes
  modulo B^(n+1), but it grows by n digits of B every term.

**Notes**

- Measured alternatives: the carried-over S (`n=S=3`), also 174 bytes but
  about twice as slow (around 10 s for 100 terms here, too close to the
  bar); `S=0;` in the loop, 176; the list oldest first with a separate
  modulus M, 181. In V = 1/(1 − T) the polynomial is
  (V − 1)³(3V² + 4V + 2), which drops the `-1` but ties. The previous
  program (203 bytes) used the base 2^(5n+8) and `pow(1-S,-5,…)`.
- Exact integer arithmetic, so the program is right for every n.
- 100 terms in about 5 s here, 176 terms in 60 s. The b-file has 648
  terms (up to a(650)); the bar is 100 terms in 10 s.
- a(n) has about 0.477n digits (a(650) has 310), so the 4300-digit
  int-to-str limit comes only near n = 9000, far beyond the program's
  reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 203 | first entry |
| 2026-11-07 | Python 3 | 174 | U = T/(1-T), base 9^n, Horner walrus over a newest-first tree list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000444), CC BY-SA 4.0.
