# A002185

> Smallest primitive factor of 2^(2n+1) + 1.
> — [OEIS A002185](https://oeis.org/A002185)

Offset 0: 3, 1, 11, 43, 19, 683, 2731, 331, 43691, 174763, 5419, 2796203, 251, 87211, 59, …

### Python 3 — 111 bytes

```python
import math
n=P=1
while 1:
 t=2**n+1;c=t//math.gcd(t,P);P*=t*t;p=n+1
 while c%p:p=[c,p+n][p*p<c]
 print(p);n+=2
```

**How it works**

- **Primitive factors.** In the program `n` is the odd exponent
  m = 2n + 1. A prime p | 2^m + 1 is primitive when it divides no
  2^d + 1 with d < m. The order of 2 mod such a p divides 2m but not m,
  so it is 2o with o | m and p | 2^o + 1: p is primitive exactly when
  the order is 2m, the primitive prime factors of 2^(2m) − 1. By
  Zsigmondy's theorem they exist for every odd m except m = 3
  (2^6 − 1 = 3²·7), where 9 = 3² has none and the entry has a(1) = 1;
  the program prints 1 there too.
- **The primitive part.** `P` is the product of (2^d + 1)² over the odd
  d < m, and `c` = t / gcd(t, P) with t = 2^m + 1. No primitive prime
  divides P. A non-primitive p | t has order 2o with o | m, o < m, so
  k = m/o is odd and at least 3. For odd j, p ∤ 2^(jo) − 1, and the
  lifting-the-exponent lemma gives v_p(2^(jo) + 1) = v_p(2^(2jo) − 1)
  = e + v_p(j) with e = v_p(2^o + 1) ≥ 1; so v_p(t) = e + v_p(k), and
  the (k − 1)/2 squared factors with j odd, j < k, give
  v_p(P) ≥ (k − 1)e ≥ e + v_p(k), since k − 2 ≥ v_p(k). So `c` is
  exactly the primitive part. The square matters only at m = 3, where
  t = 9 and P would be just 3.
- **Trial division.** Every prime factor of c has order 2m, so
  p ≡ 1 (mod 2m); the candidates m + 1, 2m + 1, 3m + 1, … include them
  all (the even ones never divide the odd c), and stepping by m
  instead of 2m saves 4 bytes. The first candidate that divides c is
  prime, since a prime factor of it would be a smaller candidate.
  `p=[c,p+n][p*p<c]` moves on while p² < c and otherwise jumps to c:
  every candidate up to √c gets tested, and if none divides, c is
  prime (or 1, at m = 3).

**Notes**

- Exact integer arithmetic throughout. The work per term is the least
  primitive factor or √c, divided by m. m = 61 needs 1.4·10⁷ steps; at
  m = 79 the primitive part is a 24-digit prime and trial division
  stalls (5.7·10⁹ steps), so the program prints a(0) to a(38), in
  about 5 s here (1.5–2.6 times slower than the reference), and then
  thinks for hours. The bar is 31 terms (a(0) to a(30)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 111 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002185), CC BY-SA 4.0.
