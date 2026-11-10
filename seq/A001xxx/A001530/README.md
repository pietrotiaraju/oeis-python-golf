# A001530

> NPN-equivalence classes of threshold functions of exactly n variables.
> — [OEIS A001530](https://oeis.org/A001530)

Offset 0: 1, 1, 1, 3, 9, 48, 504, 14188, 1351563, 495252138

### Python 3 — 233 bytes

```python
import math
n=o=0
while 1:
 V=[[0]];exec('V=(v+[a+c for a in v]for v in V for c in range(v[len(v)//2],math.isqrt((n+1)**-~n)+2**n>>n));'*n)
 print(-o+(o:=len({min((*map(u.__lt__,v),)for u in(t,v[-1]+~t))for v in V for t in v})));n+=1
```

**What is counted**

- A threshold function of n variables that depends on exactly k of them is,
  with those k moved to the front, a threshold function of exactly k
  variables (fix the other inputs to 0), and two such functions are
  NPN-equivalent exactly when their k-variable versions are. So the NPN
  classes of threshold functions of n or fewer variables,
  [A001529](../A001529/)(n), number a(0) + … + a(n), and
  a(n) = A001529(n) − A001529(n−1) with a(0) = A001529(0) = 1 (the two
  constants form one class). This matches all ten OEIS terms.

**How it works**

- `len({…})` is A001529(n), computed as on that page: the sorted
  integer-weight functions [w·x > t] with 0 ≤ w₁ ≤ … ≤ wₙ ≤ B, one per NP
  class by the Muroga–Toda–Takasu bound B = ⌊(n+1)^((n+1)/2)/2ⁿ⌋ (proof on
  the [A000617](../A000617/) page), paired with [w·x > W − 1 − t], the
  sorted function of the class of the negation.
- `-o+(o:=…)` with `o` starting at 0 prints the running difference.

**Notes**

- Correctness for every n rests on the Muroga–Toda–Takasu weight bound,
  computed exactly with `isqrt`.
- n = 6 takes about 27 s here; n = 7 would need about 15 million weight
  vectors on 128 points. The bar is the 7 terms n = 0 to 6 in 60 s; the
  b-file has 10.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 233 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001530), CC BY-SA 4.0.
