# A000236

> Maximum m such that there are no two adjacent elements belonging to the same n-th power residue class modulo some prime p in the sequence 1,2,...,m (equivalently, there is no n-th power residue modulo p in the sequence 1/2,2/3,...,(m-1)/m).
> — [OEIS A000236](https://oeis.org/A000236)

Offset 2: 3, 8, 20, 44, 80, 343, 288, 608, 1023, 2848, 4095, 40959, …

### Python 3 — 216 bytes

```python
f=lambda F,k:max([f(F+[v],k+1)for v in{(F[a]+F[k//a])%d for a in range(2,k)if k%a<1}or range(d)if v-F[-1]and v+F[0]*~-k//4&1<=d%(2*k)]+[k-1])
n=2
while[print(max(f([D,0],2)for D in range(2*n)if n%(d:=n-D%n)<1))]:n+=1
```

**How it works**

- **Classes as a map.** Take a prime p > m and g = gcd(n, p−1). The n-th
  powers mod p are exactly the g-th powers, their cosets form a cyclic group
  of order g, and k ↦ (class of k) is a completely additive map f from the
  positive integers to Z/g, a discrete logarithm mod g. So a(n) is the
  longest start 1..m on which some such f has f(k) ≠ f(k+1).
- **Which maps occur.** For primes p ≡ 1 (mod d), Chebotarev's theorem in
  Q(ζ_d)(q^(1/d) : q ≤ m) gives every additive map into Z/d except those
  that break a Kummer relation. By Schinzel's theorem on abelian binomials, a
  positive rational is a d-th power in Q(ζ_d) only when it is b^(d/2) with
  √b ∈ Q(ζ_d). So the only constraints are on parities: for a prime q with
  2q | d, f(q) mod 2 is the Legendre symbol (q/p), and with p = 1 + T
  quadratic reciprocity makes it T(q−1)/4 mod 2 (for q = 2 and 4 | d the same
  formula comes from (p²−1)/8). This is Don Reble's correction on the OEIS
  page, plus one free bit, the parity of T/d. For d ≡ 2 (mod 4) that bit
  gives all primes q ≡ 3 (mod 4) dividing d the same parity. For d ≡ 4
  (mod 8) it frees f(2).
- **Divisors.** At a prime p ≡ 1 (mod d) the classes for gcd(n, p−1) refine
  the d-th power classes, so a(n) is the maximum over d | n of the best map
  into Z/d.
- **One loop for d and T.** For D in range(2n), d = n − D mod n takes every
  value 1..n twice, and `n%d<1` keeps the divisors. T = D is always a
  multiple of d. For d = n, T/d is 0 or 1. Otherwise T/d is n/d − 1 or
  2n/d − 1, so both parities occur when n/d is odd. When n/d is even, the
  missing case (p ≡ 1 mod 2d) is already covered by the divisor 2d, whose
  classes refine those of d. T goes into F[0], an index that is never read as
  a value of f. The walrus makes d a global, which f can read; a loop variable
  of the generator would be invisible to f (6 bytes cheaper than passing d
  down the recursion).
- **Search.** F[k] = f(k) mod d with F[1] = 0, filled in order. For a
  composite k every split a·(k/a) gives the same value, so the set has one
  element. For a prime it is empty, and all d values are tried. A candidate
  must differ from F[-1] = f(k−1) and pass `v+F[0]*~-k//4&1<=d%(2*k)`. If
  2k ∤ d, the right side is at least 1 and the test always passes. If 2k | d,
  it says v ≡ T(k−1)/4 (mod 2). On composites the test also always passes,
  because T(k−1)/4 adds up the same way the parities of the prime factors
  do, so it needs no prime test of its own. A dead end at k returns k − 1, the
  length of the valid start.
- **Termination.** The tree has finite branching. An infinite branch would be
  a map that every prime-realizable prefix extends, making a(n) infinite, so
  every branch ends because a(n) is finite (Jordan 1964).

**Notes**

- The same model, solved with CP-SAT (one Z/d variable per prime, each
  adjacent pair a nonzero linear form mod d, the parity rule for each
  (d, T/d mod 2)), is satisfiable at m = a(n) and unsatisfiable at a(n) + 1
  for n = 6, 7, 8, 9, 10 and 12, matching the OEIS terms. n = 8 is the first
  case where the parity rule matters: f(2) must be even.
- a(2) to a(5) come out at once, but a(6) = 80 takes more than 10 minutes:
  with 4 free values per prime, the d = 6 tree is huge. The bar is 4 terms.
- The recursion is a(n) + 2 frames deep, past Python's default limit of 1000
  from a(10) = 1023 on (an interpreter limit, not a wrong answer).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 216 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000236), CC BY-SA 4.0.
