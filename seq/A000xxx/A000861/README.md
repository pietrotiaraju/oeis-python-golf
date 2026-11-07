# A000861

> Numbers ending with a vowel in American English.
> — [OEIS A000861](https://oeis.org/A000861)

Offset 1: 0, 1, 2, 3, 5, 9, 12, 21, 22, 23, 25, 29, 31, 32, 33, 35, 39, 41, 42, 43, 45, 49, 51, …

### Python 3 — 63 bytes

```python
n=0
while 1:[559,4][n//10%10==1]>>(n%10or n)&1and print(n);n+=1
```

**Which names**

- The last word of the name of n > 0 is fixed by m = n mod 100. When m ≠ 0
  it is the name of m: one … nine (alone or after twenty … ninety), ten,
  eleven … nineteen, or a tens word twenty … ninety. When m = 0 it is
  hundred, thousand or a scale word ending in -illion, and all of those end
  in a consonant, whatever the large scales are called. The vowel endings
  are one, two, three, five, nine and twelve, plus zero for n = 0; y is not
  a vowel here (20 is not in the data). British English adds "and" in the
  middle but has the same last word.
- So n is a term when n = 0, when n mod 100 = 12, or when the units digit
  is 1, 2, 3, 5 or 9 and the tens digit is not 1. That is the PARI program
  of the OEIS entry, and the reason for its recurrence a(n) = a(n−46) + 100:
  46 terms in every hundred.

**How it works**

- 559 = 2⁰ + 2¹ + 2² + 2³ + 2⁵ + 2⁹ is a bit mask of the units digits 1, 2,
  3, 5, 9, plus bit 0 for zero; 4 = 2² is the mask for the teens, where only
  twelve qualifies. `n//10%10==1` (tens digit 1) picks the mask, and
  `>>…&1` reads the bit of the units digit.
- The shift is `n%10or n`: the units digit, or n itself when that digit is
  0. For n = 0 that reads bit 0 of 559 (zero); for n = 10, 20, 100, … the
  shift is at least 10, past both masks, so the bit is 0.
- `…&1and print(n)` prints only the terms.

**Notes**

- A single 100-bit mask for n mod 100, `0x8ba2e8ba2e8ba2e8ba2e0122f>>(n%100or n)&1`,
  makes the program 71 bytes; masks for n mod 100 mod K or n mod K₁ mod K₂
  (searched up to K₁ = 400) are no shorter.
- Handling zero with `print(0)` first, or with `or n<1`, costs 2 or 3 bytes
  more than `or n` in the shift.
- About 4.5 million terms in 60 s here (up to 9.8 million).
- The b-file has 1000 terms (up to a(1000) = 2172); the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000861), CC BY-SA 4.0.
