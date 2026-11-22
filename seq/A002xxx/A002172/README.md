# A002172

> Glaisher's chi numbers chi(p) for p a prime of the form 4m+1.
> — [OEIS A002172](https://oeis.org/A002172)

Offset 1: -2, 6, 2, -10, -2, 10, 14, -10, -6, 10, 18, -2, …

### Python 3 — 92 bytes

```python
P=k=1
while[P%k*k%4==1==print(k+3-2*sum(pow(x**3-x,k//2,k)<2for x in range(k)))]:P*=k*k;k+=1
```

**How it works**

- **Point count.** Glaisher's χ(p) is the coefficient of q^p in
  η(4τ)²η(8τ)², the newform of the elliptic curve y² = x³ − x
  (conductor 32, "32a2"; Martin and Ono 1997, Theorem 2, row N = 32,
  quoted in [A002171](../A002171/)). So for every prime p,
  χ(p) = p − N_p, where N_p is the number of solutions of
  y² ≡ x³ − x (mod p). Each x gives 1 + ((x³ − x)/p) values of y
  (Legendre symbol), so N_p = p + Σ_x ((x³ − x)/p) and
  χ(p) = −Σ_(x mod p) ((x³ − x)/p), which is also the entry's own PARI
  program.
- **Euler's criterion.** For an odd prime p, (x³ − x)^((p−1)/2) mod p is
  0, 1 or p − 1 as x³ − x is 0, a nonzero square or a non-square. With
  c the number of x giving a value `<2` (zero or a square), and
  x³ − x ≡ 0 for exactly three x (0, 1 and p − 1, distinct for p ≥ 5),
  there are c − 3 squares and p − c non-squares, so the Legendre sum is
  2c − p − 3 and χ(p) = p + 3 − 2c: that is
  `k+3-2*sum(pow(x**3-x,k//2,k)<2for x in range(k))`.
- **Primes ≡ 1 (mod 4).** `P` = ((k − 1)!)², so by Wilson's theorem
  `P%k` is 1 for a prime k and 0 otherwise (k = 1 and k = 4 included:
  P = 1 is ≡ 0 mod 1, and 36 ≡ 0 mod 4). `P%k*k%4==1` therefore holds
  exactly for the primes k ≡ 1 (mod 4), and in the chain
  `P%k*k%4==1==print(…)` the print runs only then.
- `while[…]:` never ends: the list is true whatever it holds.

**Notes**

- Wilson's theorem, Euler's criterion and exact integers: right for every
  n, given the modularity of y² = x³ − x (classical for this curve with
  complex multiplication by Z[i]).
- Each prime p costs p modular powers: the whole b-file (1000 terms,
  p up to 17657) comes in 6.5 reference seconds (11 s here), and the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002172), CC BY-SA 4.0.
