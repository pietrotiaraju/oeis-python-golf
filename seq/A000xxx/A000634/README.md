# A000634

> Number of glycols with n carbon atoms.
> — [OEIS A000634](https://oeis.org/A000634)

Offset 2: 1, 2, 6, 14, 38, 97, 260, 688, 1856, 4994, …

### Python 3 — 215 bytes

```python
m=3
while X:=9**m:M=X**m;V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%M//6for k in range(m)]+P for _ in P];print((2*pow(u:=2-X*(V[1]**2+V[2]),-1,M)+(4-u)*pow(2-X*X*(V[2]**2+V[4]),-1,M)+u)%M*X//M>>1);m+=1
```

**How it works**

- B(x) = 1 + x·S₃(B) counts alkyl radicals with B₀ = 1 for a hydrogen
  ([A000598](../A000598/)), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6.
  G = S₂(B) = (B² + B(x²))/2 counts unordered pairs of radicals, so
  P = x·G counts a carbon carrying two radicals ([A000642](../A000642/)).
- A path from a substituent X into the molecule is a sequence of such
  carbons, so 1/(1 − P) counts the X-chains (including the empty one, X
  sitting directly on the next carbon).
- Two identical X on different carbons form a chain of at least two
  carbons up to reversal. Sequences up to reversal count
  T = (1/(1 − P) + (1 + P)/(1 − P(x²)))/2 (all sequences plus
  palindromes, as in [A000636](../A000636/)); removing the one-carbon
  chains, **a(n) = [xⁿ](T − P)**, the entry's A000636(n) − A000642(n+1).
- The series are packed into integers in base X = 9^m, as on the
  [A000602](../A000602/) page: `V[k]` is B(x^k) evaluated at X and cut
  below X^m, so `V[2*k]`, `V[3*k]` are B(x^(2k)), B(x^(3k)) with no
  substitution, and the padding entries `+P` (k ≥ m) are 1, which is right
  modulo x^m. Each pass applies B(x^k) = 1 + x^k·S₃(B)(x^k); shifting by
  X^k before the cut keeps only digits of degree < m, all multiples of 6,
  so `//6` is exact digit by digit. Each pass fixes at least one more
  digit, and there are more than m passes.
- With f = 2G at X, u = 2 − X·f (= 2(1 − P)) and v = 2 − X²·f(x²):
  2T = 2/u + (4 − u)/v and 2P = 2 − u, so the printed
  2/u + (4 − u)/v + u is 2(T − P) + 2. The +2 only touches digit 0.
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
  (root degree ≤ 2), so 1/(1 − P) ≤ (1 − 4x)/(1 − 5x) coefficientwise
  and the read digits 4, 0, 2a₂, …, 2aₘ₋₁ stay below 2·5^m < 9^m.
- Each term is recomputed from scratch with integers of about 3m² bits.
- The reference file has the 29 terms of the OEIS b-file;
  the bar is all 29 in 60 s (it needs about 3 s here and printed 48 terms in 60 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 215 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000634), CC BY-SA 4.0.
