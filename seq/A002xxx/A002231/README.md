# A002231

> Primitive roots that go with the primes in A029932.
> — [OEIS A002231](https://oeis.org/A002231)

Offset 1: 2, 3, 5, 7, 11, 19, 43, 53, 79, 107, 149, 151, …

### Python 3 — 136 bytes

```python
P=r=1;k=2
while 1:
 g=1
 while P%k*(0in(g%j for j in range(2,g))or sum(g**e%k<2for e in range(k))>2):g+=1
 g>r==print(r:=g)
 P*=k*k;k+=1
```

**How it works**

- **What is listed.** A029932 lists the primes p at which the least
  *prime* primitive root sets a record (3, 7, 23, 41, 109, 191, 271, …), and
  this entry the roots that go with them, the record values. As in
  A029932, p = 2 is left out (its only primitive root is 1, which is not
  prime): `r` starts at 1, so the g = 1 that k = 2 finds is no record.
- **Primes.** `k` runs over 2, 3, 4, … with `P` = ((k − 1)!)², so by
  Wilson's theorem `P%k` is 1 when k is prime and 0 otherwise.
- **Primitive roots by counting.** Modulo a prime k, g^e ≡ 1 holds
  exactly at the multiples of the order of g, so among e = 0, 1, …, k − 1
  it holds at e = 0 and e = k − 1 only when g has order k − 1, and at
  least three times otherwise. So g is a primitive root exactly when
  `sum(g**e%k<2for e in range(k))` is at most 2.
- **Least prime root.** For a prime k, `g` goes 1, 2, 3, … and skips the
  composite g (`0in(g%j for j in range(2,g))`); g = 1 is never a
  primitive root of k ≥ 3 (its count is k), so from k = 3 on the root found is a prime. The search has no cap: no
  theorem keeps the least prime primitive root below k, and the counting
  test works for any g (a multiple of k counts k zeros and fails). It
  ends because some prime is a primitive root (Dirichlet's theorem gives
  primes in the class of any primitive root). For a composite k `P%k` is
  0, the product `P%k*(…)` is 0 at once (the test of g = 1 is still computed), and `g` stays 1,
  never a record.
- **Records.** `r` is the largest least root so far. `g>r==print(r:=g)` is
  a chained comparison: when g > r it goes on to `r==print(r:=g)`, which
  prints g and stores it in `r` (the `r` on its left was read before, and
  comparing it with `None` is false and ignored); otherwise it stops
  before printing.

**Notes**

- Exact integers; Wilson's theorem and Dirichlet's theorem (for termination) make it right for every n.
- Each candidate g costs k powers g^e, computed as growing big integers, so the search is slow: here (1.5–2.6 times slower than the reference) a(8) = 53 (the root of the prime 2791) comes after 6–8 s, while a(9) = 79 (11971) takes more than a minute. The bar is 8 terms in 60 s; they fit in a table shorter than the program, so it went through a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 136 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002231), CC BY-SA 4.0.
