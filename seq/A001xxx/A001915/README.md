# A001915

> Primes p such that the congruence 2^x == 3 (mod p) is solvable.
> — [OEIS A001915](https://oeis.org/A001915)

Offset 1: 2, 5, 11, 13, 19, 23, 29, 37, 47, 53, 59, 61, 67, 71, 83, 97, 101, 107, …

### Python 3 — 70 bytes

```python
P=k=1
while[3%k in{2**e%k for e in range(-P%k*k)}==print(k)]:P*=k;k+=1
```

**How it works**

- 2^x ≡ 3 (mod p) is solvable when 3 mod p is among the powers 2⁰, 2¹,
  2², … mod p. For a prime p these repeat with a period dividing p − 1, so
  the exponents x = 0, …, p − 1 give them all, and the program tests
  `3%k in{2**e%k for e in range(k)}`.
- The small primes follow the data: x = 0 counts, so p = 2 is a term
  (3 ≡ 1 = 2⁰); p = 3 is not (3 ≡ 0 is never a power of 2); p = 5 is
  (2³ = 8 ≡ 3).
- Composites are dropped with Wilson's theorem: P = (k − 1)!, and
  `-P%k` is 1 when k is prime and 0 when k is composite and k > 4, so the
  range is 0..k − 1 for primes and empty otherwise (an empty set never
  holds 3%k). For k = 4, `-P%k` is 2 and the set is {1, 2, 0}, which does
  not hold 3. For k = 1 the range is empty as well.
- In `3%k in S==print(k)` the chained comparison calls `print` only when
  3%k is in S; the list `[False]` keeps the loop going.

**Notes**

- Wilson's theorem and exact integers: right for every n. Pólya showed
  that the sequence is infinite.
- `pow(2,e,k)` instead of `2**e%k` is 3 bytes longer and reaches about
  twice as many terms in the same time. [A001916](../A001916/) is the same
  test with 5, one byte longer.
- Every prime p costs p powers: about 596 terms (p = 8269) in 24 s here.
  The b-file has 10000 terms; the bar is 560 terms (a(560) = 7717) in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001915), CC BY-SA 4.0.
