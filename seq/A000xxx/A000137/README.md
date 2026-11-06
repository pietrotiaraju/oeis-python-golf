# A000137

> Series-parallel numbers.
> — [OEIS A000137](https://oeis.org/A000137)

Offset 1: 1, 2, 6, 18, 58, 186, 614, 2034, 6818, 22970, 77858, 264970, …

The g.f. is x(1+S)/(1−S), where S is the g.f. of
[A000084](https://oeis.org/A000084) (series-parallel networks with n edges).

### Python 3 — 132 bytes

```python
R=[n:=1];v=2,
while[print(v[-1]-1//n)]:v+=sum(map(int.__mul__,R:=[sum(R+[j*R[~j]*sum(R[j-1::j])for j in range(1,n)])//n]+R,v)),;n+=1
```

**How it works**

- Write 1 + S = Σ eₙ xⁿ, so e₀ = 1 and eₙ = A000084(n). By the formula on
  A000084, 1 + S = ∏ₖ (1−xᵏ)^(−cₖ) with c = [A000669](https://oeis.org/A000669),
  and c₁ = 1, cₖ = eₖ/2 for k ≥ 2.
- Taking x·d/dx of the logarithm gives n·eₙ = Σₖ₌₁ⁿ (Σ_{j|k} j·c_j)·e_{n−k}.
  Writing j·c_j = (j·e_j + [j = 1])/2, the j = 1 extra contributes
  ½·(e₀ + ⋯ + e_{n−1}), and the term j = k = n is n·eₙ/2, which moves to the
  left. What is left is

  n·eₙ = Σ_{i<n} eᵢ + Σ_{j=1}^{n−1} j·e_j·(e_{n−j} + e_{n−2j} + ⋯).

- `R` holds e_{n−1}, …, e₀, newest first. Then `R[~j]` is e_j,
  `R[j-1::j]` is e_{n−j}, e_{n−2j}, …, and `sum(R+[…])` adds Σ eᵢ to the
  double sum. The new eₙ is put at the front of `R`.
- For the output, let v = 2/(1−S), i.e. v₀ = 2 and vₙ = Σₖ₌₁ⁿ eₖ·v_{n−k}.
  Since x(1+S)/(1−S) = x(v − 1), a(1) = v₀ − 1 = 1 and a(n+1) = vₙ.
- With `R` = [eₙ, …, e₀] and `v` = [v₀, …, v_{n−1}],
  `map(int.__mul__,R,v)` pairs eₙ·v₀, …, e₁·v_{n−1} (it stops at the shorter
  sequence), so its sum is vₙ. `print(v[-1]-1//n)` subtracts 1 only for the first
  term.

**Notes**

- Each step costs about n·log n big-integer operations, so the program prints
  the 1000 terms of the b-file in under 2 s and about 2900 terms in a minute.
  The bar is the whole b-file (1000 terms) in 60 s.
- a(n) grows like 3.56ⁿ, so it reaches Python's 4300-digit int-to-str limit
  near n = 7800; the program is correct beyond that once the limit is lifted.
- Starting from `v=[1]` and adding eₙ back (`sum(…,R[0])`) instead of
  printing `v[-1]-1//n` costs the same 133 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 133 | first entry |
| 2026-11-06 | Python 3 | 132 | use a tuple for the initial v state |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000137), CC BY-SA 4.0.
