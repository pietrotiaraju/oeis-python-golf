# A000564

> Number of discordant permutations.
> — [OEIS A000564](https://oeis.org/A000564)

Offset 6: 20, 371, 2588, 11097, 35645, 94457, 218124, 454220, 872648, 1571715, …

a(n) is the number of ways to put 6 non-attacking rooks on the n × n board
whose cells are (i, j) with j − i ≡ 0, 1 or 2 (mod n). The page of
[A000561](../A000561/) (3 rooks) explains the board and the name.

### Python 3 — 81 bytes

```python
w=2
while[print((w*(w*(w*(w*(w*(w+21)+125)+715)+154)+3544)-3200)//720+4//w)]:w+=3
```

**How it works**

- **A polynomial.** 720·a(n) = 729n⁶ − 18225n⁵ + 185085n⁴ − 957015n³ +
  2526426n² − 2731320n for n ≥ 7. The proof on the [A000561](../A000561/) page
  shows that the number of k-rook placements is a polynomial of degree ≤ k in
  n for n ≥ 2k + 1; this one is fitted at n = 13, …, 19 (values confirmed by a
  brute-force count) and also matches the b-file for 7 ≤ n ≤ 12.
- **Monic in w = 3n − 16.** The leading coefficient of 720·a(n) is 3⁶, so with
  3n = w + 16 the sextic becomes w⁶ + 21w⁵ + 125w⁴ + 715w³ + 154w² + 3544w −
  3200 (expanding gives back the polynomial in n exactly). The numerator is
  that sextic in Horner form; `//720` divides all of it. The numerator equals
  720·a(n), so the division is exact. `w+=3` steps n.
- **a(6).** The sextic gives 18 at n = 6, but a(6) = 20. `w=2` is n = 6, and
  `4//w` adds 2 there and 0 from w = 5 (n = 7) on.
- `while[print(…)]:` loops forever: print returns None and `[None]` is truthy.

**Notes**

- Other versions: the first entry, `print(20)` and then the sextic in n in
  Horner form with the factor n taken out, was 94 bytes.
- Exact integer arithmetic and the proof on the A000561 page, so the program
  is right for every n.
- The whole b-file prints in under 0.1 s here. a(n) has about 6·log₁₀ n
  digits, so the 4300-digit int-to-str limit is out of reach.
- The b-file has 25 terms (up to a(30)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 94 | first entry |
| 2026-11-07 | Python 3 | 81 | monic sextic in w = 3n − 16, a(6) through `4//w` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000564), CC BY-SA 4.0.
