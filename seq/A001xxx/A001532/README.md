# A001532

> Number of NP-equivalence classes of self-dual threshold functions of n or fewer variables; number of majority (i.e., decisive and weighted) games with n players.
> — [OEIS A001532](https://oeis.org/A001532)

Offset 1: 1, 1, 2, 3, 7, 21, 135, 2470, 175428, 52980624

### Python 3 — 221 bytes

```python
import math
n=1
while 1:
 V=[[0]];exec('V=(v+[a+c for a in v]for v in V for c in range(v[len(v)//2],math.isqrt((n+1)**-~n)+2**n>>n));'*n)
 print(len({(*(0<s for s in u),)for v in V if all(u:=[2*a-v[-1]for a in v])}));n+=1
```

**What is counted**

Threshold functions f(x) = [w·x > t] on {0,1}ⁿ that are self-dual,
f(¬x) = ¬f(x), up to permuting and negating inputs (NP-equivalence).
Permuting and negating inputs commutes with x ↦ ¬x, so it keeps a function
self-dual.

- *One sorted function per NP class.* Integer weights with
  |wᵢ| ≤ B = ⌊(n+1)^((n+1)/2)/2ⁿ⌋ suffice (Muroga, Toda and Takasu, 1961), so
  every NP class of threshold functions holds a function [w·x > t] with
  0 ≤ w₁ ≤ … ≤ wₙ ≤ B, and two different such functions are never
  NP-equivalent: the [A000617](../A000617/) page proves both. If the class is
  self-dual, so is this function.
- *A self-dual threshold function has threshold W/2.* Let f = [w·x > t] be
  self-dual with w ≥ 0 and W = w₁ + … + wₙ. If f(x) = 1 and w·x < W/2, then
  w·¬x = W − w·x > w·x > t, so f(¬x) = 1 too, which self-duality forbids.
  If f(x) = 0 and w·x ≥ W/2, then w·¬x ≤ w·x ≤ t and f(¬x) = 0, forbidden
  too. So f(x) = [2w·x > W], and no x has 2w·x = W (else x and ¬x have
  the same sum and f(x) = f(¬x)).
  Conversely, for any w with no sum w·x equal to W/2, [2w·x > W] is a
  self-dual threshold function.
- So a(n) is the number of distinct functions [2w·x > W] over the sorted
  weight vectors 0 ≤ w₁ ≤ … ≤ wₙ ≤ B with no sum equal to W/2. For a
  majority game the players are the inputs and the winning coalitions are
  the x with f(x) = 1.

**How it works**

- `exec` builds the sorted weight vectors as in A000617: appending a weight
  `c` turns the list `v` of all sums w·x into `v+[a+c for a in v]`,
  `v[len(v)//2]` is the last weight appended, and
  `math.isqrt((n+1)**-~n)+2**n>>n` is B + 1. `V` is a chain of generators,
  so the weight vectors are made one at a time and memory stays small.
- `v[-1]` is W, `u` lists 2w·x − W for every x, `all(u)` drops the vectors
  with a tie, and `(*(0<s for s in u),)` is the truth table of [2w·x > W].
  The set counts the distinct tables.

**Notes**

- Correctness for every n rests on the Muroga–Toda–Takasu weight bound,
  computed exactly with `isqrt`. The program is a sibling of
  [A001529](../A001529/), whose NPN classes are (A000617(n) + a(n))/2.
- n = 6 takes about a second here (C(20, 6) = 38 760 weight vectors, one
  table each); n = 7 would need C(39, 7) ≈ 15 million weight vectors on 128
  points. The bar is the 6 terms n = 1 to 6 in 60 s; the b-file has 10.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 221 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001532), CC BY-SA 4.0.
