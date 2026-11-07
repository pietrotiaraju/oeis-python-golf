# A000562

> Number of discordant permutations.
> — [OEIS A000562](https://oeis.org/A000562)

Offset 4: 9, 95, 420, 1225, 2834, 5652, 10165, 16940, 26625, 39949, …

a(n) is the number of ways to put 4 non-attacking rooks on the n × n board
whose cells are (i, j) with j − i ≡ 0, 1 or 2 (mod n). The page of
[A000561](../A000561/) (3 rooks) explains the board and the name.

### Python 3 — 55 bytes

```python
w=1
while[print(w*(w*(w*(w+14)+43)+110)//24+2//w)]:w+=3
```

**How it works**

- **A polynomial.** 24·a(n) = 81n⁴ − 810n³ + 2763n² − 3234n for n ≥ 5 (the
  OEIS formula for n > 4). The proof on the [A000561](../A000561/) page shows
  that the number of k-rook placements is a polynomial of degree ≤ k in n for
  n ≥ 2k + 1; this one is fitted at n = 9, …, 13 (values confirmed by a
  brute-force count) and also matches the b-file for 5 ≤ n ≤ 8.
- **Monic in w = 3n − 11.** The leading coefficient of 24·a(n) is 3⁴, so with
  3n = w + 11 the quartic becomes w⁴ + 14w³ + 43w² + 110w (expanding gives
  back the polynomial in n exactly). `w*(w*(w*(w+14)+43)+110)//24` is the
  quartic in Horner form; `*` and `//` group from the left, so the whole
  product is divided. The numerator equals 24·a(n), so the division is exact.
  `w+=3` steps n.
- **a(4).** The quartic gives 7 at n = 4, but a(4) = 9. `w=1` is n = 4, and
  `2//w` adds 2 there and 0 from w = 4 (n = 5) on.
- `while[print(…)]:` loops forever: print returns None and `[None]` is truthy.

**Notes**

- Other versions: the first entry, `print(9)` and then the quartic in n in
  Horner form with the factor n taken out, was 65 bytes.
- Exact integer arithmetic and the proof on the A000561 page, so the program
  is right for every n.
- The whole b-file prints in under 0.1 s here. a(n) has about 4·log₁₀ n
  digits, so the 4300-digit int-to-str limit is out of reach.
- The b-file has 36 terms (up to a(39)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 65 | first entry |
| 2026-11-07 | Python 3 | 55 | monic quartic in w = 3n − 11, a(4) through `2//w` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000562), CC BY-SA 4.0.
