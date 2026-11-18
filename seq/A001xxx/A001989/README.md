# A001989

> Class numbers associated with terms of A001988.
> — [OEIS A001989](https://oeis.org/A001989)

Offset 1: 1, 1, 5, 7, 7, 7, 9, 53, 73, 83, 83, 83, …

### Python 3 — 230 bytes

```python
r=7;P=4;q=3;Q=[]
while 1:
 if P%q:
  Q+=q,;a=h=0
  while any(pow(-r,d//2,d)<2for d in Q)or 0in(r%d for d in range(2,r//q)):r+=24
  while 3*a*a<r:a+=1;h+=sum((x:=b*b+r>>2)%a<1>a*a-x for b in range(-a|1,a,2))
  print(h)
 P*=q*q;q+=1
```

**How it works**

- **Terms of [A001988](../A001988/).** Apart from `;a=h=0` and the two
  lines that count and print h, this is that page's program: it finds
  p = A001988(n) in `r` (Wilson's theorem for the odd primes q,
  Euler's criterion for Legendre(−r, d) = −1, steps of 24 from 7,
  trial division up to r/q; that page has the details).
- **Class number.** h(−r) is the number of reduced forms ax² + bxy + cy²
  of discriminant b² − 4ac = −r: |b| ≤ a ≤ c, and b ≥ 0 when |b| = a or
  a = c. For a prime r ≡ 3 (mod 4), r > 3, every such form is primitive
  (a common factor g has g² | r), b is odd, a = c is impossible
  (r = (2a − b)(2a + b) would force |b| = (r − 1)/2 > a) and |b| = a
  forces a | r, so a = 1. Hence h(−r) counts the pairs (a, b), b odd in
  [−a, a), with a | x and a² ≤ x for x = (b² + r)/4 = ac: for a ≥ 2 the
  admissible b are symmetric and miss ±a, and at a = 1 the range takes
  b = −1 in place of b = 1. a ≤ c gives 4a² ≤ b² + r ≤ a² + r, so
  a runs while 3a² < r. `-a|1` is the first odd number ≥ −a, and
  `b*b+r>>2` is x exactly, as b² + r ≡ 0 (mod 4).

**Notes**

- **Which class number.** a(n) = h(−p) for p = [A001988](../A001988/)(n),
  the class number of Q(√−p): the number of reduced forms of discriminant
  −p. The PARI program in the entry computes h(−4p) (primitive forms),
  which is the same number here: for p ≡ 7 (mod 8), −p ≡ 1 (mod 8), so 2
  splits and h(−4p) = h(−p)·(2 − 1) = h(−p) (p > 3).
- **Which search.** [A001988](../A001988/)'s title has a sign slip; its
  data, which these class numbers follow, is the least prime r ≡ 7
  (mod 8) with Legendre(−r, q) = −1 for the first n odd primes q (see that
  page). The title as written would give r = 23, h = 3 for n = 1.
- Exact integer arithmetic throughout. Counting the forms takes about r/6
  steps per term: here (about 1.4 times slower than the reference) a(17),
  the bar, comes after 0.3 s, a(18) after 10 s and a(20) after 25 s.
  The bar is 17 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 230 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001989), CC BY-SA 4.0.
