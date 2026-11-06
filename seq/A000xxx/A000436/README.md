# A000436

> Generalized Euler numbers c(3,n).
> — [OEIS A000436](https://oeis.org/A000436)

Offset 0: 1, 8, 352, 38528, 7869952, 2583554048, 1243925143552, 825787662368768, 722906928498737152, 806875574817679474688, …

### Python 3 — 120 bytes

```python
import math
a=[]
while 1:
 n=len(a);a+=[(-1)**n-sum(math.comb(2*n,2*k)*(-9)**k*a[-k]for k in range(1,n+1))];print(a[-1])
```

**How it works**

- Write F(x)=cos(x)/cos(3x) as
  Σₙ≥₀ a(n)x^(2n)/(2n)!.
  Only even derivatives occur, since F is even.
  Multiplying by cos(3x) gives cos(x).
- The 2k-th derivative of cos(3x) at zero is
  (−1)ᵏ·3^(2k)=(-9)ᵏ; the 2n-th derivative
  of cos(x) is (−1)ⁿ. The product rule therefore gives

  a(n) = (−1)ⁿ − Σₖ₌₁ⁿ C(2n,2k)·(-9)ᵏ·a(n−k).

- `n=len(a)` is the next sequence index, and before appending,
  `a[-k]` selects a(n−k). The k=0 term of the product is the unknown
  a(n), because cos(0)=1; moving the other terms to the right gives
  the subtraction in the code.
- At n=0 the sum is empty, so the initial value is 1. At n=1,
  −1−(−9)·1=8, the next
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
- The b-file has 101 terms (indices 0 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 123 | first entry |
| 2026-11-06 | Python 3 | 122 | use a shorter math import |
| 2026-11-06 | Python 3 | 120 | remove addition of zero in the binomial argument |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000436), CC BY-SA 4.0.
