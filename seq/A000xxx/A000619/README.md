# A000619

> NP-equivalence classes of threshold functions of exactly n variables.
> — [OEIS A000619](https://oeis.org/A000619)

Offset 0: 2, 1, 2, 5, 17, 92, 994, 28262, 2700791, …

### Python 3 — 213 bytes

```python
import math
n=o=0
while 1:
 V=[[0]];exec('V=[v+[a+c for a in v]for v in V for c in range(v[len(v)//2],math.isqrt((n+1)**-~n)+2**n>>n)];'*n)
 print(-o+(o:=len({(*map(t.__lt__,v),)for v in V for t in v+[-1]})));n+=1
```

**How it works**

- An NP-class of threshold functions of n or fewer variables has a number k
  of essential inputs, and moving those to the front makes it a class of
  nondegenerate threshold functions of k variables. So
  [A000617](../A000617/)(n) = a(0) + … + a(n), and
  a(n) = A000617(n) − A000617(n−1).
- The program is the A000617 program with the running difference
  `-o+(o:=…)`; `o` starts at 0, so the first line is A000617(0) = 2.
- A000617 counts the distinct functions [w·x > t] with sorted weights
  0 ≤ w₁ ≤ … ≤ wₙ ≤ ⌊(n+1)^((n+1)/2)/2ⁿ⌋; see its page for why each class
  appears exactly once.

**Notes**

- Correctness for every n rests on the Muroga–Toda–Takasu weight bound
  (integer weights of size at most (n+1)^((n+1)/2)/2ⁿ suffice) and on the
  argument on the A000617 page.
- n = 6 takes about 22 s here and n = 7 is out of reach (about 15 million
  sorted weight vectors on 128 points). The bar is the 7 terms n = 0 to 6 in
  120 s; the b-file has 10.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 213 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000619), CC BY-SA 4.0.
