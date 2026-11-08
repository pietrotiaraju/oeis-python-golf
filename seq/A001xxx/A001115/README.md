# A001115

> Maximal number of pairwise relatively prime polynomials of degree n over GF(2).
> — [OEIS A001115](https://oeis.org/A001115)

Offset 0: 1, 2, 3, 4, 6, 9, 14, 23, 38, 64, 113, 200, …

### Python 3 — 103 bytes

```python
P=[1];n=0
while[print(P[n]+sum(P[1:n//2+1]))]:n+=1;P+=(2**n-sum(d*P[d]for d in range(1,n)if n%d<1))//n,
```

**How it works**

- a(n) = P(n) + Σ_{i=1}^{⌊n/2⌋} P(i), where P(n) = A001037(n) is the number
  of irreducible polynomials of degree n over GF(2) (P(0) = 1), the formula
  in the OEIS entry. Why: the irreducible factors of pairwise coprime
  polynomials are disjoint, and a polynomial of degree n that is not
  irreducible has a factor of degree ≤ n/2, so there are at most
  Σ_{i≤n/2} P(i) of those besides the P(n) irreducible ones. The OEIS
  comment (after Bossen & Yau 1968) gives a set that reaches the bound for
  n ≥ 4 (p·q with q irreducible of degree n − d, and p² for d = n/2); the
  terms n ≤ 3 are the examples in the entry.
- P comes from Gauss's count Σ_{d|n} d·P(d) = 2^n (every element of
  GF(2^n) has a minimal polynomial of degree d | n): P(n) = (2^n −
  Σ_{d|n, d<n} d·P(d))/n, appended to the list `P` as n grows. P[0] = 1 only
  serves a(0) = 1; the divisor sum starts at d = 1.

**Notes**

- The b-file has 41 terms (n = 0 to 40); they print instantly, and the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001115), CC BY-SA 4.0.
