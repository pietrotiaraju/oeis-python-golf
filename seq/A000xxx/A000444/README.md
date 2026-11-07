# A000444

> Number of partially labeled rooted trees with n nodes (3 of which are labeled).
> — [OEIS A000444](https://oeis.org/A000444)

Offset 3: 9, 64, 326, 1433, 5799, 22224, 81987, 293987, 1031298, 3555085, …

A partially labeled rooted tree has n nodes, 3 of which carry the labels
1, 2, 3 while the rest are unlabeled; trees are counted up to isomorphisms
that keep the labels.

### Python 3 — 169 bytes

```python
R=[2,1,1];n=3
while 1:S=B=9**n;[S:=(S+c)*B for c in R];print(S**3*(9-8*S+2*S*S)*pow(1-S,-5,B**-~n)//B**n%B);R=[sum(d*R[d]*sum(R[~d::-d])for d in range(-n,0))//-n]+R;n+=1
```

**How it works**

- Let T(x) = Σ t(k)xᵏ = x + x² + 2x³ + 4x⁴ + … count unlabeled rooted
  trees ([A000081](../A000081/)). The program evaluates the generating
  function on the OEIS page, T³(9 − 8T + 2T²)/(1 − T)⁵, as it stands.
- R lists t(n), t(n−1), …, t(1), newest first. The Euler-transform
  recurrence n·t(n+1) = Σ_{e=1..n} e·t(e)·Σ_{j≥1} t(n+1−je) gives the
  next one: for d = −e, `R[d]` is t(e) and `R[~d::-d]`, which is
  `R[e-1::e]`, is t(n+1−e), t(n+1−2e), …; the minus signs of `d` and
  `//-n` cancel, and the division is exact. The new value goes in front.
- Packing: x ↦ B = 9ⁿ is a ring map from power series modulo x^(n+1) to
  the integers modulo B^(n+1). The Horner walrus `S:=(S+c)*B` over R,
  started at S = B, leaves S = B^(n+1) + Σ t(k)Bᵏ ≡ T(B): the start is
  a multiple of B and gets multiplied by Bⁿ, so it vanishes. Since
  1 − S ≡ 1 (mod B) it is invertible, and `pow(1-S,-5,B**-~n)` is
  (1 − T)⁻⁵ at B. The product is ≡ Σ_{j≤n} a(j)Bʲ modulo B^(n+1). It is
  not reduced, but it is positive (2S² − 8S + 9 > 0), and `//B**n%B`
  reads digit n of its remainder modulo B^(n+1) all the same, as long as
  no coefficient up to xⁿ reaches B.
- No carries: with U = T/(1 − T), 1/(1 − T) = 1 + U and T(1 + U) = U, so
  the function is U³(9(1 + U)² − 8U(1 + U) + 2U²) = U³(3U² + 10U + 9),
  with nonnegative coefficients. Rooted trees are at most plane rooted
  trees, so t(k) ≤ C_{k−1} < 4^(k−1), and at x = 1/9 the series give
  T ≤ (1/9)/(1 − 4/9) = 1/5, U ≤ 1/4 and U³(3U² + 10U + 9) ≤ 187/1024
  < 1. So a(j) < 9ʲ ≤ B for j ≤ n.
- `S=B=9**n` costs no more than `n=S=3`, but a leftover S from the
  previous term is not a multiple of B, so the reset is needed.

**Notes**

- Measured alternatives: the previous record, 174 bytes, used the
  U-polynomial, `U=pow(1-S*B,-1,B**-~n)-1` with U³(3U² + 10U + 9) and the
  Horner step `S*B+c`; in V = 1/(1 − T) the polynomial is
  (V − 1)³(3V² + 4V + 2), which ties with that. Keeping t(0) = 0 at the
  end of R, so that the leftover S of the previous term vanishes without
  a reset (`n=S=3`, Horner step `S*B+c`, multiplier `e*R[~e]`), is 170
  bytes, but the leftover grows and only 68 terms come out in 10 s.
  Earlier: `S=0;` in the loop, 176; the list oldest first with a separate
  modulus M, 181; the base 2^(5n+8) with the unpacked numerator, 203.
- Exact integer arithmetic, so the program is right for every n.
- 100 terms in about 5 s here, 173 terms in 60 s. The b-file has 648
  terms (up to a(650)); the bar is 100 terms in 10 s.
- a(n) has about 0.477n digits (a(650) has 310), so the 4300-digit
  int-to-str limit comes only near n = 9000, far beyond the program's
  reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 203 | first entry |
| 2026-11-07 | Python 3 | 174 | U = T/(1-T), base 9^n, Horner walrus over a newest-first tree list |
| 2026-11-07 | Python 3 | 169 | the OEIS form T³(9−8T+2T²)(1−T)⁻⁵ as it stands, Horner step `(S+c)*B` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000444), CC BY-SA 4.0.
