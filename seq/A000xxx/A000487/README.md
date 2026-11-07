# A000487

> Number of permutations of length n with exactly two valleys.
> — [OEIS A000487](https://oeis.org/A000487)

Offset 5: 16, 272, 2880, 24576, 185856, 1304832, 8728576, 56520704, 357888000, 2230947840, …

A valley of a permutation p is an interior position i with p(i−1) > p(i) <
p(i+1); two valleys first fit at length 5.

### Python 3 — 51 bytes

```python
m=4
while[print(3*3**m+2*m*(m-(2<<m))-3<<m-4)]:m+=1
```

**How it works**

- The g.f. is 16x⁵(1 − 3x)/((1 − 2x)³(1 − 4x)²(1 − 6x)) (Ralf Stephan 2003,
  proved by Désiré André in 1895 per the OEIS entry). Its poles 1/6, 1/4 and
  1/2 have orders 1, 2 and 3, so partial fractions give 6ⁿ, 4ⁿ times a linear
  and 2ⁿ times a quadratic polynomial; the result is Mitchell Harris's
  a(n) = (6ⁿ + (2 − 2n)·4ⁿ + (2n² − 4n − 1)·2ⁿ)/32.
- With m = n − 1 the polynomials become −2m and 2m² − 3, and taking out
  2ⁿ = 2^(m+1) leaves
  a(n) = 2^(m−4)·(3^(m+1) − 3 + 2m(m − 2^(m+1))).
  The program prints exactly this: `3*3**m` is 3^(m+1) and `2<<m` is 2^(m+1).
- `X<<m-4` multiplies by 2^(m−4) instead of dividing by 32, and since m ≥ 4
  the shift count is never negative. `<<` binds looser than `+` and `-`, so
  neither side needs parentheses.
- The loop is the `while[print(…)]:` form: `[None]` is a non-empty list, so
  the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Same length: `3*~-3**m+2*m*m-(m<<m+2)<<m-4` (51 bytes; `~-3**m` is
  3^m − 1). Harris's formula as it stands,
  `while[print((6**n+(2-2*n)*4**n+(2*n*n-4*n-1)*2**n)//32)]:n+=1`, is
  65 bytes.
- Exact integer arithmetic with no division at all, so the program is right
  for every n. A brute-force count over all permutations agrees for n = 5..9.
- The b-file has 196 terms (up to a(200)); the bar is the whole b-file in
  60 s. All of it prints in 0.1 s here.
- a(5528) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there, after about 1.4 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 66 | first entry |
| 2026-11-07 | Python 3 | 51 | m = n − 1, factor 2^(m−4) out as a shift |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000487), CC BY-SA 4.0.
