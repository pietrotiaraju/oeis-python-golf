# A000446

> Smallest number that is the sum of 2 squares (allowing zeros) in exactly n ways.
> — [OEIS A000446](https://oeis.org/A000446)

Offset 1: 0, 25, 325, 1105, 4225, 5525, 203125, 27625, 71825, 138125, …

Representations m = x² + y² are counted with 0 ≤ x ≤ y.

### Python 3 — 193 bytes

```python
F=lambda d,i:d<2or min(P[i]**~-k*F(d//k,i+1)for k in range(2,d+1)if d%k<1)
c=0;P=[];p=t=1
while 1:
 while 2**len(P)<=c:t*=p*p;p+=1;P+=[p]*(t%p>0<p%4<2)
 print(c and min(F(c+1,0),F(c+2,0)));c+=2
```

**How it works**

- **The count.** Write m = 2^a·Π pᵉ·Π q^f with p ≡ 1 and q ≡ 3 (mod 4).
  If some f is odd there is no representation; otherwise there are
  r₂(m) = 4B signed ordered ones, B = Π (e+1). A pair 0 < x < y gives 8
  of them, a pair with x = 0 or x = y gives 4, and such a pair exists
  exactly when m or m/2 is a square, that is when B is odd. So m has
  ⌈B/2⌉ representations, and exactly n of them means B = 2n − 1 or
  B = 2n.
- **The shape of the minimum.** Powers of 2 and squares of the q change
  nothing in B, so a minimal m > 0 is Π pᵢ^(eᵢ) over primes ≡ 1 (mod 4).
  Its primes are the smallest ones, 5, 13, 17, 29, …, used consecutively
  (a used prime above an unused one can be swapped down), and
  F(d, i) = the least Π_{j≥i} P[j]^(e_j) with Π (e_j + 1) = d, using
  P[i], P[i+1], … in order with every exponent at least 1, satisfies
  F(1, i) = 1 and F(d, i) = min over divisors k ≥ 2 of d of
  P[i]^(k−1)·F(d/k, i+1). Skipping the ordering condition on the
  exponents only adds candidates that are valid numbers anyway.
- **The code.** c = 2n − 2, so the two targets are c + 1 and c + 2;
  `c and …` prints a(1) = 0 (0 = 0² + 0²) without calling F. `d<2or` makes
  F(1, i) = `True`, which multiplies as 1. F only reads P[i] when d ≥ 2
  is left after i factors of at least 2, so 2^(i+1) ≤ 2n and
  i ≤ log₂ n; `while 2**len(P)<=c:` makes len(P) at least the bit length
  of c = 2n − 2, which is more than log₂ n.
- **The primes.** Before p is tested, t = ((p−1)!)², so by Wilson's
  theorem t mod p is 1 for a prime p and 0 for a composite one (for p = 4,
  36 mod 4 = 0); `t%p>0<p%4<2` keeps the primes ≡ 1 (mod 4).

**Notes**

- Other versions that print the same terms: the same lambda wrapped in
  `cache` (with `from functools import*`): 223 bytes, and faster on the
  targets with many divisors; the first versions with a divisor helper,
  a nonincreasing-exponent bound and `isqrt`: 361 bytes and up.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 1458 terms print in 2.8 s here, and the program reaches
  the 4300-digit limit in about 53 s. The b-file has 1458 terms (up to
  a(1458)); the bar is the whole b-file in 60 s.
- When n and 2n − 1 are both prime, B = 2n − 1 forces 5^(2n−2) and B = 2n
  gives at best 5^(n−1)·13, so a(n) = 13·5^(n−1). The first n where this
  has more than 4300 digits is 6211, so printing stops at a(6211).
- [A000448](../A000448/) asks for at least n ways.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 410 | first entry |
| 2026-11-06 | Python 3 | 405 | simplify the minimum expression |
| 2026-11-06 | Python 3 | 370 | use Wilson prime generation, cached lambdas and a shared target |
| 2026-11-06 | Python 3 | 361 | short-circuit the exhausted-factor base case |
| 2026-11-07 | Python 3 | 193 | min over divisors without exponent bound or cache, `2**len(P)<=c` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000446), CC BY-SA 4.0.
