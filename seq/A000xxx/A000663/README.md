# A000663

> Number of binary relations on an infinite set, each with exactly n ordered pairs, up to isomorphism.
> — [OEIS A000663](https://oeis.org/A000663)

Offset 0: 1, 2, 9, 37, 183, 933, 5314, 32043, 207212, 1415934, 10200289, 77018442, …

### Python 3 — 182 bytes

```python
from math import*
f=lambda r,*L:r<1or sum(f(r-k,*L,k)*prod((1+B**lcm(k,d))**gcd(k,d)for d in(*L,*L,k))%B**-~n for k in range(1,r+1))//r
n=0
while 1:B=9**n**2;print(f(2*n)//B**n);n+=1
```

**What is counted**

- A relation with n ordered pairs touches at most 2n elements. Adding or
  deleting untouched elements is harmless, so the classes on an infinite
  set are the classes of relations with exactly n pairs on N = 2n points,
  up to S_N: the coefficient of xⁿ in Burnside's sum
  (1/N!) Σ_σ Π_orbits (1 + x^|orbit|) over the orbits of σ on the N²
  ordered pairs (loops included), as in the formula of Michael Spiegel in
  the entry. Two cycles of lengths a and b (or one cycle twice, a = b)
  carry gcd(a, b) orbits of size lcm(a, b).

**How it works**

- The recursion of [A000250](../A000250/) on the cycle through one of the
  r remaining points, `//r` at every level, but with polynomials instead of
  powers of two. A new cycle of length k brings its own k orbits of size k
  and gcd(k, d) orbits of size lcm(k, d) in each direction for every
  earlier cycle d, so its factor is the product of
  (1 + x^lcm(k, d))^gcd(k, d) over d in `(*L,*L,k)` (gcd(k, k) = lcm(k, k)
  = k).
- **Packed polynomials.** x is the integer B = 9^(n²), and every product is
  reduced mod B^(n+1), keeping the coefficients of x⁰, …, xⁿ as base-B
  digits. A coefficient of r·f(r, L) is at most 2n·C(4n², n) labelled
  relations, which is below 9^(n²) for every n ≥ 1, so no digit up to xⁿ
  ever overflows. Higher digits of the unreduced products may carry, but
  carries only move upwards and `%B**-~n` drops them.
- Each coefficient of the sum is r times an orbit count (de Bruijn's lemma
  works coefficient by coefficient, since σ preserves the number of
  pairs), so `//r` on the packed integer divides every digit exactly.
- f(2n) < B^(n+1), so its top digit `f(2*n)//B**n` is a(n). For n = 0,
  B = 1 and f(0) is `True`, which prints as 1 after `//1`.

**Notes**

- The recursion runs over all 2^(2n−1) compositions of 2n with growing
  packed numbers: 9 terms in about 18 s here, the tenth would take minutes.
- The bar is 7 terms in 60 s; the b-file has 41.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 182 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000663), CC BY-SA 4.0.
