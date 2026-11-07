# A000641

> Number of paraffins C_n H_{2n-1} X_3 with n carbon atoms.
> — [OEIS A000641](https://oeis.org/A000641)

Offset 0: 0, 1, 2, 5, 14, 39, 109, 312, 890, 2552, …

### Python 3 — 223 bytes

```python
m=1
while X:=9**m:M=X**m;V=P=[1]*6*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%M//6for k in range(m)]+P for _ in P];s,t,u=[2*pow(2-X**k*(V[k]**2+V[2*k]),-1,M)for k in(1,2,3)];print(X*V[1]*(s**3+3*s*t+2*u)%M*X//M//6);m+=1
```

**How it works**

- B(x) = 1 + x·S₃(B) counts alkyl radicals with B₀ = 1 for a hydrogen
  ([A000598](../A000598/)), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6.
  G = S₂(B) = (B² + B(x²))/2 counts unordered pairs of radicals, so
  P = x·G counts a carbon carrying two radicals ([A000642](../A000642/)).
- A path from a substituent X into the molecule is a sequence of such
  carbons, so 1/(1 − P) counts the X-chains (including the empty one, X
  sitting directly on the next carbon).
- The three X's paths meet at one carbon, which carries the remaining
  radical (possibly H) and an unordered triple of X-chains:
  **a(n) = [xⁿ] x·B·S₃(1/(1 − P))**, the entry's formula.
- The series are packed into integers in base X = 9^m, as on the
  [A000602](../A000602/) page: `V[k]` is B(x^k) evaluated at X and cut
  below X^m, so `V[2*k]`, `V[3*k]` are B(x^(2k)), B(x^(3k)) with no
  substitution, and the padding entries `+P` (k ≥ m) are 1, which is right
  modulo x^m. Each pass applies B(x^k) = 1 + x^k·S₃(B)(x^k); shifting by
  X^k before the cut keeps only digits of degree < m, all multiples of 6,
  so `//6` is exact digit by digit. Each pass fixes at least one more
  digit, and there are more than m passes.
- `s,t,u` are 1/(1 − P(x^k)) = 2/(2 − X^k·(B(x^k)² + B(x^(2k)))) for
  k = 1, 2, 3, so X·B(X)·(s³ + 3st + 2u) has the digits 6aⱼ; the padding
  `[1]*6*m` makes `V[6]` exist already at m = 1.
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
  (root degree ≤ 2), so B and 1/(1 − P) are at most 1/(1 − 5x)
  coefficientwise, and S₃(F) ≤ F³ gives 6aⱼ ≤ 6[x^(j−1)](1 − 5x)^(−4)
  < 9^m.
- Each term is recomputed from scratch with integers of about 3m² bits.
- The reference file has the 28 terms of the OEIS b-file;
  the bar is all 28 in 60 s (it needs about 3 s here and printed 45 terms in 60 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 223 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000641), CC BY-SA 4.0.
