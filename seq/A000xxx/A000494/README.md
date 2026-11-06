# A000494

> Nearest integer to sin(n).
> — [OEIS A000494](https://oeis.org/A000494)

Offset 0: 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, …

### Python 3 — 215 bytes

```python
n=0;S=1
while 1:
 S*=2;K=S.bit_length();E=20*-~K
 p=sum((-1)**k*S*a//((2*k+1)*b**(2*k+1))for a,b in((16,5),(-4,239))for k in range(K))
 while p>E and(q:=6*n*S//(p+E))==6*n*S//(p-E):print((0<q%6<5)*(1-q//6%2*2));n+=1
```

**How it works**

- All angles are in **radians**. The program determines the sector
  containing n using certified bounds on π, then reads off the nearest integer to sin(n).
  It never evaluates a floating-point sine or cosine.
- [Machin's identity](https://mathworld.wolfram.com/Machin-LikeFormulas.html)
  is π=16atan(1/5)−4atan(1/239). With
  atan(1/b)=Σₖ≥₀ (−1)ᵏ/((2k+1)b^(2k+1)), take K terms
  at the integer scale S. The comprehension uses the pairs
  `(16,5)` and `(-4,239)` and rounds every signed scaled
  contribution down before adding the two series.
- Those divisions contribute less than 2K total error. Since
  K=S.bit_length() and S≥2, the two scaled alternating-series
  tails together are less than 1. The generous error allowance
  E=20(K+1) therefore proves **p−E<Sπ<p+E**.
- Once `p>E`, both denominators are positive. The two quotients
  ⌊6nS/(p+E)⌋ and ⌊6nS/(p−E)⌋ bracket
  q=⌊6n/π⌋. Print only if they agree, using the first
  quotient stored by the walrus in q.
- If they disagree, double S and recompute tighter bounds.
  Otherwise advance n and reuse the current bounds for as many
  consecutive inputs as they certify. For n>0, 6n/π is
  not an integer, so increasing precision eventually resolves it.
- Sine rounds to 1 above 1/2, −1 below −1/2, and 0
  between. These thresholds are multiples of π/6, so
  q=⌊6n/π⌋ identifies one of twelve sectors per period.
  `0<q%6<5` selects the four nonzero sectors in each
  half-period, while `1-q//6%2*2` supplies their alternating
  sign. The result is 1 for residues 1 through 4, −1 for
  residues 7 through 10, and zero for the others.
- The n=0 quotient is exactly zero and prints 0. No positive
  integer n lies at a tie sin(n)=±1/2, since such an n
  would be a rational multiple of π.

The sector-to-output mapping is:

| q mod 12 | 0 | 1–4 | 5–6 | 7–10 | 11 |
|---|---|---|---|---|---|
| nearest integer to sin(n) | 0 | 1 | 0 | −1 | 0 |

**Notes**

- Exact integer arithmetic and a rigorous error interval at every
  precision. Irrationality of π rules out the positive-index
  sector boundaries; the separate handling of n=0 is described above.
- The output uses only −1, 0 and 1, so its conversion never
  reaches Python's 4300-digit integer limit. Time and temporary
  integer sizes grow when a closer approach to a sector boundary
  requires a more accurate π interval.
- [A000493](../A000493/) uses the same π bounds with
  a different sector scale or rounding rule. The lookup is part
  of the mathematical rounding test, not a table of sequence terms.
- The b-file has 1001 terms (indices 0 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 239 | first entry |
| 2026-11-06 | Python 3 | 215 | share the Machin summand and compute the sector sign arithmetically |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000494), CC BY-SA 4.0.
