# A000635

> Number of paraffins C_n H_{2n} X Y with n carbon atoms.
> — [OEIS A000635](https://oeis.org/A000635)

Offset 0: 0, 1, 2, 5, 12, 31, 80, 210, 555, 1479, …

### Python 3 — 172 bytes

```python
m=1
while X:=9**m:M=X**m;V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%M//6for k in range(m)]+P for _ in P];print((2*pow(2-X*(V[1]**2+V[2]),-1,M)-1)%M*X//M);m+=1
```

**How it works**

- B(x) = 1 + x·S₃(B) counts alkyl radicals with B₀ = 1 for a hydrogen
  ([A000598](../A000598/)), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6.
  G = S₂(B) = (B² + B(x²))/2 counts unordered pairs of radicals, so
  P = x·G counts a carbon carrying two radicals ([A000642](../A000642/)).
- A path from a substituent X into the molecule is a sequence of such
  carbons, so 1/(1 − P) counts the X-chains (including the empty one, X
  sitting directly on the next carbon).
- X and Y sit at the two ends of a nonempty chain of such carbons (the
  same carbon when the chain has length 1), so
  **a(n) = [xⁿ] P/(1 − P) = [xⁿ] (1/(1 − P) − 1)**, the entry's B/(1 − B)
  with B the A000642 series shifted to start at x.
- The series are packed into integers in base X = 9^m, as on the
  [A000602](../A000602/) page: `V[k]` is B(x^k) evaluated at X and cut
  below X^m, so `V[2*k]`, `V[3*k]` are B(x^(2k)), B(x^(3k)) with no
  substitution, and the padding entries `+P` (k ≥ m) are 1, which is right
  modulo x^m. Each pass applies B(x^k) = 1 + x^k·S₃(B)(x^k); shifting by
  X^k before the cut keeps only digits of degree < m, all multiples of 6,
  so `//6` is exact digit by digit. Each pass fixes at least one more
  digit, and there are more than m passes.
- With f = `V[1]**2+V[2]` = 2G at X, 1/(1 − P) = 2/(2 − X·f); the −1
  clears digit 0.
- x ↦ X is a ring map from Z[½][x]/(x^m) to Z/X^m (X is odd, so 2 is a
  unit), so a rational function of the packed series is computed by
  `pow(…,-1,M)` modulo M = X^m: the denominators are ≡ 2 (mod X), hence
  invertible. When all coefficients of degree < m of the result lie in
  [0, X), the residue is exactly the packed truncated series and
  `%M*X//M` reads digit m−1.

**Notes**

- Base width: a tree with child counts at most 3 is fixed by its child
  counts in preorder, so Bⱼ ≤ 4^(j−1) for j ≥ 1, and the update digits
  are at most 6Bₘ₋₁ < 9^m. Gⱼ ≤ 4ʲ by the same preorder argument
  (root degree ≤ 2), so P ≤ x/(1 − 4x) and 1/(1 − P) ≤ (1 − 4x)/(1 − 5x)
  coefficientwise: aⱼ ≤ 5^(j−1) < 9^m.
- Each term is recomputed from scratch with integers of about 3m² bits.
- The reference file has the 201 terms of the OEIS b-file;
  the bar is 40 terms in 60 s (it printed 50 terms in 60 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000635), CC BY-SA 4.0.
