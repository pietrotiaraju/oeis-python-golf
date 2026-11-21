# A002091

> From a Goldbach conjecture: the location of records in A185091.
> — [OEIS A002091](https://oeis.org/A002091)

Offset 1: 3, 9, 19, 21, 55, 115, 193, 323, 611, 1081, 1571, 10771, …

[A185091](https://oeis.org/A185091)(n) is the smallest positive
noncomposite q (1 or a prime) such that 2n − 1 = 2p + q for some positive
noncomposite p. This sequence lists the odd numbers N = 2n − 1 at which
A185091 sets a new record, and [A002092](../A002092/) the records.

### Python 3 — 156 bytes

```python
L=[1];T={2,4};m=1;r=0
while m:=m+2:
 if all(m%p for p in L[1:1<<m.bit_length()//2]):L+=m,;T|={2*m}
 if(q:=next((q for q in L if m-q in T),0))>r:r=q;print(m)
```

**How it works**

- `L` holds 1 and the odd primes up to m in increasing order, and `T` the
  numbers 2p for p = 1, 2 and the odd primes up to m. m runs over the odd
  numbers 3, 5, 7, … (`while m:=m+2:`).
- **Primality.** m is odd, and L[1:k] are the k − 1 smallest odd primes,
  all below m. With b the bit length of m and k = 2^⌊b/2⌋, the odd
  numbers from 3 to √m number at most k − 1 (√m < 2^(b/2)), so the
  slice holds every odd prime up to √m and `all(m%p for p in …)` is an
  exact primality test.
- **The smallest q.** For odd N = m, q is odd (N − q = 2p is even), so
  the first q in L with m − q in T is A185091 at N. q runs through L in
  increasing order and stops at the first hit, usually after a few steps.
- **Records.** `r` is the largest value so far; the program prints m
  when q beats it.

**Notes**

- Integer arithmetic only, so it is correct for every n.
- Every odd N ≥ 3 is expected to have such a representation (a form of
  Lemoine's conjecture, checked to about 10¹³ according to the entry),
  but the program does not need it: `next(…,0)` would give 0 for an N
  without one, which sets no record, so the program would skip that N
  and go on.
- The b-file has 49 terms, up to about 8.6·10¹²; the bar is 20 terms in
  60 s (N = 442307), about 3 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 156 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002091), CC BY-SA 4.0.
