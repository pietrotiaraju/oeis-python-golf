# A001572

> Related to series-parallel networks.
> — [OEIS A001572](https://oeis.org/A001572)

Offset 0: 1, 1, 1, 1, 3, 5, 17, 41, 127, 365, 1119, 3413, 10685, 33561, …

### Python 3 — 138 bytes

```python
A=[s:=1,n:=1];Q=[-1]
while[print(s)]:Q=[s:=-sum(map(int.__mul__,A[1:],Q))]+Q;n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
```

**How it works**

- **The formula.** The entry gives 1 − Σ_(k≥1) a(k)·x^k =
  Π_n (1 − xⁿ)^b(n) with b = [A000669](https://oeis.org/A000669), and
  a(0) = 1. On [A000084](../../A000xxx/A000084/)'s page the
  series-parallel networks satisfy 1 + Σ A(n)·xⁿ = Π_n (1 − xⁿ)^(−b(n)),
  so the product is 1/(1 + A(x)) and the terms are Adamson's INVERTi
  transform of A000084: (1 + A)(1 − C) = 1 with C = Σ_(k≥1) a(k)x^k.
- **A000084 inside.** `A` is that page's program unchanged: a(0) = 1,
  A(1) = 1, and n·A(n) = Σ_d d·A(d)·Σ_(j≥1) A(n − jd) over
  d = 1, 1, 2, …, n − 1 (the d = 1 term counts twice because b(1) = 1
  but A(1)/2 = ½).
- **The INVERTi.** Put q(0) = −1 and q(k) = a(k) for k ≥ 1. Comparing
  coefficients of xⁿ (n ≥ 1) in (1 + A)(1 − C) = 1 gives
  **q(n) = −Σ_(k=1..n) A(k)·q(n − k)**. `Q` keeps q newest first, so
  this is the dot product of A(1), …, A(n) with `Q`; `map` stops at the
  shorter list, so it does not matter that `A` is one term ahead.
- **Printing.** The terms printed are q(n) itself, with no sign trick
  and no assumption that a(n) > 0; only a(0) = 1 is printed separately,
  by starting `s` at 1 (`A=[s:=1,n:=1]` sets s, A(0) and n at once).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 29 terms (up to a(28)); the bar is the whole b-file
  in 60 s, which takes a few milliseconds.
- The two series can also share one interleaved list with two Euler
  passes (weights d·A(d), divisors n and −2n), but the passes need
  different ranges of d and it came out longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 138 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001572), CC BY-SA 4.0.
