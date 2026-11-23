# A002228

> Smallest prime p such that first n primes (p_1=2, ..., p_n) are 11th power residues mod p.
> — [OEIS A002228](https://oeis.org/A002228)

Offset 1: 331, 39139, 253243, 4397207, 21587171, 781712537, 781712537, 25467966877, 1304374210679, …

### Python 3 — 148 bytes

```python
p=23;P=m=1
while 1:
 m+=1
 while any(pow(q,p//11,p)>1for q in range(m+1))or 0in(p%d for d in range(2,4**len(str(p)))):p+=22
 P%m and print(p);P*=m*m
```

**How it works**

- **Which primes.** For a prime p ≢ 1 (mod 11), x ↦ x^11 is a bijection mod p and every number is an 11th power, so the entry counts only primes p ≡ 1 (mod 11): its data start at 331, the least such prime with 2 an 11th power residue, while under the other reading a(1) would be 3. So `p` runs over the odd numbers
  ≡ 1 (mod 11), that is 23, 45, 67, … in steps of 22, from the least prime
  of that form, and the program prints the first one that is prime and
  has each of the first n primes as a 11th power residue.
- **Euler's criterion.** Modulo a prime p ≡ 1 (mod 11) the nonzero 11th powers
  are the subgroup of index 11 of the cyclic group of units, so q (not a
  multiple of p) is a 11th power exactly when q^((p − 1)/11) ≡ 1; `p//11` is
  (p − 1)/11, and `pow(q,p//11,p)>1` flags a non-residue.
- **Every integer up to m.** 11th powers are closed under products, so the
  first n primes are residues exactly when every integer up to p_n is.
  The program tests q = 0, 1, …, m (0 and 1 give 0 and 1 and pass) instead
  of keeping a list of primes, and `any` stops at the first q that fails
  (usually 2). A prime p ≤ m cannot pass, since only (p − 1)/11 of 1, …, p − 1
  are 11th powers.
- **Primes m.** `m` runs over 2, 3, 4, … with `P` = ((m − 1)!)², so by
  Wilson's theorem `P%m` is 1 when m is prime and 0 otherwise. After the
  search for m the program prints `p` when m is prime, which is a(n) for
  m = p_n. At a composite m nothing changes (its prime factors were
  tested already): the search only checks `p` again.
- **Primality of p.** Only the candidates that pass every residue test
  get the trial division `0in(p%d for d in range(2,4**len(str(p))))`.
  With L digits, p < 10^L, so √p < 10^(L/2) < 4^L and every d ≤ √p is
  tried; for L ≥ 3, 4^L < 10^(L−1) ≤ p, so d never reaches p, and no candidate is below 16.
- **Resuming.** The conditions for n include those for n − 1, so
  a(n) ≥ a(n − 1) and the search goes on from the last term, testing it
  again first: that is how repeated terms come out.

**Notes**

- Exact integer arithmetic; Euler's criterion for 11th powers and Wilson's
  theorem make it right for every n.
- The search tests every candidate up to a(n), and the terms grow fast:
  here (1.5–2.6 times slower than the reference) a(5) = 21587171 comes after 6 s, while a(6) = 781712537 would take about four minutes. The bar is 5 terms in 60 s. The few terms in the bar fit in a table shorter than the
  program, so it went through a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 148 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002228), CC BY-SA 4.0.
