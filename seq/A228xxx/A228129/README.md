# A228129

> a(n) = number of semistandard Young tableau families, headed by a father SSYT, containing daughter SSYT of shape equal to once-trimmed father's shape, so that union of families equals all SSYT with sum of entries n.
> — [OEIS A228129](https://oeis.org/A228129)

Offset 1: 1, 1, 2, 3, 5, 9, 13, 22, 34, 53, 80, 125, 184, 279, 413, …

### Python 3 — 91 bytes

```python
R=[n:=1]
while 1:R+=sum(d//2*d*sum(R[d::d])for d in range(-n,-1))//n,;print(R[-1]or 1);n+=1
```

**How it works**

- A family is a father tableau together with every tableau obtained from it by
  deleting one box. In his answer to the
  [MathOverflow question](https://mathoverflow.net/questions/129854) behind this
  sequence, Richard Stanley shows that the families exist and that the number
  of fathers with entry sum n is the coefficient of qⁿ in
  (1 − q)·Σ_{λ ≠ ∅} s_λ(q, q², q³, …), where s_λ(q, q², …) counts the SSYT of
  shape λ by entry sum. So the program is correct for every n by that theorem.
- Littlewood's identity Σ_λ s_λ(x) = ∏ᵢ 1/(1 − xᵢ) · ∏_{i<j} 1/(1 − xᵢxⱼ) at
  xᵢ = qⁱ gives G(q) = ∏_{m≥1} (1 − qᵐ)^−⌈m/2⌉, the counts of all SSYT
  ([A003293](https://oeis.org/A003293)). Then
  (1 − q)(G − 1) = P(q) − 1 + q with P(q) = ∏_{m≥2} (1 − qᵐ)^−⌈m/2⌉, so
  a(n) = [qⁿ]P(q) for n ≥ 2 and a(1) = [q¹]P(q) + 1 = 1.
- P is an Euler transform, so its coefficients c satisfy
  n·c(n) = Σ_{k=2..n} k⌈k/2⌉ · Σ_{j≥1} c(n − jk), with c(0) = 1. `R` holds
  c(0), …, c(n − 1) oldest first; for d = −k, `R[d::d]` is
  c(n − k), c(n − 2k), …, and `d//2*d` is (−⌈k/2⌉)(−k) = k⌈k/2⌉. The range
  stops at −2 because the m = 1 factor is gone.
- c(1) = 0 is the only zero coefficient (every n ≥ 2 is a sum of 2s and 3s, and
  P contains 1/(1 − q²) and 1/(1 − q³)), so `R[-1]or 1` adds the missing 1
  exactly at n = 1 while `R` keeps the true c(1) = 0 for the recurrence.

**Notes**

- The Mathematica line on the OEIS entry is the one from A228125 and sums all
  SSYT, which gives A003293; the data follow the father count above
  (a(n) = A003293(n) − A003293(n − 1) for n ≥ 2).
- The b-file is synthesized from the 36 terms of the entry; the program prints
  about 8500 terms in 60 seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A228129), CC BY-SA 4.0.
