# A002143

> Class numbers h(-p) where p runs through the primes p == 3 (mod 4).
> — [OEIS A002143](https://oeis.org/A002143)

Offset 1: 1, 1, 1, 1, 3, 3, 1, 5, 3, 1, 7, 5, 3, 5, 3, 5, 5, 3, 7, 1, 11, 5, 13, …

### Python 3 — 137 bytes

```python
P=k=1
while 1:
 if-P%k*k%4>2:
  a=h=0
  while 3*a*a<k:a+=1;h+=sum((x:=b*b+k>>2)%a<1>a*a-x for b in range(-a|1,a,2))
  print(h)
 P*=k;k+=1
```

**How it works**

- **Which sequence.** a(n) = h(−p) for p = [A002145](../A002145/)(n), the
  n-th prime p ≡ 3 (mod 4): the class number of Q(√−p), which is the
  number of reduced forms of discriminant −p.
- **Primes ≡ 3 (mod 4).** `k` runs over 1, 2, 3, … with `P` = (k − 1)!.
  By Wilson's theorem −P mod k is 1 when k is prime; it is 0 when k > 4
  is composite (k | (k − 1)!), and for k = 1 and k = 4 (−6 mod 4 = 2)
  the product with k is still ≡ 0 (mod 4). So `-P%k*k%4>2` holds exactly
  for the primes k ≡ 3 (mod 4).
- **Class number.** Reduced forms ax² + bxy + cy² of discriminant
  b² − 4ac = −k have |b| ≤ a ≤ c, and b ≥ 0 when |b| = a or a = c. For a
  prime k ≡ 3 (mod 4), k > 3, every such form is primitive (a common
  factor g has g² | k), b is odd, a = c is impossible
  (k = (2a − b)(2a + b) would force |b| = (k − 1)/2 > a) and |b| = a
  forces a | k, so a = 1. Hence h(−k) counts the pairs (a, b), b odd in
  [−a, a), with a | x and a² ≤ x for x = (b² + k)/4 = ac: for a ≥ 2 the
  admissible b are symmetric and miss ±a, and at a = 1 the range takes
  b = −1 in place of b = 1. a ≤ c gives 4a² ≤ b² + k ≤ a² + k, so
  a runs while 3a² < k. `-a|1` is the first odd number ≥ −a, and
  `b*b+k>>2` is x exactly, as b² + k ≡ 0 (mod 4). For k = 3 the only
  pair is (1, −1), and h(−3) = 1 (the form x² + xy + y²).

**Notes**

- The same counter as [A001985](../A001985/)–[A001989](../A001989/);
  here the primes come from Wilson's theorem, with the unsquared
  factorial, because every prime is wanted.
- Exact integer arithmetic throughout. Counting the forms takes about
  p/6 steps for each prime, and the factorial grows to over a million
  bits by the bar: a(4000), p = 81547, comes after about 16 reference
  seconds, and about 7500 terms come in 60. The bar is 4000 terms in
  60 s; the b-file has 10000.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-21 | Python 3 | 137 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002143), CC BY-SA 4.0.
