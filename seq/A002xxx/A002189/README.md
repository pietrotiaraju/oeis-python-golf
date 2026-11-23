# A002189

> Pseudo-squares: a(n) = the least nonsquare positive integer which is 1 mod 8 and is a (nonzero) quadratic residue modulo the first n odd primes.
> — [OEIS A002189](https://oeis.org/A002189)

Offset 0: 17, 73, 241, 1009, 2641, 8089, 18001, 53881, 87481, 117049, 515761, 1083289, …

### Python 3 — 128 bytes

```python
k=9;j=q=3;P=4;L=[]
while 1:
 if P%q:
  while any(pow(k,p//2,p)-1for p in L)or k==j*j:k+=8;j+=k>j*j
  print(k);L+=q,
 P*=q*q;q+=1
```

**How it works**

- **The definition, directly.** `k` runs over 9, 17, 25, … (the
  numbers ≡ 1 mod 8; 1 is a square) and the program prints the first
  one that is not a square and is a nonzero quadratic residue of every
  prime in `L`, the first n odd primes. This is the entry's definition
  word for word (and what its PARI program does), so it holds for
  every n with no theorem beyond Wilson's and Euler's below; the terms
  it reaches agree with the b-file.
- **Odd primes.** `q` runs over 3, 4, 5, … with `P` = ((q − 1)!)², so by
  Wilson's theorem `P%q` is 1 when q is prime and 0 otherwise
  ((q − 1)! ≡ 0 mod q for composite q > 4, and P = 36 at q = 4). When q
  is the (n + 1)-th odd prime, `L` still holds the first n, so the term
  printed is a(n); then q joins `L`.
- **Residues.** By Euler's criterion `pow(k,p//2,p)` is 1 when k is a
  nonzero quadratic residue of the odd prime p, p − 1 for a
  non-residue and 0 when p | k, so `pow(k,p//2,p)-1` is false exactly
  for the residues, and `any` stops at the first prime that rejects k
  (usually 3).
- **Squares.** `j` follows ⌈√k⌉: it starts at 3 with k = 9 and grows
  by one whenever k passes j². From k = 25 (j = 5) on, a step of 8
  never jumps over a square gap ((j + 1)² − j² = 2j + 1 > 8), so
  (j − 1)² < k ≤ j² and k is a square exactly when k = j²; the one
  exception, k = 17 with j = 4, is not a square either. A square passes
  every residue test, so this check is needed.
- **Resuming.** The conditions for n include those for n − 1, so
  a(n) ≥ a(n − 1) and the search goes on from the last term, testing it
  again first: that is how repeated terms such as
  a(16) = a(17) = 48473881 come out.

**Notes**

- Exact integer arithmetic. The search tests every k ≡ 1 (mod 8) up to
  a(n), and a(n) grows quickly (the b-file's 74 terms reach 25 digits,
  found by sieving), so few terms come in time: here (1.5–2.6 times
  slower than the reference) a(17) = 48473881 comes after 9 s, a(18)
  after 34 s and a(20) after 83 s, and a(21) = 898716289 would take
  about three minutes. The bar is 18 terms (a(0) to a(17)) in 60 s.
- A set instead of `any`, `{pow(k,p//2,p)for p in L}-{1}`, is 2 bytes
  shorter but tests every prime for every k: 3.5 times slower already
  at a(14), and more as `L` grows.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 128 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002189), CC BY-SA 4.0.
