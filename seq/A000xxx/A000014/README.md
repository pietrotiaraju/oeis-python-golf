# A000014

> Number of series-reduced trees with n nodes.
> — [OEIS A000014](https://oeis.org/A000014)

Offset 0: 0, 1, 1, 0, 1, 1, 2, 2, 4, 5, 10, 14, 26, 42, 78, 132, 249, …

Series-reduced trees (homeomorphically irreducible trees) have no node of
degree 2.

### Python 3 — 167 bytes

```python
A=[0,1];F=A*1;n=0
while[print(F[n]+(A[n//2]*(-1)**n-sum(A[i]*F[n-i]for i in range(n)))//2)]:n+=1;F+=sum(d*A[d]*sum(F[-d::-d])for d in range(1,n+1))//n,;A+=F[-1]-A[-1],
```

**How it works**

- `A` counts planted series-reduced trees ([A001678](https://oeis.org/A001678)):
  rooted trees with a stem edge above the root, so that the root's degree
  also counts the stem. A node has any number of branches except exactly one,
  so A = x·(E − A), where E = ∏ (1 − xᵏ)^(−Aₖ) counts multisets of planted
  trees.
- `F` holds (1 + x)·A, which is x·E: F₀ = 0 and Fₙ₊₁ = Eₙ. The body gets Eₙ
  from the Euler-transform recurrence n·Eₙ = Σ d·A_d·Σₖ E_(n−dk). Since F is
  E shifted by one place, the inner sum is just the slice `sum(F[-d::-d])`.
  Then Aₙ₊₁ = Fₙ₊₁ − Aₙ.
- The unrooted count comes from the generating function on the OEIS entry
  (Harary and Palmer, in Somos's form):
  a(n) = [xⁿ] ((1 − x)·A(x²) + (1 + x)·A·(2 − A))/2. With F = (1 + x)·A this
  is Fₙ + ((−1)ⁿ·A_⌊n/2⌋ − Σ Aᵢ·Fₙ₋ᵢ)/2, which is the printed expression.
- The lists run one step ahead of n (they start at A₁ = F₁ = 1), so the
  division by n never meets n = 0 and a(0) = 0 needs no special case.
  `F=A*1` is a copy, not a second name for the same list.

**Notes**

- Every step is exact integer arithmetic: both divisions are exact.
- Each term costs about n log n steps; the whole b-file (1001 terms) takes a
  few seconds.
- A first version with a separate E list, a double loop for the Euler
  transform and `print(0)` up front was 174 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 167 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000014), CC BY-SA 4.0.
