# A000229

> a(n) is the least number m such that the n-th prime is the least quadratic nonresidue modulo m.
> — [OEIS A000229](https://oeis.org/A000229)

Offset 1: 3, 7, 23, 71, 311, 479, 1559, 5711, 10559, 18191, …

### Python 3 — 133 bytes

```python
p=1
while 1:
 p+=1;m=3
 while p%(w:=next(b for b in range(m)if pow(b,m//2,m)>1))or 0in(m%d for d in range(2,m)):m+=2
 w<p or print(m)
```

**How it works**

- For each p = 2, 3, 4, … the inner loop walks the odd m from 3 and takes
  the witness w, the least b with b^((m−1)/2) mod m > 1. For a prime m,
  Euler's criterion makes w the least quadratic nonresidue (the values are
  0 at b = 0, 1 at residues and m − 1 at nonresidues).
- w always exists and is always prime, for every odd m ≥ 3. If b = st with
  s, t < b, both values are 0 or 1, so b's value is 0 or 1 too. And some
  b < m has a value above 1: a nonresidue when m is prime, the smallest
  prime factor r of m when m has two different prime factors (its value is
  a nonzero multiple of r), and a primitive root when m = r^e, since
  (m − 1)/2 is prime to r and so not a multiple of the order r^(e−1)(r − 1).
- The loop stops at the first prime m whose witness divides p, and prints
  m only if w = p. For a prime p that is the first prime m whose least
  nonresidue is p. For a composite p, w is one of its prime factors, so
  nothing is printed and the loop stops soon (every prime is a witness,
  and the smallest factor of p is small). This skips the composite p
  without testing p at all.
- The trial division `0in(m%d …)` runs only when w divides p, so in
  practice once per term plus the composite m that pass the Euler test.
  It can't be dropped: a composite m with b^((m−1)/2) ≡ 1 (mod m) for
  every b < p and p as its witness is not ruled out by any theorem. Such an
  m has no prime factor below p (for a factor r < p the base r gives a
  nonzero multiple of r, or, if m is a power of r, the bases 2 … r − 1
  can't all have order dividing r − 1 modulo r²), so checking small
  divisors only wouldn't do either.
- The least m overall is a prime, as the definition wants (OEIS uses "least
  non-square mod m", with nothing about coprimality). If 4 | m, 2 is a
  non-square; m = 2u has the same squares as u; and for an odd m, b < r is
  a square mod r^e exactly when it is a residue mod r, so the least
  non-square of m is the smallest least nonresidue among its prime factors
  r, and a composite m with p there has a prime factor r < m that gets p
  first. A brute force over all m with the set of squares agrees on the
  first 8 terms.

**Notes**

- a(n) exists for every n (Dirichlet's theorem on primes with prescribed
  Legendre symbols, through quadratic reciprocity), so every search ends.
- Each p starts again from m = 3, since the sequence isn't monotonic
  (a(14) < a(13)). That costs about Σ a(k)/2 Euler tests up to a(n): here
  a(15) comes at 22 s and a(16) at 54 s. The bar is 15 terms in 60 s.
- Making p run over primes with Wilson's theorem (K = ((p−1)!)², p prime
  when K % p is 1) and printing from the loop condition is 140 bytes. The
  `p%w` test above replaces that prime test.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 133 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000229), CC BY-SA 4.0.
