# A002223

> Smallest prime p of form p = 8k-1 such that first n primes (p_1=2, ..., p_n) are quadratic residues mod p.
> — [OEIS A002223](https://oeis.org/A002223)

Offset 1: 7, 23, 71, 311, 479, 1559, 5711, 10559, 18191, 31391, 366791, 366791, …

### Python 3 — 149 bytes

```python
p=7;m=3;P=4;L=[]
while 1:
 if P%m:print(p);L+=m,
 while any(pow(-p,q//2,q)-1for q in L)or 0in(p%d for d in range(2,4**len(str(p)))):p+=8
 P*=m*m;m+=1
```

**How it works**

- **The definition, directly.** `p` runs over the numbers ≡ 7 (mod 8)
  from 7 on (the least prime of that form), and the program prints
  the first one that is prime and has each of the first n primes as a
  quadratic residue. The conditions for n include those for n − 1, so
  a(n) ≥ a(n − 1) and the search goes on from the last term, testing it
  again first: that is how repeated terms come out.
- **Residues mod the small prime.** For a prime p ≡ 3 (mod 4) and an odd prime q ≠ p, quadratic reciprocity gives (q/p) = (−1)^((q−1)/2)·(p/q) = (−p/q), so by Euler's criterion
  modulo q the prime q is a residue of p exactly when `pow(-p,q//2,q)` is 1.
  This powers modulo the small q instead of modulo p, three times faster.
  2 is a residue of every prime p ≡ 7 (mod 8) (the second supplementary law), so `L` never needs 2 and holds the odd primes 3, 5, 7, … only. If q divides p the power is 0 and p is rejected: p is then
  composite, or p = q ≤ p_n, which is no term anyway (the least
  non-residue of an odd prime p is a prime below p, so it would be
  one of the first n primes).
- **Primes q.** `m` runs over 3, 4, 5, … with `P` = ((m − 1)!)², so by
  Wilson's theorem `P%m` is 1 when m is prime and 0 otherwise. At a prime
  m the program first prints the current `p`, the answer for the primes
  below m, then adds m to `L` and searches on; the first print, at m = 3,
  is a(1) = 7, for which only 2 has to be a residue.
- **Primality of p.** Only the candidates that pass every residue test
  get the trial division `0in(p%d for d in range(2,4**len(str(p))))`.
  With L digits, p < 10^L, so √p < 10^(L/2) < 4^L and every d ≤ √p is
  tried; for L ≥ 3, 4^L < 10^(L−1) ≤ p, so d never reaches p. The only two-digit candidate below 16 is 15, which is composite.
  The bound is shorter than `math.isqrt` with its import.

**Notes**

- Exact integer arithmetic; quadratic reciprocity, Euler's criterion and
  Wilson's theorem make it right for every n.
- The search tests every candidate up to a(n), and the terms grow
  quickly (the b-file's 57 terms reach 19 digits). Here (1.5–2.6 times
  slower than the reference) a(14) = 4080359 comes after 1 s, a(18) = 82636319 after 18 s and a(22) = 131486759 after 27 s; a(23) = 2929911599 would take about ten minutes. The bar is 22 terms in 60 s.
- The 22 terms of the bar fit in a table shorter than the program, so
  it went through a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 149 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002223), CC BY-SA 4.0.
