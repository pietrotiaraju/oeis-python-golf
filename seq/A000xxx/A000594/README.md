# A000594

> Ramanujan's tau function (or Ramanujan numbers, or tau numbers).
> — [OEIS A000594](https://oeis.org/A000594)

Offset 1: 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643, -115920, …

### Python 3 — 83 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=24*sum(d*sum(a[d::d])for d in range(n,0))//-n,
```

**How it works**

- Ramanujan's generating function is
  Σₘ≥₁τ(m)xᵐ=x∏ₖ≥₁(1−xᵏ)²⁴. Write
  A(x)=∏ₖ≥₁(1−xᵏ)²⁴=Σₘ≥₀a(m)xᵐ; then a(m)=τ(m+1).
- Formal logarithmic differentiation gives
  xA′(x)/A(x)=−24Σₖ≥₁kxᵏ/(1−xᵏ). Comparing coefficients yields

  **m·a(m)=−24Σₖ₌₁ᵐ k·Σⱼ₌₁^⌊m/k⌋ a(m−jk)**.

- The list begins with a(0)=1. Before computing coefficient m,
  it contains a(0),…,a(m−1), and the code's n is −m.
  For d=−k, `a[d::d]` supplies a(m−k),a(m−2k),… .
- The sum over negative d is the negative of the positive-k sum.
  Multiplying it by 24 and dividing by −n=m therefore gives
  a(m) with exactly the required sign. The division is exact
  because A is an integer-coefficient product.
- Print the newest coefficient before each update. The initial 1
  is τ(1), so the output begins at the OEIS offset 1.

**Notes**

- All operations use signed integers; there is no floating point
  approximation, integer factorization or table of known tau values.
- One coefficient list is stored. The slice sums use O(m log m)
  entries per new coefficient, with exact cancellation. This trades
  the sparse triangular recurrence for shorter source.
- Python's integer-to-string conversion limit can eventually apply.
- The reference file has 16091 terms. The unchanged verification
  bar is 5000 terms in 60 s; every term produced is checked.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 150 | first entry |
| 2026-11-06 | Python 3 | 83 | use the logarithmic derivative of the discriminant product |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000594), CC BY-SA 4.0.
