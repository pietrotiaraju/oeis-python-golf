# A001569

> Sum_{n>=0} a(n)*x^n/n!^2 = BesselI(0,2*(1-exp(x))^(1/2)).
> — [OEIS A001569](https://oeis.org/A001569)

Offset 0: 1, −1, −1, 2, 37, 329, 1501, −31354, −1451967, −39284461, …

### Python 3 — 79 bytes

```python
P=[s:=1]
while[print(s)]:k=d=len(P);P=[s:=-P[0]]+[s:=s+d*(k:=k-1)*p for p in P]
```

**How it works**

- **Stirling form.** I₀(2√z) = Σ_k z^k/k!², and (e^x − 1)^k/k! =
  Σ_n S₂(n, k)·xⁿ/n!, so with z = 1 − e^x the definition gives
  b(n) = a(n)/n! = Σ_k (−1)^k·S₂(n, k)/k! (Jovovic's formula on the
  entry).
- **A transposed Stirling table.** Let L(0, r) = (−1)^r/r! and
  L(j+1, r) = L(j, r+1) + r·L(j, r). Then L(j, 0) = b(j): with
  ℓ_j(y) = Σ_r L(j, r)·y^r/r! the rule is ℓ_(j+1) = (1 + y)·ℓ_j′, and
  with y = e^x − 1 the operator (1 + y)·d/dy is d/dx, so
  ℓ_j(e^x − 1) is the j-th derivative of
  ℓ₀(e^x − 1) = Σ_r (−1)^r(e^x − 1)^r/r!², whose value at x = 0 is
  b(j).
- **Antidiagonals.** The program fills the table along
  d = j + r, scaled to integers: X_j = d!·L(j, d − j). Then X₀ = (−1)^d
  and X_j = X_(j−1) + d·(d − j)·P_(j−1), where P is the previous
  antidiagonal (scaled by (d − 1)!). The last step has weight 0, so the
  last entry X_d = d!·b(d) = a(d) equals the one before, and it is
  where the running sum `s` ends.
- **The code.** `P=[s:=1]` is antidiagonal 0 and prints a(0) = 1.
  Antidiagonal d − 1 has d entries, so each pass sets `k=d=len(P)`
  (1 byte under keeping a counter); `-P[0]` flips the sign of the
  first entry ((−1)^d), and `d*(k:=k-1)` counts the weights down
  d(d − 1), …, d·0 (9 bytes under `d*(d+~i)` with `enumerate`).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (20 terms, up to a(19)) prints at once; the program
  reaches a(1013) in under a second, where the next term passes
  Python's 4300-digit int-to-str limit and it stops with a ValueError.
- The bar is the whole b-file in 60 s.
- The integer triangle W(n, k) = (−1)^k·S₂(n, k)·n!/k!, with
  W(n, k) = n·k·W(n−1, k) − n·W(n−1, k−1)/k, gives a(n) = Σ_k W(n, k)
  too, but it was about 105 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001569), CC BY-SA 4.0.
