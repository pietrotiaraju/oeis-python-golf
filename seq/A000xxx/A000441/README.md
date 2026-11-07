# A000441

> a(n) = Sum_{k=1..n-1} k*sigma(k)*sigma(n-k).
> — [OEIS A000441](https://oeis.org/A000441)

Offset 1: 0, 1, 9, 34, 95, 210, 406, 740, 1161, 1920, …

### Python 3 — 77 bytes

```python
r=[1]
for n in r:r+=n+1,;print(n*sum(5*k**3+k-6*n*k for k in r if n%k<1)//24)
```

**How it works**

- Write σ_j(n) = Σ_{d|n} d^j. Ramanujan's identity q·dE₂/dq = (E₂² − E₄)/12
  for E₂ = 1 − 24Σσ(n)qⁿ and E₄ = 1 + 240Σσ₃(n)qⁿ gives, on comparing the
  qⁿ coefficients, the classical convolution
  Σ_{k=1}^{n−1} σ(k)σ(n−k) = (5σ₃(n) + (1 − 6n)σ(n))/12.
- Swapping k and n − k shows Σ k·σ(k)σ(n−k) = Σ (n−k)·σ(k)σ(n−k), so the
  weighted sum is n/2 times the plain one:
  24a(n) = n·(5σ₃(n) + (1 − 6n)σ(n)) (the formula on the OEIS page).
- Both divisor sums run over the same divisors, so the program sums
  5k³ + k − 6nk over the k dividing n and multiplies by n. The right side
  is 24 times an integer, so `//24` is exact.
- The list `r` is the loop and the divisor range at once: `for n in r`
  sees the items appended while it runs, and `r+=n+1,` makes r = [1, …,
  n+1] at the time of the sum. The extra n+1 never divides n, so
  `for k in r if n%k<1` is exactly the divisors of n (the
  [A000203](../A000203/) trick).
- At n = 1 the only divisor gives 5 + 1 − 6 = 0, the empty sum a(1) = 0.

**Notes**

- `n=1` / `while[print(n*sum(…for k in range(1,n+1)if n%k<1)//24)]:n+=1`
  is 78 bytes. The summand as `k*(5*k*k+1-6*n)` ties at 77 (no space is
  needed before the `for`). Negative divisors do not work here: `n%k` is
  never positive for k < 0.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints in about 0.3 s here. The b-file has 1000 terms
  (up to a(1000)); the bar is the whole b-file in 60 s.
- a(n) grows like n⁴, so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 82 | first entry |
| 2026-11-06 | Python 3 | 79 | remove the identity exponent on n |
| 2026-11-07 | Python 3 | 77 | growing list r as loop and divisor range |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000441), CC BY-SA 4.0.
