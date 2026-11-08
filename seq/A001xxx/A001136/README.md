# A001136

> Primes p such that the multiplicative order of 2 modulo p is (p-1)/6.
> — [OEIS A001136](https://oeis.org/A001136)

Offset 1: 31, 223, 433, 439, 457, 727, 919, 1327, 1399, 1423, 1471, 1831, 1999, 2017, 2287, 2383, 2671, 2767, 2791, 2953, …

One of four siblings: ord_p(2) = (p − 1)/k for k = 3 ([A001133](../A001133/)), 4 ([A001134](../A001134/)), 5 ([A001135](../A001135/)), 6 (this page); the programs
differ in one constant, and [A001133](../A001133/) has the longer notes.

### Python 3 — 72 bytes

```python
P=k=1
while[7==sum(2**e%k==1for e in range(-P%k*k))==print(k)]:P*=k;k+=1
```

**How it works**

- **Count the exponents.** For a prime p, 2ᵉ ≡ 1 (mod p) exactly when
  ord_p(2) divides e, and ord_p(2) divides p − 1 (Fermat). So among
  e = 0, 1, …, p − 1 there are 1 + (p − 1)/ord_p(2) hits, and the order is
  (p − 1)/6 exactly when the count is 7. No factoring, and 6 | p − 1 comes
  for free.
- **Only primes get a range.** `P` is (k − 1)!, so by Wilson's theorem
  `-P%k` is 1 for a prime, 0 for k = 1 and every composite k > 4, and 2 for
  k = 4: `range(-P%k*k)` is `range(k)` for a prime and empty (sum 0) for
  k = 1 and the composites above 4.
- `2**e%k==1` is the test 2ᵉ ≡ 1. Here it has to be `==1`, one byte more
  than the `<2` of the siblings: k = 4 is the one composite with a range
  (8 exponents), and 2ᵉ mod 4 = 1, 2, 0, 0, … would give exactly 7 hits
  with `<2`; with `==1` it has only e = 0. (The squared factorial,
  `range(P%k*k)` with `P*=k*k`, also avoids k = 4 and ties at 72.)
- The chained comparison `7==sum(…)==print(k)` prints only when the count
  is 7, and the list around it keeps the loop going.

**Notes**

- Exact for every n; it rests on Wilson's and Fermat's theorems only.
- Each prime p costs p powers 2ᵉ with up to p bits, about p² work per prime:
  69 terms in 50 s on the PC it was written on (every prime up to about
  10 500). The b-file has 1000 terms; the bar is 62 terms in 120 s.
- Faster but longer, as on A001133: `(1<<e)%k` (+2 bytes) or `pow(2,e,k)`
  (+4 bytes) print about 1.7 and 2.2 times as many terms in the same time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 72 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001136), CC BY-SA 4.0.
