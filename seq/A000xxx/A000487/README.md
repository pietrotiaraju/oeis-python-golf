# A000487

> Number of permutations of length n with exactly two valleys.
> — [OEIS A000487](https://oeis.org/A000487)

Offset 5: 16, 272, 2880, 24576, 185856, 1304832, 8728576, 56520704, 357888000, 2230947840, …

### Python 3 — 66 bytes

```python
n=5
while 1:print((6**n+(2-2*n)*4**n+(2*n*n-4*n-1)*2**n)//32);n+=1
```

**How it works**

- A valley is an interior position i with p_(i−1)>p_i<p_(i+1).
  Two valleys first fit in a permutation of length 5, explaining
  the output offset and the alternating first case a(5)=16.
- The ordinary generating function is
  16x⁵(1−3x)/((1−2x)³(1−4x)²(1−6x)).
  Its partial fractions give the closed form listed by the OEIS:

  **a(n)=(6ⁿ+(2−2n)4ⁿ+(2n²−4n−1)2ⁿ)/32.**

- Poles of orders 1, 2 and 3 produce an exponential times a
  polynomial of degrees 0, 1 and 2 respectively, accounting for
  the three pieces in that expression.
- The loop evaluates the full numerator at n≥5 before dividing.
  At n=5 it is 7776−8192+928=512, so the first print is 16.

**Notes**

- Exact integer powers and cancellation, with an exact division by
  32 for every output index. The expression needs no enumeration
  of permutations or numerical evaluation of the generating function.
- The direct formula keeps only a counter and integer temporaries.
  A denominator-based linear recurrence would instead retain six
  preceding coefficients because its denominator has degree six.
- Exponential growth eventually reaches Python 3.11+'s default
  4300-digit integer-to-string limit, an interpreter limit rather
  than a failure of the coefficient formula.
- The b-file has 196 terms (indices 5 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000487), CC BY-SA 4.0.
