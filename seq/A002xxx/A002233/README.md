# A002233

> a(1) = 1; for n > 1, a(n) = least positive prime primitive root of n-th prime.
> — [OEIS A002233](https://oeis.org/A002233)

Offset 1: 1, 2, 2, 3, 2, 2, 3, 2, 5, 2, 3, 2, 7, 3, 5, 2, 2, 2, 2, 7, 5, 3, 2, 3, …

### Python 3 — 130 bytes

```python
P=k=g=1
while 1:
 if P%k:
  while 0in(g%j for j in range(2,g))or sum(g**e%k<2for e in range(k))>2:g+=1
  print(g);g=1
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
  `sum(g**e%k<2for e in range(k))` is at most 2. A multiple of k gives 1 at e = 0 and 0 after it, so it counts k and fails too.
- **Least prime root.** For a prime k, `g` goes 1, 2, 3, … and skips the
  composite g (`0in(g%j for j in range(2,g))` is true when g has a divisor
  in 2, …, g − 1). For k = 2 the group is trivial and g = 1 passes (e = 0
  and e = 1): that is the convention a(1) = 1. For k ≥ 3, g = 1 counts k
  ones and fails, so the printed g is a prime.
- **No cap.** No theorem keeps the least prime primitive root below k, so
  `g` is not bounded by k; the loop ends because some prime is a
  primitive root (Dirichlet's theorem gives primes in the class of any
  primitive root). Then the program prints g and resets it to 1.

**Notes**

- Exact integers; Wilson's theorem and Dirichlet's theorem (for termination) make it right for every n.
- Each candidate g costs k powers g^e, computed as growing big integers; `pow(g,e,k)` is 4 bytes longer and about twice as fast, and testing g^((k−1)/d) only for the divisors d of k − 1 is faster still but longer. Here (1.5–2.6 times slower than the reference) 500 terms (p = 3571) come after 11 s, 600 after 19 s, 700 after 36 s and 800 after 62 s. The b-file has 10000 terms; the bar is 600 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 130 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002233), CC BY-SA 4.0.
