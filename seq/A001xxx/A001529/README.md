# A001529

> Number of NPN-equivalence classes of threshold functions of n or fewer variables.
> — [OEIS A001529](https://oeis.org/A001529)

Offset 0: 1, 2, 3, 6, 15, 63, 567, 14755, 1366318, 496618456

### Python 3 — 223 bytes

```python
import math
n=0
while 1:
 V=[[0]];exec('V=(v+[a+c for a in v]for v in V for c in range(v[len(v)//2],math.isqrt((n+1)**-~n)+2**n>>n));'*n)
 print(len({min((*map(u.__lt__,v),)for u in(t,v[-1]+~t))for v in V for t in v}));n+=1
```

**What is counted**

Threshold functions f(x) = [w·x > t] on {0,1}ⁿ up to permuting and negating
inputs and negating the output (NPN-equivalence). The program starts from the
NP classes as [A000617](../A000617/) counts them and joins each class with
the class of its negation.

- *One sorted function per NP class.* Integer weights with
  |wᵢ| ≤ B = ⌊(n+1)^((n+1)/2)/2ⁿ⌋ suffice (Muroga, Toda and Takasu, 1961), so
  every NP class holds a function [w·x > t] with 0 ≤ w₁ ≤ … ≤ wₙ ≤ B, and two
  different such functions are never NP-equivalent: the A000617 page proves
  both. Call them the sorted functions.
- *Negating the output.* For f = [w·x > t] with integer weights and
  W = w₁ + … + wₙ, negating the output and all inputs gives
  ¬f(¬x) = [w·(1−x) ≤ t] = [w·x > W − 1 − t]: a sorted function again, with
  the same weights. Negating all inputs is an NP map, so this is the sorted
  function of the NP class of ¬f. NPN classes are therefore the pairs
  {f, ¬f(¬x)} of sorted functions (a single one when they coincide), and the
  smaller truth table of the pair names its NPN class.

**How it works**

- `exec` builds the sorted weight vectors as in A000617: appending a weight
  `c` turns the list `v` of all sums w·x into `v+[a+c for a in v]`,
  `v[len(v)//2]` is the last weight appended, and
  `math.isqrt((n+1)**-~n)+2**n>>n` is B + 1. Here `V` is a chain of
  generators instead of lists, so the weight vectors are made one at a time
  and memory stays small.
- For each threshold `t` in `v`, `u` runs over `t` and `v[-1]+~t` =
  W − 1 − t, and `(*map(u.__lt__,v),)` is the truth table [w·x > u]. The
  minimum of the two names the pair; the set counts the pairs.
- `t` = −1 (the constant 1) is not needed: its pair is that of `t` = W, the
  constant 0.

**Notes**

- Correctness for every n rests on the Muroga–Toda–Takasu weight bound,
  computed exactly with `isqrt`. It agrees with the OEIS comment
  a(n) = (A000617(n) + A001532(n))/2.
- n = 6 builds C(20, 6) = 38 760 weight vectors with 64 sums each, about
  27 s here; n = 7 would need C(39, 7) ≈ 15 million on 128 points. The bar is
  the 7 terms n = 0 to 6 in 60 s; the b-file has 10.
- [A001530](../A001530/) prints the differences of this sequence, and
  [A001532](../A001532/) counts the self-dual classes the same way.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 223 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001529), CC BY-SA 4.0.
