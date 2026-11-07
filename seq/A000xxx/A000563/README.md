# A000563

> Number of discordant permutations.
> — [OEIS A000563](https://oeis.org/A000563)

Offset 5: 13, 192, 1085, 3880, 10656, 24626, 50380, 94128, 163943, 270004, …

a(n) is the number of ways to put 5 non-attacking rooks on the n × n board
whose cells are (i, j) with j − i ≡ 0, 1 or 2 (mod n). The page of
[A000561](../A000561/) (3 rooks) explains the board and the name.

### Python 3 — 62 bytes

```python
w=5
while[print((w*(w*(w*(w*w-45)+360)-1596)+3040)//120)]:w+=3
```

**How it works**

- **A polynomial.** 120·a(n) = 243n⁵ − 4050n⁴ + 25785n³ − 74610n² + 83112n for
  n ≥ 5. The proof on the [A000561](../A000561/) page shows that the number of
  k-rook placements is a polynomial of degree ≤ k in n for n ≥ 2k + 1; this
  one is fitted at n = 11, …, 16 (values confirmed by a brute-force count) and
  also matches the b-file for 5 ≤ n ≤ 10.
- **Monic in w = 3n − 10.** The leading coefficient of 120·a(n) is 3⁵, so with
  3n = w + 10 the quintic becomes w⁵ − 45w³ + 360w² − 1596w + 3040 (expanding
  gives back the polynomial in n exactly). `w*(w*(w*(w*w-45)+360)-1596)+3040`
  is that quintic in Horner form, with no w⁴ term: s = 10 removes it. The
  numerator equals 120·a(n), so the division is exact. `w+=3` steps n.
- `while[print(…)]:` loops forever: print returns None and `[None]` is truthy.

**Notes**

- Other versions: the first entry, the quintic in n in Horner form with the
  factor n taken out, `n*((((81*n-1350)*n+8595)*n-24870)*n+27704)//40`, was 70
  bytes.
- Exact integer arithmetic and the proof on the A000561 page, so the program
  is right for every n.
- The whole b-file prints in under 0.1 s here. a(n) has about 5·log₁₀ n
  digits, so the 4300-digit int-to-str limit is out of reach.
- The b-file has 29 terms (up to a(33)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 70 | first entry |
| 2026-11-07 | Python 3 | 62 | monic quintic in w = 3n − 10 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000563), CC BY-SA 4.0.
