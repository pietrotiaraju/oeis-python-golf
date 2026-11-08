# A001134

> Primes p such that the multiplicative order of 2 modulo p is (p-1)/4.
> — [OEIS A001134](https://oeis.org/A001134)

Offset 1: 113, 281, 353, 577, 593, 617, 1033, 1049, 1097, 1153, 1193, 1201, 1481, 1601, 1889, 2129, 2273, 2393, 2473, 3049, …

One of four siblings: ord_p(2) = (p − 1)/k for k = 3 ([A001133](../A001133/)), 4 (this page), 5 ([A001135](../A001135/)), 6 ([A001136](../A001136/)); the programs
differ in one constant, and [A001133](../A001133/) has the longer notes.

### Python 3 — 71 bytes

```python
P=k=1
while[5==sum(2**e%k<2for e in range(-P%k*k))==print(k)]:P*=k;k+=1
```

**How it works**

- **Count the exponents.** For a prime p, 2ᵉ ≡ 1 (mod p) exactly when
  ord_p(2) divides e, and ord_p(2) divides p − 1 (Fermat). So among
  e = 0, 1, …, p − 1 there are 1 + (p − 1)/ord_p(2) hits, and the order is
  (p − 1)/4 exactly when the count is 5. No factoring, and 4 | p − 1 comes
  for free.
- **Only primes get a range.** `P` is (k − 1)!, so by Wilson's theorem
  `-P%k` is 1 for a prime, 0 for k = 1 and every composite k > 4, and 2 for
  k = 4: `range(-P%k*k)` is `range(k)` for a prime and empty (sum 0) for
  k = 1 and the composites above 4.
- `2**e%k<2` is the test 2ᵉ ≡ 1: for an odd prime the residue is never 0.
  The only composite with a range is k = 4 (8 exponents), and
  2ᵉ mod 4 = 1, 2, 0, 0, … gives 7 hits there, not 5; p = 2 gives 2.
- The chained comparison `5==sum(…)==print(k)` prints only when the count
  is 5, and the list around it keeps the loop going.

**Notes**

- Exact for every n; it rests on Wilson's and Fermat's theorems only.
- Each prime p costs p powers 2ᵉ with up to p bits, about p² work per prime:
  64 terms in 50 s on the PC it was written on (every prime up to about
  10 500). The b-file has 1000 terms; the bar is 56 terms in 120 s.
- Faster but longer, as on A001133: `(1<<e)%k` (+2 bytes) or `pow(2,e,k)`
  (+4 bytes) print about 1.7 and 2.2 times as many terms in the same time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001134), CC BY-SA 4.0.
