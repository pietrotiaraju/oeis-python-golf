# A002146

> Smallest prime == 7 (mod 8) where Q(sqrt(-p)) has class number 2n+1.
> — [OEIS A002146](https://oeis.org/A002146)

Offset 0: 7, 23, 47, 71, 199, 167, 191, 239, 383, 311, 431, 647, 479, 983, 887, 719, …

### Python 3 — 172 bytes

```python
P=k=n=1;d={}
while 1:
 a=h=0;c=-P%k*k%8>6
 while 3*a*a<k*c:a+=1;h+=sum((x:=b*b+k>>2)%a<1>a*a-x for b in range(-a|1,a,2))
 d={h:k}|d;P*=k;k+=1
 while n in d:print(d[n]);n+=2
```

**How it works**

- **One sweep.** `k` runs over 1, 2, 3, … with `P` = (k − 1)!. By
  Wilson's theorem −P mod k is 1 for a prime k and 0 for a composite
  k > 4 (also 0·k or 2·4 ≡ 0 (mod 8) at k = 1 and 4), so `c` is 1
  exactly for the primes k ≡ 7 (mod 8), in increasing order.
- **Class number.** For those k the loop counts the reduced forms of
  discriminant −k, which is h(−k), the class number of Q(√−k): for a
  prime k ≡ 3 (mod 4), k > 3, every reduced form ax² + bxy + cy²
  (|b| ≤ a ≤ c, b ≥ 0 when |b| = a or a = c) is primitive, b is odd,
  a = c is impossible and |b| = a forces a = 1, so h(−k) is the number of
  pairs (a, b), b odd in [−a, a), with a | x and a² ≤ x for
  x = (b² + k)/4 = ac (the argument is spelled out on
  [A002143](../A002143/)); a ≤ c gives 3a² < k. For every other k the
  loop does not run and h = 0.
- **First occurrence.** `d={h:k}|d` keeps the old value when the key is
  already there, so `d[h]` is the first, that is the smallest, prime with
  class number h. h(−p) is odd for these primes (genus theory: −p has one
  prime factor), so only odd keys besides 0 appear, and `n` steps over
  1, 3, 5, …: as soon as class number 2n + 1 has been seen, a(n) is
  printed, followed by every later term that is already known. Terms
  come in order, and each one is final when printed, since all smaller
  primes have been counted.

**Notes**

- If some odd number were never a class number of such a prime, the
  program would wait at it for ever, as the term would not exist; the
  b-file has 28604 terms.
- Exact integer arithmetic throughout. The sweep has to reach the largest
  of the first n terms (40039 for 100 terms, 83903 for 136 to 184,
  105167 for 200): the 184th term comes after about 13 reference
  seconds, and about 240 terms come in 60. The bar is 184 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-21 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002146), CC BY-SA 4.0.
