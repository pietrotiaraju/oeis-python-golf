# A001133

> Primes p such that the multiplicative order of 2 modulo p is (p-1)/3.
> — [OEIS A001133](https://oeis.org/A001133)

Offset 1: 43, 109, 157, 229, 277, 283, 307, 499, 643, 691, 733, 739, 811, 997, 1021, 1051, 1069, 1093, 1459, 1579, …

One of four siblings: ord_p(2) = (p − 1)/k for k = 3 (this page), 4
([A001134](../A001134/)), 5 ([A001135](../A001135/)) and 6
([A001136](../A001136/)); the programs differ in one constant.

### Python 3 — 71 bytes

```python
P=k=1
while[4==sum(2**e%k<2for e in range(-P%k*k))==print(k)]:P*=k;k+=1
```

**How it works**

- **Count the exponents.** For a prime p, 2ᵉ ≡ 1 (mod p) exactly when
  ord_p(2) divides e, and ord_p(2) divides p − 1 (Fermat). So among
  e = 0, 1, …, p − 1 the hits are the multiples of the order, and there are
  1 + (p − 1)/ord_p(2) of them. The order is (p − 1)/3 exactly when the count
  is 4. Nothing has to be factored, and 3 | p − 1 comes for free.
- **Only primes get a range.** As in [A000040](../../A000xxx/A000040/), `P` is
  (k − 1)!, and Wilson's theorem makes `-P%k` 1 for a prime, 0 for k = 1 and
  every composite k > 4, and 2 for k = 4. So `range(-P%k*k)` is `range(k)`
  for a prime and empty for the rest (sum 0), except k = 4, where it has 8
  exponents and 2ᵉ mod 4 = 1, 2, 0, 0, … gives 7 hits, not 4.
- `2**e%k<2` is the test 2ᵉ ≡ 1: for an odd prime the residue is never 0.
  (For p = 2 the count is 2.)
- The chained comparison `4==sum(…)==print(k)` prints only when the count
  is 4, and the list around it keeps the loop going.

**Notes**

- Exact for every n; it rests on Wilson's and Fermat's theorems only.
- Each prime p costs p powers 2ᵉ with up to p bits, so the work grows like
  p² per prime and the program slows down fast: 89 terms in 50 s on the PC it
  was written on (every prime up to about 10 500). The b-file has 1000 terms; the bar is 80
  terms in 120 s.
- Faster but longer: `(1<<e)%k` (73 bytes) builds the power with a shift
  instead of repeated squaring, and `pow(2,e,k)` (75 bytes) never makes it
  big; they print about 1.7 and 2.2 times as many terms in the same time.
- The test `0<-P%k*4==sum(…for e in range(k))` also skips the composites, 2
  bytes longer; dropping its `0<` ties at 71 but then every k, not just the
  primes, runs the inner loop.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001133), CC BY-SA 4.0.
