# A000723

> Invertible Boolean functions of n variables.
> — [OEIS A000723](https://oeis.org/A000723)

Offset 1: 1, 3, 840, 54486432000, 68523655451482690147713024000000, …

### Python 3 — 56 bytes

```python
f=k=n=1
while 1:exec("f*=k;k+=1;"*k);f//=n;n+=1;print(f)
```

**How it works**

- These are the classes of invertible maps {0,1}ⁿ → {0,1}ⁿ under
  translations x ↦ x ⊕ c of the domain and permutations of the variables
  of the range (an OEIS comment). The group has 2ⁿ·n! elements and acts
  freely (a map f with σ∘f∘τ = f for (τ,σ) ≠ 1 would make a
  fixed-point-free τ conjugate to a σ that fixes the point 0), so
  a(n) = (2ⁿ)!/(2ⁿ·n!) = (2ⁿ−1)!/n!, the OEIS formula.
- `f` is (k−1)!/(n−1)! with k = 2ⁿ⁻¹. The `exec` string, repeated k times
  (k taken before it runs), multiplies `f` by k, k+1, …, 2k−1 and doubles
  k, giving (2k−1)!/(n−1)!; `f//=n` then divides by n exactly, since the
  result is the integer a(n).

**Notes**

- a(11) = 2047!/11! has about 5870 digits, past CPython's 4300-digit
  int-to-str limit, so the program prints 10 terms and then stops with a
  `ValueError` (an interpreter limit).
- The b-file has 8 terms (n = 1..8); all of them are the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000723), CC BY-SA 4.0.
