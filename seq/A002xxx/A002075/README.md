# A002075

> Number of equivalence classes with primitive period n of base 3 necklaces, where necklaces are equivalent under rotation and permutation of symbols.
> — [OEIS A002075](https://oeis.org/A002075)

Offset 1: 1, 1, 2, 4, 8, 22, 52, 140, 366, 992, 2684, 7404, …

### Python 3 — 139 bytes

```python
import math
L=[0];n=0
while 1:n+=1;L+=sum(3**(g:=math.gcd(k,n))*(6-(d:=n//g)*-d%6)+d%2*3-n*L[k]*(g==k)for k in range(n))//n,;print(L[n]//6)
```

**How it works**

- **Primitive period.** Rotating a word or permuting its symbols keeps
  its least rotation period, so all the words in a class of
  [A002076](../A002076/) (length-n words under rotation and the six
  permutations of the symbols) share one least period d, a divisor of n.
  Cutting the words to one period is a bijection between those classes
  and the classes of length-d words of least period d. So
  A002076(n) = Σ_{d | n} a(d), the relation stated in the OEIS entry, and
  a(n) = A002076(n) − Σ_{d | n, d < n} a(d) (Möbius inversion done by
  subtraction).
- **A002076(n)** comes from Burnside's lemma over C_n × S₃, as on
  [A002076](../A002076/): 6n·A002076(n) = Σ_{k<n} (3^g·c(n/g) + 3·[n/g odd])
  with g = gcd(k, n), where c(d) = 6 − (−d²) mod 6 is the number of
  σ ∈ S₃ with σᵈ = 1.
- **Subtraction inside the same sum.** `L[k]` holds 6·a(k) (and a dummy
  `L[0]`). For k ≥ 1, gcd(k, n) = k exactly when k divides n, and k = 0
  has gcd n ≠ 0, so `-n*L[k]*(g==k)` subtracts 6n·a(k) for each proper
  divisor k. The sum is then 6n·a(n); `//n` stores 6·a(n) and the print
  divides by 6.

**Notes**

- Exact integer arithmetic; every division is exact, and the program is
  right for every n.
- The b-file has the 28 terms of the entry (n = 1 to 28), all printed in
  well under a second; the bar is all 28 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 139 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002075), CC BY-SA 4.0.
