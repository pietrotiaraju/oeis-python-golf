# A001726

> Weight distribution of [ 64,22,16 ] 2nd-order Reed-Muller code of length 64.
> — [OEIS A001726](https://oeis.org/A001726)

Offset 0: 1, 0, 0, 0, 2604, 0, 291648, 888832, 1828134, 888832, 291648, 0, 2604, 0, 0, 0, 1 (finite: 17 terms)

### Python 3 — 66 bytes

```python
l=1,0,0,0,2604,0,291648,888832
print(*l,1828134,*l[::-1],sep='\n')
```

**How it works**

The sequence is finite. RM(2, 6) is the binary code of length 64 whose
words are the value tables of the Boolean polynomials of degree at most 2
in six variables (spanned by the 22 monomials 1, x_i, x_i·x_j). Every
weight is a multiple of 4, and a(n) is the number of codewords of weight
4n, for n = 0, …, 16. The program prints the known distribution:

| weight | 0 | 16 | 24 | 28 | 32 | 36 | 40 | 48 | 64 |
|---|---|---|---|---|---|---|---|---|---|
| words | 1 | 2604 | 291648 | 888832 | 1828134 | 888832 | 291648 | 2604 | 1 |

and 0 at every other multiple of 4.

- These numbers are a theorem (Sloane and Berlekamp 1970, linked in the
  entry; MacWilliams and Sloane, *The Theory of Error-Correcting Codes*,
  ch. 15): in RM(2, m) a nonzero word other than the all-ones word has
  weight 2^(m−1) or 2^(m−1) ± 2^(m−1−h) with 1 ≤ h ≤ ⌊m/2⌋, and

  A(2^(m−1) ± 2^(m−1−h)) = 2^(h(h+1)) · ∏_{i=m−2h+1..m} (2^i − 1) / ∏_{i=1..h} (4^i − 1).

  For m = 6, h = 1, 2, 3 give 4·63·31/3 = 2604 at weights 16 and 48,
  64·63·31·15·7/45 = 291648 at 24 and 40, and 4096·7·31 = 888832 at 28
  and 36. The 2^22 words add up, so weight 32 has
  2^22 − 2 − 2·(2604 + 291648 + 888832) = 1828134.
- The list is symmetric because the all-ones word is in the code: adding
  it maps weight w to 64 − w. So the program stores the first eight
  values, prints the middle one, and prints the eight again reversed.
- As a check outside the program, a Gray-code walk over all 2^22
  combinations of the 22 monomial vectors (one XOR and one `bit_count`
  per word) finds exactly these counts.
- It spells out its terms, so it needs a review.

**Notes**

- It prints the 17 terms (the whole b-file) and stops.
- The dual code RM(3, 6) has the distribution
  [A001727](https://oeis.org/A001727), which follows from this one by the
  MacWilliams identity.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001726), CC BY-SA 4.0.
