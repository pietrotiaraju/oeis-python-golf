# A000627

> Number of non-stereoisomeric paraffins with n carbon atoms.
> — [OEIS A000627](https://oeis.org/A000627)

Offset 1: 1, 1, 1, 2, 3, 5, 7, 13, 20, 35, …

### Python 3 — 102 bytes

```python
Q=1,;n=0
while 1:Q+=0,0,0,sum(map(int.__mul__,Q[::4],Q[2*n::-2]));n+=1;print((Q[-1]+Q[2*n]+Q[n-1])//2)
```

**How it works**

- Non-stereoisomeric paraffins are the alkanes with no asymmetric
  carbon (every carbon has two identical substituents). A(x) = ΣAₖxᵏ
  counts the alkyl radicals with that property
  ([A000621](../A000621/)): A = 1 + x·A(x)·A(x²).
- Root the carbon skeleton at its centroid: one carbon whose four
  branches all have fewer than n/2 carbons, or, for even n, one bond
  with n/2 carbons on each side. Inside a branch, every carbon sees the
  centroid side as a group with more than n/2 carbons, different from
  its other three groups; so each branch is a radical counted by A.
  The centroid carbon needs two equal branches among four. Multisets of
  four with a repeated element have cycle index (p₁²p₂ + p₄)/2; the
  centroid bond joins an unordered pair, (Aₙ/₂² + Aₙ/₂)/2.
- Only one branch can reach n/2 carbons, and the other three then
  contribute [x^(n−1−j)]A·A(x²) = Aₙ₋ⱼ. Removing those big branches
  from [xⁿ⁻¹]A(x)²A(x²) = [xⁿ]A(A − 1) leaves Aₙ − [2 | n]Aₙ/₂², and
  everything adds up to

  **a(n) = (Aₙ + [2 | n]Aₙ/₂ + [4 | n−1]A₍ₙ₋₁₎/₄)/2**,

  that is, a(x) = (A(x) + A(x²) + x·A(x⁴))/2 for n ≥ 1.
- `Q` stores A with three zeros between terms, Q[4e] = Aₑ. Then
  `Q[2*n]` is [2 | n]Aₙ/₂ and `Q[n-1]` is [4 | n−1]A₍ₙ₋₁₎/₄ with no
  divisibility tests, and `Q[-1]` is Aₙ.
- The recurrence Aₙ₊₁ = Σⱼ Aⱼ·[x^(n−j)]A(x²) pairs `Q[::4]` (A₀,…,Aₙ)
  with `Q[2*n::-2]` (the coefficients of A(x²) from xⁿ down to x⁰).

**Notes**

- Exact integer arithmetic, O(n) per term; the formula was checked
  against all 42 terms of the OEIS entry.
- The reference file has the 42 terms of the OEIS entry (no longer
  b-file there); the bar is all 42 in 60 s, which takes well under a
  second.
- [A000626](../A000626/) = [A000628](../A000628/) − A000627.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 102 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000627), CC BY-SA 4.0.
