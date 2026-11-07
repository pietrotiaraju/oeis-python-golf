# A000565

> Number of discordant permutations.
> — [OEIS A000565](https://oeis.org/A000565)

Offset 7: 31, 696, 5823, 29380, 108933, 327840, 848380, 1958004, 4130895, 8107024, …

a(n) is the number of ways to put 7 non-attacking rooks on the n × n board
whose cells are (i, j) with j − i ≡ 0, 1 or 2 (mod n). The page of
[A000561](../A000561/) (3 rooks) explains the board and the name.

### Python 3 — 88 bytes

```python
w=6
while[print((w*(w*(w*(w*(w*(w*w-70)+1120)-11711)+75040)-276060)+453600)//5040)]:w+=3
```

**How it works**

- **A polynomial.** 5040·a(n) = 2187n⁷ − 76545n⁶ + 1131165n⁵ − 9052155n⁴ +
  41457528n³ − 103233060n² + 109390320n for n ≥ 7. The proof on the
  [A000561](../A000561/) page shows that the number of k-rook placements is a
  polynomial of degree ≤ k in n for n ≥ 2k + 1; this one is fitted at
  n = 15, …, 22 (values confirmed by a brute-force count) and also matches the
  b-file for 7 ≤ n ≤ 14.
- **Monic in w = 3n − 15.** The leading coefficient of 5040·a(n) is 3⁷, so
  with 3n = w + 15 the septic becomes w⁷ − 70w⁵ + 1120w⁴ − 11711w³ + 75040w² −
  276060w + 453600 (expanding gives back the polynomial in n exactly). The
  numerator is that septic in Horner form, with no w⁶ term: s = 15 removes it.
  The numerator equals 5040·a(n), so the division is exact. `w+=3` steps n.
- `while[print(…)]:` loops forever: print returns None and `[None]` is truthy.

**Notes**

- Other versions: the same polynomial as a difference table,
  `a=[31,665,4462,13968,23598,22194,10935,2187]` and
  `a[:-1]=map(sum,zip(a,a[1:]))` in the loop, is 93 bytes; the first entry,
  that table with `a=[*map(sum,zip(a,a[1:]+[0]))]`, was 94.
- Exact integer arithmetic and the proof on the A000561 page, so the program
  is right for every n.
- The whole b-file prints in under 0.1 s here. a(n) has about 7·log₁₀ n
  digits, so the 4300-digit int-to-str limit is out of reach.
- The b-file has 24 terms (up to a(30)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 94 | first entry |
| 2026-11-07 | Python 3 | 88 | monic septic in w = 3n − 15 instead of the difference table |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000565), CC BY-SA 4.0.
