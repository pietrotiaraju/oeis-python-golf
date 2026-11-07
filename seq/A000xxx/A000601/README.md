# A000601

> Expansion of 1/((1-x)^2*(1-x^2)*(1-x^3)).
> — [OEIS A000601](https://oeis.org/A000601)

Offset 0: 1, 2, 4, 7, 11, 16, 23, 31, 41, 53, 67, 83, 102, 123, 147, …

### Python 3 — 42 bytes

```python
m=7
while[print((m**3-15*m+50)//288)]:m+=2
```

**How it works**

- The generating function 1/((1−x)²(1−x²)(1−x³)) has the partial-fraction
  expansion a(n) = n³/36 + 7n²/24 + 11n/12 + 119/144 + (−1)ⁿ/16 + χ(n)/9,
  with χ(n) = 1, 0, −1 for n ≡ 0, 1, 2 (mod 3) (R. J. Mathar's formula in the
  OEIS entry). The periodic part lies between 94/144 and 1, so
  a(n) = ⌊(2n³ + 21n² + 66n)/72⌋ + 1 (M. Somos's formula) for every n.
- Put m = 2n + 7, the odd numbers 7, 9, 11, …: then
  4(2n³ + 21n² + 66n + 72) = m³ − 15m + 50, and multiplying numerator and
  denominator of the floor by 4 gives a(n) = ⌊(m³ − 15m + 50)/288⌋. The
  quadratic term disappears, which is what makes this form short.
- The loop prints that value and steps m by 2.

**Notes**

- Exact integer arithmetic; the closed form holds for every n by the
  partial-fraction argument above. Any constant from 50 to 237 in place of 50
  gives the same floors (the residue of the numerator mod 288 depends only on
  m mod 288, and the b-file covers all residues); 50 is the one that makes the
  formula an identity.
- Shorter than summing [A001399](https://oeis.org/A001399)
  (`s:=s+n*(n+6)//12+1`, 43 bytes) or the order-7 linear recurrence.
- Constant time per term: the whole b-file (10001 terms) prints in well under a
  second, and the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000601), CC BY-SA 4.0.
