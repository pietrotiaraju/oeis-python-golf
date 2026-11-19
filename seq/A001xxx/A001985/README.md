# A001985

> Class numbers associated with terms of A002223.
> — [OEIS A001985](https://oeis.org/A001985)

Offset 1: 1, 3, 7, 19, 25, 51, 109, 153, 213, 289, 1121, 1121, …

### Python 3 — 225 bytes

```python
r=7;P=1;q=2
while 1:
 a=h=0
 if P%q:
  while any(pow(d,r//2,r)>1for d in range(q+1))or 0in(r%d for d in range(2,r//q)):r+=8
  while 3*a*a<r:a+=1;h+=sum((x:=b*b+r>>2)%a<1>a*a-x for b in range(-a|1,a,2))
  print(h)
 P*=q*q;q+=1
```

**How it works**

- **Which sequence.** a(n) = h(−p) for p = [A002223](https://oeis.org/A002223)(n), the least prime
  p ≡ 7 (mod 8) such that the first n primes 2, 3, …, p_n are quadratic
  residues modulo p; h(−p) is the class number of Q(√−p) (the comment in
  the entry), the number of reduced forms of discriminant −p. The first
  terms of A002223 are 7, 23, 71, 311, 479, …, with h = 1, 3, 7, 19, 25, ….
- **Primes p_n.** `q` runs through 2, 3, 4, … with `P` = ((q − 1)!)², so by
  Wilson's theorem `P%q` is 1 exactly when q is prime: each prime gives one
  term, with q = p_n.
- **Residues.** For a prime r > q, every d ≤ q is a residue as soon as every
  prime ≤ q is (the Legendre symbol is multiplicative), so the test runs
  over all of d = 0, …, q, and Euler's criterion makes `pow(d,r//2,r)`
  1 for a residue and r − 1 for a nonresidue (0 and 1 always pass). A
  prime r ≤ q fails, since some d < r is a nonresidue. `r` runs over
  7, 15, 23, …, the numbers ≡ 7 (mod 8) (2 is a residue of all such
  primes, so p_1 = 2 asks nothing more). A prime that
  works for p_(n+1) works for p_n, so the search for the next term
  resumes at the current `r`.
- **Primality.** Trial division runs only on an `r` that passed the Euler
  test, and such an `r` has no prime factor p ≤ q: `pow(p,r//2,r)` is a
  multiple of p, so it passes only as 0, which makes r a power p^j; if
  j ≥ 2, the base p − 1 (≤ q and prime to r) must give 1, but p − 1 has
  order 2p modulo p² ((p − 1)² ≡ 1 − 2p), and 2p | (r − 1)/2 is impossible
  when p | r. So a composite `r` has its least prime factor s with
  q + 1 ≤ s ≤ r/(q + 1), and r ≥ s² ≥ q(q + 1) turns that into
  s < ⌊r/q⌋: `range(2,r//q)` reaches s, and holds no divisor of a prime.
- **Class number.** h(−r) is the number of reduced forms ax² + bxy + cy²
  of discriminant b² − 4ac = −r: |b| ≤ a ≤ c, and b ≥ 0 when |b| = a or
  a = c. For a prime r ≡ 3 (mod 4), r > 3, every such form is primitive
  (a common factor g has g² | r), b is odd, a = c is impossible
  (r = (2a − b)(2a + b) would force |b| = (r − 1)/2 > a) and |b| = a
  forces a | r, so a = 1. Hence h(−r) counts the pairs (a, b), b odd in
  [−a, a), with a | x and a² ≤ x for x = (b² + r)/4 = ac: for a ≥ 2 the
  admissible b are symmetric and miss ±a, and at a = 1 the range takes
  b = −1 in place of b = 1. a ≤ c gives 4a² ≤ b² + r ≤ a² + r, so
  a runs while 3a² < r. `-a|1` is the first odd number ≥ −a, and
  `b*b+r>>2` is x exactly, as b² + r ≡ 0 (mod 4).
  The counters `a` and `h` start from 0 on every pass of the outer loop.

**Notes**

- Every search ends: the conditions fix r modulo 8·p₂⋯p_n to a nonempty
  set of classes prime to the modulus (Chinese remainder theorem), and
  Dirichlet's theorem puts primes in them.
- Exact integer arithmetic throughout. The Euler test costs a few modular
  powers with modulus r per candidate, and r steps by 8, so the search is
  slower than in [A001986](../A001986/): here (about 1.7 times slower than
  the reference) a(15), the bar, comes after 12 s and a(17) after 37 s.
  Testing d against a list of the primes found so far, modulo d instead of
  r, is about three times faster and 5 bytes longer. The bar is 15 terms
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 225 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001985), CC BY-SA 4.0.
