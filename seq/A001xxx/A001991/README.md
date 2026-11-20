# A001991

> Class numbers associated with terms of A001990.
> — [OEIS A001991](https://oeis.org/A001991)

Offset 1: 2, 2, 2, 2, 2, 2, 2, 2, 46, 46, 46, 46, …

### Python 3 — 235 bytes

```python
r=5;P=4;q=3;Q=[]
while 1:
 if P%q:
  Q+=q,;a=h=0
  while any(pow(-2*r,d//2,d)<2for d in Q)or 0in(r%d for d in range(2,r//q)):r+=24
  while a*a<3*r:a+=1;h+=sum((x:=b*b+8*r>>2)%a<1>a*a-x for b in range(a%2-a,a,2))
  print(h)
 P*=q*q;q+=1
```

**How it works**

- **Terms of [A001990](../A001990/).** Apart from `;a=h=0` and the two
  lines that count and print h, this is that page's program: it finds
  p = A001990(n) in `r` (Wilson's theorem for the odd primes q,
  Euler's criterion for Legendre(−2r, d) = −1, steps of 24 from 5,
  trial division up to r/q; that page has the details).
- **Class number.** h(−8r) is the number of reduced forms ax² + bxy + cy²
  of discriminant b² − 4ac = −8r: |b| ≤ a ≤ c, and b ≥ 0 when |b| = a or
  a = c. For a prime r ≡ 5 (mod 8) every such form is primitive (a common
  factor g has g² | 8r, and g = 2 would leave the discriminant −2r ≡ 2
  (mod 4)), b is even, and neither boundary case occurs: with b = 2t,
  a = c gives (a − t)(a + t) = 2r, a product of two numbers of equal
  parity that is ≡ 2 (mod 4); |b| = a gives a = 2u, u² + 2r = 2uc, so
  u = 2v and 2v² + r = 2vc with r odd. Hence h(−8r) counts the pairs
  (a, b), b even in [−a, a), with a | x and a² ≤ x for
  x = (b² + 8r)/4 = ac. a ≤ c gives 3a² ≤ 8r, so running a while
  a² < 3r covers it. `range(a%2-a,a,2)` starts at −a or 1 − a, whichever
  is even.

**Notes**

- **Which class number.** a(n) = h(−8p) for p = [A001990](../A001990/)(n),
  as in the entry's formula: the number of reduced forms of discriminant
  −8p, the class number of Q(√−2p).
- **Which search.** [A001990](../A001990/)'s title has a sign slip; its
  data, which these class numbers follow, is the least prime r ≡ 5
  (mod 8) with Legendre(−2r, q) = −1 for the first n odd primes q (see
  that page).
- Exact integer arithmetic throughout. With |D| = 8r the form count takes
  about 3r/2 steps per term, more than the search: here (about 1.7 times
  slower than the reference) a(17), the bar, comes after 12 s and a(21)
  after 71 s. The bar is 17 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 235 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001991), CC BY-SA 4.0.
