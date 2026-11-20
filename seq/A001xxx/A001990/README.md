# A001990

> Let p be the n-th odd prime. a(n) is the least prime congruent to 5 modulo 8 such that Legendre(-a(n), q) = -Legendre(-2, q) for all odd primes q <= p.
> — [OEIS A001990](https://oeis.org/A001990)

Offset 1: 5, 29, 29, 29, 29, 29, 29, 29, 23669, 23669, 23669, 23669, …

### Python 3 — 148 bytes

```python
r=5;P=4;q=3;Q=[]
while 1:
 if P%q:
  Q+=q,
  while any(pow(-2*r,d//2,d)<2for d in Q)or 0in(r%d for d in range(2,r//q)):r+=24
  print(r)
 P*=q*q;q+=1
```

**How it works**

- **Odd primes.** `q` runs through 3, 4, 5, … with `P` = ((q − 1)!)², so by
  Wilson's theorem `P%q` is 1 when q is prime and 0 otherwise (q = 4
  included). Each odd prime is appended to `Q` and gives one term: after
  the n-th odd prime p, `Q` holds exactly the odd primes ≤ p.
- **Legendre symbols.** For an odd prime d, Euler's criterion makes
  `pow(-2*r,d//2,d)` equal to 1, d − 1 or 0 when Legendre(−2r, d) is 1, −1
  or 0 (Python's three-argument `pow` takes a negative base as it is).
  As d ≥ 3, d − 1 ≥ 2, so `<2` flags every d where the symbol is not −1.
- **Search.** A prime that works for the first n + 1 odd primes works for
  the first n, so the sequence is nondecreasing and the search for the
  next term resumes at the current `r`. Every term is ≡ 5
  (mod 24): it is ≡ 5 (mod 8) by definition, and
  Legendre(−2r, 3) = −1 means −2r ≡ 2 (mod 3), so r ≡ 2 (mod 3). So `r` starts at 5 and steps by 24
  without skipping a candidate.
- **Primality.** Trial division runs only on an `r` that passed every
  Legendre test. Such an `r` is odd and has no prime factor d ≤ q (that
  would make the symbol 0). So if it is composite, its least prime
  factor s has q + 1 ≤ s ≤ r/s ≤ r/(q + 1), and r ≥ s² ≥ (q + 1)² ≥ q(q + 1)
  turns that into s ≤ r/q − 1 < ⌊r/q⌋: `range(2,r//q)` reaches s. For a
  prime `r` it holds no divisor. Bounding the trial division by r/q
  instead of r makes it negligible next to the search.

**Notes**

- **The title has a sign slip; the program follows the data.** Taken
  literally, Legendre(−a(n), q) = −Legendre(−2, q) gives 13, 61, 61, 181,
  … (a brute force over the primes ≡ 5 (mod 8)), not 5, 29, 29, ….
  The data and the PARI program in the entry use
  Legendre(a(n), q) = −Legendre(−2, q), which is Legendre(−2a(n), q) = −1
  after multiplying both sides by Legendre(−2, q) = ±1. The program
  tests that form, which reproduces the data.
- Every search ends: the conditions fix r modulo 8·3·5⋯p to a nonempty set
  of classes prime to the modulus (Chinese remainder theorem), and
  Dirichlet's theorem puts primes in them.
- Exact integer arithmetic and trial division, so no probable-prime test is
  involved. The b-file holds the 26 terms of the entry's data. Here (about
  1.7 times slower than the reference) a(24) comes after 3 s and a(25) =
  a(26) = 240511301 after 18 s; the program then prints 240511301 once
  more, for n = 27, which the data does not list. The bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 148 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001990), CC BY-SA 4.0.
