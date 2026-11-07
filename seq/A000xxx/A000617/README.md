# A000617

> Number of NP-equivalence classes of threshold functions of n or fewer variables.
> — [OEIS A000617](https://oeis.org/A000617)

Offset 0: 2, 3, 5, 10, 27, 119, 1113, 29375, 2730166, …

### Python 3 — 203 bytes

```python
import math
n=0
while 1:
 V=[[0]];exec('V=[v+[a+c for a in v]for v in V for c in range(v[len(v)//2],math.isqrt((n+1)**-~n)+2**n>>n)];'*n)
 print(len({(*map(t.__lt__,v),)for v in V for t in v+[-1]}));n+=1
```

**What is counted**

Threshold functions f(x) = [w·x > t] on {0,1}ⁿ up to permuting and negating
inputs (NP-equivalence). The program counts one function per class:

- *Every class has one with sorted weights.* Integer weights with
  |wᵢ| ≤ B = ⌊(n+1)^((n+1)/2)/2ⁿ⌋ suffice (Muroga, Toda and Takasu, 1961).
  Negating the inputs with negative weight and then permuting the inputs
  gives a function of the class with weights 0 ≤ w₁ ≤ … ≤ wₙ ≤ B.
- *Two different such functions are never equivalent.* First, if g and
  g' are positive (monotone) and g' is g with inputs permuted and some
  negated, the negated inputs are irrelevant (see [A000615](../A000615/)), so
  g' is a permutation of g. Second, say input i is weaker than input j in g
  when g(x) ≤ g(x with xᵢ and xⱼ swapped) whenever xᵢ = 1, xⱼ = 0. For
  g = [w·x > t] this holds whenever wᵢ ≤ wⱼ, so any two inputs compare, and
  with sorted weights the inputs 1, …, n come in non-decreasing strength. If
  g and h = g∘π both have sorted weights, the strengths of π(1), …, π(n) in g
  are non-decreasing too, so π only moves inputs among others of equal
  strength. Two inputs of equal strength can be swapped without changing g,
  so h = g.
- So a(n) is the number of distinct functions [w·x > t] with
  0 ≤ w₁ ≤ … ≤ wₙ ≤ B.

**How it works**

- `exec` runs the doubling step n times: appending a weight c turns the list
  `v` of sums w·x into `v+[a+c for a in v]`. Since v[0] = 0, the entry
  `v[len(v)//2]` is the last weight appended, so `c` runs from it up to B
  and the weights come out sorted. `math.isqrt((n+1)**-~n)+2**n>>n` is B + 1.
- For each list, the thresholds are the sums themselves and −1, which give
  every cut including both constants; `(*map(t.__lt__,v),)` is the truth
  table, and the size of the set is a(n).

**Notes**

- Correctness for every n rests on the Muroga–Toda–Takasu weight bound; the
  bound is computed exactly with `isqrt`.
- n = 6 enumerates C(20, 6) = 38 760 sorted weight vectors on 64 points
  (about 22 s here); n = 7 would need C(39, 7) ≈ 15 million on 128 points.
  The bar is the 7 terms n = 0 to 6 in 120 s; the b-file has 10.
- [A000619](../A000619/) prints the differences of this sequence.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 203 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000617), CC BY-SA 4.0.
