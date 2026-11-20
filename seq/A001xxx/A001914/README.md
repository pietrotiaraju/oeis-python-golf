# A001914

> Cyclic numbers: 10 is a quadratic residue modulo p and class of mantissa is 2.
> — [OEIS A001914](https://oeis.org/A001914)

Offset 1: 2, 13, 31, 43, 67, 71, 83, 89, 107, 151, 157, 163, 191, 197, 199, 227, …

### Python 3 — 74 bytes

```python
P=k=1
while[3==sum(10**e%k<2for e in range(-P%k*k+1))==print(k)]:P*=k;k+=1
```

**Definition used**

As the OEIS comment puts it, apart from the first term 2 these are the
primes p for which the repunit R((p−1)/2) = (10^((p−1)/2) − 1)/9 is the
smallest repunit divisible by p. For p ≠ 3 that means ord_p(10) =
(p − 1)/2: 10 is a quadratic residue, and the fractions m/p have two
different cycles of digits (one cycle is class 1, the full reptend primes
[A001913](../A001913/)). The prime 3 is not a term: ord_3(10) = 1, but 3
divides R(3), not R(1). The data start with 2, and the program reproduces
that too, as explained below.

**How it works**

- For each k, the `sum` counts the exponents e = 0, 1, …, k with
  10^e mod k equal to 0 or 1 (`10**e%k<2`); call the count c. k is
  printed when c = 3.
- For a prime p other than 2 and 5, 10^e ≡ 1 exactly at the multiples of
  d = ord_p(10), so c = 1 + ⌊p/d⌋. With d = p − 1 that is 2; with
  d = (p − 1)/2 it is 3 once p > 3; with d ≤ (p − 1)/3 it is at least 4.
  So c = 3 picks out ord_p(10) = (p − 1)/2 for p ≥ 7. For p = 3, 10 ≡ 1
  and c = 4; for p = 5, 10^e ≡ 0 from e = 1 on and c = 6; neither is
  printed, as in the data. For p = 2 the values are 1, 0, 0, so c = 3 and
  2 is printed: the count gives a(1) = 2 without a special case.
- Composites are dropped with Wilson's theorem: P = (k − 1)!, and
  `-P%k` is 1 when k is prime, 0 when k is composite and k > 4, and 2 for
  k = 4. So the range is e = 0..k for primes; for composites (and k = 1)
  it is e = 0 alone and c = 1, and for k = 4 it is e = 0..8 with
  c = 8.
- `3==sum(…)==print(k)` calls `print` only when c = 3; `[False]` keeps
  the loop going.

**Notes**

- Wilson's theorem and exact integers: right for every n.
- `pow(10,e,k)` instead of `10**e%k` is 4 bytes longer and reaches about
  three times as many terms in the same time.
- Every prime p costs p + 1 powers: about 190 terms (p = 4799) in 24 s
  here. The b-file has 1180 terms; the bar is 180 terms (a(180) = 4597) in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001914), CC BY-SA 4.0.
