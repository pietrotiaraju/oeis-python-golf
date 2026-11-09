# A001228

> Orders of sporadic simple groups.
> — [OEIS A001228](https://oeis.org/A001228)

Offset 1: 7920, 95040, 175560, 443520, 604800, 10200960, 44352000, 50232960, 244823040, 898128000, 4030387200, …

### Python 3 — 190 bytes

```python
O=[x:=1,1]
for c in'xBn r78~x(.dxrl"8.7w8tA uc@rb]<.  ul`X}L }oC>~ |u_E"2.|!tXVJ ~W|Qd^LD@ ~u~}{vt[MG':
 if(k:=ord(c))<27:O+=x,;print(x);x=O[k]
 else:x*=k
```

The string holds ASCII control characters (codes 1–26, never 10 or 13), so
the code block above may look garbled. Its contents are decoded in the table
below.

**How it works**

- The sequence is finite. By the classification of finite simple groups
  there are exactly 26 sporadic groups, and their orders are known
  (ATLAS of Finite Groups, 1985). So the program stores those orders and
  prints them in increasing order. Nothing is computed beyond that list.
- Each order is stored as a product. A character with code k ≥ 27 is a
  factor, and `x*=k` multiplies it in. A character with code k < 27 ends
  the current group: it appends `x` to `O`, prints it, and starts the
  next group at `x=O[k]`. `O[1]` is 1 (no parent), and `O[j+1]` is the
  j-th order printed, so a group can start from an earlier group whose
  order divides its own (M22 = M11 × 56). The first group starts at
  `x=1`, and a final `\x01` prints the Monster.
- Every factor is at most 126, so each one costs a single byte. A
  greedy search with a short lookahead picked the factors and parents.
  The whole list of 26 orders takes 117 characters.

| n | group | order | factorization | stored as |
|---|---|---|---|---|
| 1 | M11 | 7920 | 2⁴·3²·5·11 | 120 · 66 |
| 2 | M12 | 95040 | 2⁶·3³·5·11 | 110 · 32 · 27 |
| 3 | J1 | 175560 | 2³·3·5·7·11·19 | 114 · 55 · 28 |
| 4 | M22 | 443520 | 2⁷·3²·5·7·11 | M11 × 56 |
| 5 | J2 | 604800 | 2⁷·3³·5²·7 | 126 · 120 · 40 |
| 6 | M23 | 10200960 | 2⁷·3²·5·7·11·23 | M11 × 46 · 28 |
| 7 | HS | 44352000 | 2⁹·3²·5³·7·11 | M22 × 100 |
| 8 | J3 | 50232960 | 2⁷·3⁵·5·17·19 | 120 · 114 · 108 · 34 |
| 9 | M24 | 244823040 | 2¹⁰·3³·5·7·11·23 | M12 × 56 · 46 |
| 10 | McL | 898128000 | 2⁷·3⁶·5³·7·11 | J2 × 55 · 27 |
| 11 | He | 4030387200 | 2¹⁰·3³·5²·7³·17 | J2 × 119 · 56 |
| 12 | Ru | 145926144000 | 2¹⁴·3³·5³·7·13·29 | J2 × 116 · 65 · 32 |
| 13 | Suz | 448345497600 | 2¹³·3⁷·5²·7·11·13 | J2 × 117 · 99 · 64 |
| 14 | O'N | 460815505920 | 2⁹·3⁴·5·7³·11·19·31 | M22 × 114 · 98 · 93 |
| 15 | Co3 | 495766656000 | 2¹⁰·3⁷·5³·7·11·23 | M23 × 60 · 30 · 27 |
| 16 | Co2 | 42305421312000 | 2¹⁸·3⁶·5³·7·11·23 | McL × 46 · 32 · 32 |
| 17 | Fi22 | 64561751654400 | 2¹⁷·3⁹·5²·7·11·13 | J2 × 117 · 108 · 96 · 88 |
| 18 | HN | 273030912000000 | 2¹⁴·3⁶·5⁶·7·11·19 | McL × 125 · 76 · 32 |
| 19 | Ly | 51765179004000000 | 2⁸·3⁷·5⁶·7·11·31·37·67 | McL × 125 · 111 · 67 · 62 |
| 20 | Th | 90745943887872000 | 2¹⁵·3¹⁰·5³·7²·13·19·31 | J2 × 126 · 32 · 124 · 117 · 95 · 27 |
| 21 | Fi23 | 4089470473293004800 | 2¹⁸·3¹³·5²·7·11·13·17·23 | Fi22 × 69 · 34 · 27 |
| 22 | Co1 | 4157776806543360000 | 2²¹·3⁹·5⁴·7²·11·13·23 | Fi22 × 50 · 46 · 28 |
| 23 | J4 | 86775571046077562880 | 2²¹·3³·5·7·11³·23·29·31·37·43 | M23 × 124 · 33 · 116 · 88 · 86 · 74 · 32 |
| 24 | Fi24′ | 1255205709190661721292800 | 2²¹·3¹⁶·5²·7³·11·13·17·23·29 | Fi23 × 126 · 87 · 28 |
| 25 | B | 4154781481226426191177580544000000 | 2⁴¹·3¹³·5⁶·7²·11·13·17·19·23·31·47 | Co1 × 124 · 81 · 100 · 94 · 76 · 68 · 64 · 32 |
| 26 | M | 808017424794512875886459904961710757005754368000000000 | 2⁴⁶·3²⁰·5⁹·7⁶·11²·13³·17·19·23·29·31·41·47·59·71 | B × 126 · 117 · 126 · 125 · 123 · 118 · 116 · 91 · 77 · 71 |

**Notes**

- The parent links are the only thing the product form buys. Without them
  the orders take about 190 factor characters plus separators, and the decimal
  digits alone are 375 characters.
- The program prints the 26 terms and stops, as a finite sequence should.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 190 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001228), CC BY-SA 4.0.
