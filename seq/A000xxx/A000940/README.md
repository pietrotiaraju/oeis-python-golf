# A000940

> Number of n-gons with n vertices.
> — [OEIS A000940](https://oeis.org/A000940)

Offset 3: 1, 2, 4, 12, 39, 202, 1219, 9468, 83435, 836017, 9223092, 111255228, 1453132944, 20433309147, 307690667072, 4940118795869, 84241805734539, 1520564059349452, 28963120073957838, 580578894859915650, …

### Python 3 — 162 bytes

```python
from math import*
n=3
while[print((prod(range(2,n,2))*(n+6,4)[n%2]+4*sum(factorial(g)*(n//g)**g for k in range(n*n)if(g:=gcd(k,n))==gcd(k//n,n))//n//n)//16)]:n+=1
```

**How it works**

- Burnside over the dihedral group (Golomb–Welch; Howroyd's PARI formula):
  for n ≥ 3, 4n²·a(n) = 2^{k−2} k! n X + Σ_{d|n} φ(n/d)² d! (n/d)ᵈ with
  k = ⌊n/2⌋, X = 4n for odd n and n+6 for even n.
- With Q = 2·4·…·(largest even number below n) = `prod(range(2,n,2))`:
  for odd n, 2ᵏk! = Q; for even n, 2ᵏk!/n = 2^{k−1}(k−1)! = Q. Both cases
  become 16a = Q·Y + 4T with Y = 4 or n+6 (`(n+6,4)[n%2]`) and
  T = Σ/n², and no negative power of 2 is left (n = 3 has k−2 = −1).
- The divisor sum is the one of [A000939](../A000939/): one loop k < n²
  over pairs (k mod n, k//n) with equal gcd with n, each adding g!(n/g)ᵍ.

**Notes**

- Exact integer arithmetic; correctness rests on Burnside's lemma and
  the cycle counts in the formula.
- The b-file (498 terms, n = 3..500) takes about 28 s; about 640 terms in
  60 s.
- The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 162 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000940), CC BY-SA 4.0.
