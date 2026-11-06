# A000411

> Generalized tangent numbers d(6,n).
> — [OEIS A000411](https://oeis.org/A000411)

Offset 1: 6, 522, 152166, 93241002, 97949265606, 157201459863882, 357802951084619046, 1096291279711115037162, 4350684698032741048452486, 21709332137467778453687752842, …

### Python 3 — 128 bytes

```python
from math import*
a=[]
while 1:
 n=len(a);a+=[6*(-9)**n-2*sum(comb(2*n+1,2*k)*(-16)**k*a[-k]for k in range(1,n+1))];print(a[-1])
```

**How it works**

- Write F(x)=2sin(3x)/(2cos(4x)−1)=
  Σₘ≥₀ a(m+1)x^(2m+1)/(2m+1)!. Only odd derivatives occur;
  the sequence starts at a(1)=F′(0)=6.
- Multiplying by the denominator gives (2cos(4x)−1)F(x)=2sin(3x).
  Its constant coefficient is 1, while its 2k-th derivative is
  2·(−16)ᵏ for k≥1. The numerator's (2m+1)-th derivative is
  6·(−9)ᵐ. The product rule therefore yields

  a(m+1)=6·(−9)ᵐ−2Σₖ₌₁ᵐ C(2m+1,2k)·(−16)ᵏ·a(m−k+1).

- In the code `n=len(a)` is m, the number of derivatives already
  stored. Before the append, `a[-k]` is a(m−k+1); afterwards
  `a[-1]` is the new a(m+1). The list index is one below the OEIS index.
- The empty sum gives 6 on the first pass. On the next,
  6·(−9)−2·C(3,2)·(−16)·6=522, matching a(2).

**Notes**

- Exact integer arithmetic from a formal generating-function identity.
  The program never evaluates sine, cosine or a quotient numerically.
  The denominator's constant term 1 is why no division is needed.
- As in [A000464](../A000464/), only derivatives of one parity are
  stored. Computing term m+1 uses m preceding values and m binomial
  summands; the list grows by one per term.
- Generalized tangent numbers grow rapidly. Python 3.11+ eventually
  stops when a printed integer passes its default 4300-digit limit;
  this is an interpreter limit rather than a failure of the recurrence.
- The b-file has 184 terms (indices 1 through 184). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 128 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000411), CC BY-SA 4.0.
