# A000517

> Number of permutations of length n with exactly three valleys.
> — [OEIS A000517](https://oeis.org/A000517)

Offset 7: 272, 7936, 137216, 1841152, 21253376, 222398464, 2174832640, 20261765120, 182172651520, 1594922762240, …

### Python 3 — 71 bytes

```python
m=5
while[print(8*4**m-m*(3**m*27+2*m*m-11)//3+(m*m-2<<m+2)<<m-4)]:m+=1
```

**How it works**

- The OEIS generating function
  16x⁷(17 − 184x + 636x² − 720x³)/((1−2x)⁴(1−4x)³(1−6x)²(1−8x))
  (Stephan 2003; proved by D. André, 1895, for circular permutations, see
  A008303) splits into partial fractions. With m = n − 2 they give, for
  n ≥ 7,

  128·a(n) = 8^n − 2m·6^n + 2(m² − 2)·4^n − (2/3)·m(2m² − 11)·2^n.

  Both sides satisfy the order-10 recurrence with that denominator once
  n ≥ 17 (the numerator has degree 10), and they agree on a(7), …, a(16),
  so they agree for every n ≥ 7; the b-file confirms the formula up to
  a(200).
- Taking out the common factor 2^(m+3) = 2^(n+1) of the right side gives
  a(n) = 2^(m−4)·[8·4^m − m(27·3^m + 2m² − 11)/3 + 4(m² − 2)·2^m],
  which is the program with `m` running from 5 (n = 7).
- The `//3` is exact: m(2m² − 11) is divisible by 3 (for m ≢ 0 mod 3,
  2m² − 11 ≡ 2 − 11 ≡ 0), and so is 27m·3^m. The shift `<<m-4` is an exact
  multiplication since m ≥ 5.
- `+`/`-` bind tighter than `<<`, so `…<<m-4` shifts the whole bracket,
  and `(m*m-2<<m+2)` is 4(m² − 2)·2^m in 2 bytes less than
  `(m*m-2)*2**m*4`. Folding 9m·3^m and m(2m² − 11)/3 into one quotient
  saves another byte.

**Notes**

- The same partial fractions in n with `<<n-7`: 92 bytes; dividing the
  four contributions by 128 at the end, as written in n: 100 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints at once. The program stops after a(4763):
  a(n) is about 8^n/128, and a(4764) is the first term with more than 4300
  digits, the int-to-str limit of Python 3.11+.
- The b-file has 194 terms (up to a(200)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 100 | first entry |
| 2026-11-07 | Python 3 | 71 | m = n − 2, common factor 2^(m−4) as a shift |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000517), CC BY-SA 4.0.
