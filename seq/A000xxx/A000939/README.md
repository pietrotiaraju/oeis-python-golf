# A000939

> Number of inequivalent n-gons.
> — [OEIS A000939](https://oeis.org/A000939)

Offset 1: 1, 1, 1, 2, 4, 14, 54, 332, 2246, 18264, 164950, 1664354, 18423144, 222406776, 2905943328, 40865005494, 615376173184, 9880209206458, 168483518571798, 3041127561315224, …

### Python 3 — 155 bytes

```python
from math import*
n=1
while[print((prod(range(~n%2*2,n,2))+2*sum(factorial(g)*(n//g)**g for k in range(n*n)if(g:=gcd(k,n))==gcd(k//n,n))//n//n+3)//4)]:n+=1
```

**How it works**

- Burnside over the rotations (Golomb–Welch; Howroyd's PARI formula):
  for n ≥ 3, a(n) = (T + E)/2, where T = (1/n²) Σ_{d|n} φ(n/d)² d! (n/d)ᵈ
  counts directed Hamiltonian cycles up to rotation
  ([A002619](https://oeis.org/A002619)) and E = 2^{n/2−2}(n/2−1)! for even
  n, 0 for odd n, counts the classes that equal their own reverse.
- φ(n/g)² as a pair count: there are φ(n/g) residues j mod n with
  gcd(j, n) = g, so the pairs (i, j) with gcd(i, n) = gcd(j, n) = g number
  φ(n/g)². One loop k < n² gives the pair (k mod n, k//n), and
  gcd(k, n) = gcd(k mod n, n), so the test is
  `(g:=gcd(k,n))==gcd(k//n,n)` and each pair adds g!(n/g)ᵍ.
- 2E = (n−2)!! = 2·4·…·(n−2) for even n is `prod(range(~n%2*2,n,2))`; for
  odd n the range starts at 0 and the product is 0. So 4a = 2E + 2T.
- For n = 1 and 2 the formula gives 2/4 and 3/4 instead of 1; the ceiling
  `(…+3)//4` fixes both and is exact for n ≥ 3.

**Notes**

- Exact integer arithmetic; correctness rests on Burnside's lemma and
  the cycle counts in the formula.
- The b-file (450 terms, though its header says 1..1000) takes about
  21 s; about 650 terms in 60 s. Terms pass the 4300-digit `str` limit
  only near n = 1450, far beyond that.
- The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 155 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000939), CC BY-SA 4.0.
