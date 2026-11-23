# A002225

> a(n) is the smallest prime p such that each of the first n primes has three cube roots mod p.
> — [OEIS A002225](https://oeis.org/A002225)

Offset 1: 31, 307, 643, 5113, 21787, 39199, 360007, 360007, 4775569, …

### Python 3 — 145 bytes

```python
p=7;P=m=1
while 1:
 m+=1
 while any(pow(q,p//3,p)>1for q in range(m+1))or 0in(p%d for d in range(2,4**len(str(p)))):p+=6
 P%m and print(p);P*=m*m
```

**How it works**

- **Which primes.** The name asks for three cube roots, which happens exactly when p ≡ 1 (mod 3) and q is a cubic residue (for p ≢ 1 (mod 3) cubing is a bijection and every number has exactly one cube root), as R. Israel's comment on the entry says. So `p` runs over the odd numbers
  ≡ 1 (mod 3), that is 7, 13, 19, … in steps of 6, from the least prime
  of that form, and the program prints the first one that is prime and
  has each of the first n primes as a cubic residue.
- **Euler's criterion.** Modulo a prime p ≡ 1 (mod 3) the nonzero cubes
  are the subgroup of index 3 of the cyclic group of units, so q (not a
  multiple of p) is a cube exactly when q^((p − 1)/3) ≡ 1; `p//3` is
  (p − 1)/3, and `pow(q,p//3,p)>1` flags a non-residue.
- **Every integer up to m.** Cubes are closed under products, so the
  first n primes are residues exactly when every integer up to p_n is.
  The program tests q = 0, 1, …, m (0 and 1 give 0 and 1 and pass) instead
  of keeping a list of primes, and `any` stops at the first q that fails
  (usually 2). A prime p ≤ m cannot pass, since only (p − 1)/3 of 1, …, p − 1
  are cubes.
- **Primes m.** `m` runs over 2, 3, 4, … with `P` = ((m − 1)!)², so by
  Wilson's theorem `P%m` is 1 when m is prime and 0 otherwise. After the
  search for m the program prints `p` when m is prime, which is a(n) for
  m = p_n. At a composite m nothing changes (its prime factors were
  tested already): the search only checks `p` again.
- **Primality of p.** Only the candidates that pass every residue test
  get the trial division `0in(p%d for d in range(2,4**len(str(p))))`.
  With L digits, p < 10^L, so √p < 10^(L/2) < 4^L and every d ≤ √p is
  tried; for L ≥ 3, 4^L < 10^(L−1) ≤ p, so d never reaches p, and the two-digit candidate 13 (below 16) fails earlier, since 2 is not a cube mod 13 (2^4 ≡ 3).
- **Resuming.** The conditions for n include those for n − 1, so
  a(n) ≥ a(n − 1) and the search goes on from the last term, testing it
  again first: that is how repeated terms come out.

**Notes**

- Exact integer arithmetic; Euler's criterion for cubes and Wilson's
  theorem make it right for every n.
- The search tests every candidate up to a(n), and the terms grow fast:
  here (1.5–2.6 times slower than the reference) a(11) = 10318249 comes after 7 s and a(12) = 65139031 after 50 s, while a(13) = 387453811 would take about five minutes. The bar is 12 terms in 120 s. The few terms in the bar fit in a table shorter than the
  program, so it went through a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 145 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002225), CC BY-SA 4.0.
