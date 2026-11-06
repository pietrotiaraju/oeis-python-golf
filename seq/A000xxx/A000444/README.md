# A000444

> Number of partially labeled rooted trees with n nodes (3 of which are labeled).
> — [OEIS A000444](https://oeis.org/A000444)

Offset 3: 9, 64, 326, 1433, 5799, 22224, 81987, 293987, 1031298, 3555085, …

### Python 3 — 203 bytes

```python
r=[n:=0,1]
while 1:
 m=-n
 if m>2:
  B=1<<(5*m+8);S=sum(r[k]*B**k for k in range(1,m+1))
  print(S**3*(9-8*S+2*S*S)*pow(1-S,-5,B**(m+1))//B**m%B)
 n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
```

**How it works**

- Let T(x)=Σₖ≥₁ t(k)xᵏ count ordinary unlabeled rooted
  trees, [A000081](../A000081/). The generating function on
  the OEIS page is F(x)=T^3(9−8T+2T²)/(1−T)⁵.
  Since T has leading term x, the first output index is 3.
- r[k] stores t(k), starting with t(0)=0, t(1)=1.
  The rooted-tree Euler-transform recurrence is

  (N−1)t(N)=Σₖ₌₁ᴺ⁻¹ k·t(k)·Σⱼ≥₁ t(N−jk),

  where negative indices contribute zero. In the last line
  of the code, n=−(N−1) and d=−k: `r[-d]` selects
  t(k), `r[d::d]` gives the inner backward slice, and the
  negative signs in the numerator and divisor cancel.
- At the loop's start m=−n is the degree to extract. The
  tree list already includes t(m+1); only entries through m
  are packed as `S=sum(r[k]*B**k for k in range(1,m+1))`.
  The extra tree entry belongs to the recurrence, not the output.
- Substitute this packed T(B) into the numerator. Since S is
  divisible by B, 1−S has a modular inverse modulo B^(m+1).
  `pow(1-S,-5,B**(m+1))` computes the inverse fifth power,
  and `//B**m%B` reads its m-th base-B digit after multiplication.
- `if m>2` skips the degrees below the first possible
  labeled term. At m=3, the leading term
  9T^3 gives the initial 9.
  Later coefficients include both the tree-series substitutions
  and the denominator expansion.

**Why carries cannot change the answer**

- A rooted tree with k vertices has a plane ordering, so its
  count is at most the number of plane rooted trees, less than
  4ᵏ. Therefore T(1/32)≤Σₖ≥₁(1/8)ᵏ=1/7<1/3.
- Replace the numerator's negative coefficients by their absolute
  values to obtain a coefficientwise majorant. Evaluated at
  T=1/3 it is 107/32, less than 128. Hence each
  final coefficient f_j is less than 128·32ʲ.
- For j≤m this is smaller than B=256·32ᵐ, the chosen
  `1<<(5*m+8)`. The coefficients are nonnegative counts,
  so no lower base-B digits can carry into the answer digit.
  Degrees above m vanish modulo B^(m+1).

**Notes**

- Exact integer arithmetic: modular inversion implements formal
  series division, rather than a numerical approximation at x=B.
  A new base is chosen at each output degree.
- The tree list uses O(m) entries, while the packed integer
  and modulus have O(m²) bits. Increasing these integer sizes
  makes higher coefficients expensive even though the tree
  recurrence itself is comparatively short.
- [A000485](../A000485/) changes the labeling expression;
  [A000432](../A000432/) applies the same packing method to
  a series-parallel network series.
- The b-file has 648 terms (indices 3 through 650). The bar is the
  first 100 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 203 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000444), CC BY-SA 4.0.
