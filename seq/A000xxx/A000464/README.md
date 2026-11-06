# A000464

> Expansion of e.g.f. sin(x)/cos(2*x).
> — [OEIS A000464](https://oeis.org/A000464)

Offset 0: 1, 11, 361, 24611, 2873041, 512343611, 129570724921, 44110959165011, 19450718635716001, 10784052561125704811, …

### Python 3 — 122 bytes

```python
import math
a=[]
while 1:
 n=len(a);a+=[(-1)**n-sum(math.comb(2*n+1,2*k)*(-4)**k*a[-k]for k in range(1,n+1))];print(a[-1])
```

**How it works**

- Write F(x)=sin(x)/cos(2x) as
  Σₙ≥₀ a(n)x^(2n+1)/(2n+1)!.
  Only odd derivatives occur, since F is odd; a(0) is F′(0), not F(0).
  Multiplying by cos(2x) gives sin(x).
- The 2k-th derivative of cos(2x) at zero is
  (−1)ᵏ·2^(2k)=(-4)ᵏ; the 2n+1-th derivative
  of sin(x) is (−1)ⁿ. The product rule therefore gives

  a(n) = (−1)ⁿ − Σₖ₌₁ⁿ C(2n+1,2k)·(-4)ᵏ·a(n−k).

- `n=len(a)` is the next sequence index, and before appending,
  `a[-k]` selects a(n−k). The k=0 term of the product is the unknown
  a(n), because cos(0)=1; moving the other terms to the right gives
  the subtraction in the code.
- At n=0 the sum is empty, so the initial value is 1. At n=1,
  −1−C(3,2)·(−4)·1=11, the next
  term. Appending before `print(a[-1])` keeps these indices aligned.

**Notes**

- The sine and cosine are used only to derive a formal power-series
  identity. The program evaluates no trigonometric functions and
  uses exact integers, with no factorial divisions or rounding.
- It stores all preceding coefficients: n+1 entries after term n,
  and n binomial-convolution summands for that term. Only derivatives
  of the relevant parity are kept.
- Compare [A000490](../A000490/), which uses a constant numerator
  instead. Python 3.11+ eventually stops when the output exceeds its
  default 4300-digit conversion limit; that is an interpreter limit.
- The b-file has 216 terms (indices 0 through 215). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 123 | first entry |
| 2026-11-06 | Python 3 | 122 | use a shorter math import |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000464), CC BY-SA 4.0.
