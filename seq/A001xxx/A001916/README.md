# A001916

> Primes p such that the congruence 2^x = 5 (mod p) is solvable.
> — [OEIS A001916](https://oeis.org/A001916)

Offset 1: 2, 3, 11, 13, 19, 29, 37, 41, 53, 59, 61, 67, 71, 79, 83, 101, 107, …

### Python 3 — 71 bytes

```python
P=k=1
while[5%k in{2**e%k for e in range(P%k*k)}==print(k)]:P*=k*k;k+=1
```

**How it works**

- 2^x ≡ 5 (mod p) is solvable when 5 mod p is among the powers 2⁰, 2¹,
  2², … mod p. For a prime p these repeat with a period dividing p − 1, so
  the exponents x = 0, …, p − 1 give them all, and the program tests
  `5%k in{2**e%k for e in range(k)}`.
- The small primes follow the data: x = 0 counts, so p = 2 is a term
  (5 ≡ 1 = 2⁰); so is p = 3 (5 ≡ 2 = 2¹); p = 5 is not (5 ≡ 0 is never a
  power of 2).
- Composites are dropped with Wilson's theorem, squared:
  P = ((k − 1)!)², so `P%k` is 1 when k is prime and 0 when k is composite
  or 1, and the range is 0..k − 1 for primes and empty otherwise (an empty
  set never holds 5%k). The square matters for k = 4: (k − 1)! = 6 is not
  0 mod 4, and mod 4 the powers of 2 are {1, 2, 0}, which hold 5 ≡ 1;
  36 is 0 mod 4.
- In `5%k in S==print(k)` the chained comparison calls `print` only when
  5%k is in S; the list `[False]` keeps the loop going.

**Notes**

- Wilson's theorem and exact integers: right for every n.
- The same program with 3 and P = (k − 1)! is
  [A001915](../A001915/), one byte shorter; with 5 the unsquared
  factorial would print 4.
- `pow(2,e,k)` instead of `2**e%k` is 3 bytes longer and reaches about
  twice as many terms in the same time.
- Every prime p costs p powers: about 594 terms (p = 8219) in 24 s here.
  The b-file has 1000 terms; the bar is 560 terms (a(560) = 7669) in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001916), CC BY-SA 4.0.
