# A002184

> a(n) = least primitive factor of 2^(2n+1) - 1.
> — [OEIS A002184](https://oeis.org/A002184)

Offset 0: 1, 7, 31, 127, 73, 23, 8191, 151, 131071, 524287, 337, 47, 601, 262657, 233, …

### Python 3 — 109 bytes

```python
import math
n=P=1
while 1:
 t=2**n-1;c=t//math.gcd(t,P);P*=t;p=n+1
 while c%p:p=[c,p+n][p*p<c]
 print(p);n+=2
```

**How it works**

- **Primitive factors.** In the program `n` is the odd exponent
  m = 2n + 1. A prime p is a primitive factor of 2^m − 1 when it
  divides 2^m − 1 but no 2^d − 1 with d < m, that is when 2 has order
  exactly m mod p. For m = 1 there is none, and the entry has
  a(0) = 1; for every odd m > 1 there is one (Zsigmondy's theorem,
  Bang's for base 2), so the other terms are primes.
- **The primitive part.** `P` is the product of 2^d − 1 over the odd
  d < m, and `c` = t / gcd(t, P) with t = 2^m − 1. No primitive prime
  divides P. A non-primitive prime p | t has odd order o < m, o | m,
  so k = m/o is odd and at least 3, and p ≥ 7 (3 has order 2). By the
  lifting-the-exponent lemma, v_p(2^(jo) − 1) = e + v_p(j) with
  e = v_p(2^o − 1) ≥ 1, so v_p(t) = e + v_p(k), while P contains the
  (k − 1)/2 factors 2^(jo) − 1 with j odd and j < k, so
  v_p(P) ≥ (k − 1)e/2 ≥ e + v_p(k) (when p | k, k ≥ 7 and
  v_p(k) ≤ log₇ k). So `c` is exactly the product of the primitive
  prime powers of t.
- **Trial division.** Every prime factor p of c has order m, so
  p ≡ 1 (mod m), and the candidates are m + 1, 2m + 1, 3m + 1, … (the
  even ones never divide the odd c; stepping by m instead of 2m saves
  4 bytes and doubles the steps). The first candidate that divides c is
  prime, since a prime factor of it would be a smaller candidate
  dividing c. `p=[c,p+n][p*p<c]` moves on while p² < c and otherwise
  jumps to c: every candidate up to √c gets tested, and if none
  divides, c has no prime factor below its square root, so it is prime
  (or 1, for m = 1, where `p` lands on 1).

**Notes**

- Exact integer arithmetic throughout. The work per term is the least
  primitive factor or √c, divided by m: m = 61 (2^61 − 1 is prime)
  needs 2.5·10⁷ steps and m = 85 4·10⁷, and at m = 89 (2^89 − 1 is
  prime, √c ≈ 2.5·10¹³) trial division stalls, so the program prints
  a(0) to a(43) and then thinks for days. Here (1.5–2.6 times slower
  than the reference) a(34) comes after about 13 s and a(43) after
  34 s; the bar is 35 terms (a(0) to a(34)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 109 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002184), CC BY-SA 4.0.
