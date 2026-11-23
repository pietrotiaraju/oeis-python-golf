# A002229

> Primitive roots that go with the primes in A002230.
> — [OEIS A002229](https://oeis.org/A002229)

Offset 1: 1, 2, 3, 5, 6, 7, 19, 21, 23, 31, 37, 38, …

### Python 3 — 105 bytes

```python
P=1;k=2;r=0
while 1:
 g=1
 while P%k*sum(g**e%k<2for e in range(k))>2:g+=1
 g>r==print(r:=g)
 P*=k*k;k+=1
```

**How it works**

- **Primes.** `k` runs over 2, 3, 4, … with `P` = ((k − 1)!)², so by
  Wilson's theorem `P%k` is 1 when k is prime and 0 otherwise (k = 4
  included: 36 ≡ 0).
- **Primitive roots by counting.** Modulo a prime k, g^e ≡ 1 holds
  exactly at the multiples of the order of g, so among e = 0, 1, …, k − 1
  it holds at e = 0 and e = k − 1 only when g has order k − 1, and at
  least three times otherwise. So g is a primitive root exactly when
  `sum(g**e%k<2for e in range(k))` is at most 2. For 1 ≤ g < k the power is never 0, so `<2` means `==1`.
- **Least root.** For a prime k, `g` goes 1, 2, … until it is a primitive
  root; every prime has one in 1, …, k − 1, so the loop ends below k. For
  k = 2 the group is trivial and g = 1 passes (e = 0 and e = 1), the
  entry's convention a(1) = 1 (least root 1 of the prime 2). For a composite k
  `P%k` is 0, so `P%k*sum(…)>2` is false at once (the sum for g = 1 is still computed) and `g`
  stays 1, which is never a record after k = 2.
- **Records.** `r` is the largest least root so far. `g>r==print(r:=g)` is
  a chained comparison: when g > r it goes on to `r==print(r:=g)`, which
  prints g and stores it in `r` (the `r` on its left was read before, and
  comparing it with `None` is false and ignored); otherwise it stops
  before printing.
- The terms are the records of the least positive primitive root
  (A001918) over the primes, and the entry pairs the roots with the primes of A002230: this
  program prints the root g of each record, as the Python program in the entry does with
  sympy.

**Notes**

- Exact integers and Wilson's theorem: right for every n.
- Each candidate g costs k powers g^e, computed as growing big integers, so the search is slow: here (1.5–2.6 times slower than the reference) a(9) = 23 (least root of the prime 2161) comes after 4 s, while a(10) = 31 (5881) takes more than a minute. The bar is 9 terms in 60 s; they fit in a table shorter than the program, so it went through a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 105 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002229), CC BY-SA 4.0.
