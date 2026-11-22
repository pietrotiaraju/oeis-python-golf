# A002190

> Sum_{n>=0} a(n)*x^n/n!^2 = -log(BesselJ(0,2*sqrt(x))).
> — [OEIS A002190](https://oeis.org/A002190)

Offset 0: 0, 1, 1, 4, 33, 456, 9460, 274800, 10643745, 530052880, …

### Python 3 — 105 bytes

```python
import math
s=[0];n=0
while[print(abs(s[n]))]:n+=1;s+=~sum(j*math.comb(n,j)**2*s[j]for j in range(n))//n,
```

**How it works**

- **The series.** J₀(2√x) = f(x) = Σ (−1)ᵏ xᵏ/k!², and g = −log f has
  g = Σ a(n) xⁿ/n!². Differentiating, f·g′ = −f′.
- **Recurrence.** Comparing the coefficients of xⁿ⁻¹ in f·g′ = −f′ and
  multiplying by n!²/n gives, for n ≥ 1,
  Σ_(j=1..n) (−1)ⁿ⁻ʲ (j/n)·C(n, j)²·a(j) = (−1)ⁿ⁺¹,
  where the term j = n is a(n) itself. With s(j) = (−1)ʲ a(j) the signs
  collapse to
  s(n) = −1 − (1/n)·Σ_(j<n) j·C(n, j)²·s(j).
  (This is the formula of Ilya Gutkovskiy in the entry.)
- **Integers only.** j·C(n, j) = n·C(n−1, j−1), so the sum S is a
  multiple of n. Then `~S//n`, which Python reads as (−S−1)//n, equals
  −S/n − 1 exactly (for n ≥ 1, ⌊m − 1/n⌋ = m − 1 when m is an integer):
  one operator gives both the −1 and the division.
- **Loop.** s starts as [s(0)] = [0] (a(0) = 0, since f(0) = 1); each
  round prints |s(n)| = a(n), then appends s(n+1). The j = 0 term of the
  sum is 0, so `range(n)` may start at 0.
- **Why `abs` is right.** a(n) > 0 for n ≥ 1: J₀(2√x) is entire of order
  ½ in x with zeros c_k = j²₀,ₖ/4 > 0 (j₀,ₖ the zeros of J₀), so
  J₀(2√x) = Π(1 − x/c_k) and −log J₀(2√x) = Σ_(m≥1) (Σ_k c_k⁻ᵐ)·xᵐ/m has
  positive coefficients (a(n) also counts complete non-ambiguous trees,
  Aval et al.). So |s(n)| = a(n) for every n.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The
  first terms: s(1) = ~0 = −1, s(2) = ~(1·4·(−1))//2 = 1,
  s(3) = ~(1·9·(−1) + 2·9·1)//3 = −4.
- The whole b-file (101 terms, a(0) to a(100)) comes in a fraction of a
  second; the bar is the whole b-file, in 60 s.
- `from math import*` is one byte longer, the growing-list
  `for x in s:` loop two bytes longer, and the product form
  C(n, j)·C(n−1, j−1) (no division) ten bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 105 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002190), CC BY-SA 4.0.
