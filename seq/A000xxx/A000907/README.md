# A000907

> Second-order reciprocal Stirling number (Fekete) a(n) = [[2n+2, n]]. The number of n-orbit permutations of a (2n+2)-set with at least 2 elements in each orbit. Also known as associated Stirling numbers of the first kind (e.g., Comtet).
> — [OEIS A000907](https://oeis.org/A000907)

Offset 1: 6, 130, 2380, 44100, 866250, 18288270, 416215800, 10199989800, …

### Python 3 — 51 bytes

```python
d=m=3
while[print((2*m+3)*(m*m-1)*d//36)]:m+=2;d*=m
```

**How it works**

- n cycles of length ≥ 2 on 2n+2 points use exactly 2 points beyond n
  transpositions, so the cycle type is either one 4-cycle and n−1
  transpositions, or two 3-cycles and n−2 transpositions. Counting each:
  C(2n+2,4)·3!·(2n−3)!! + C(2n+2,6)·40·(2n−5)!! (40 ways to split 6 points
  into two 3-cycles). The sum simplifies to
  a(n) = (4n+5)·n(n+1)·(2n+1)!!/9, the closed form
  (4n+5)(2n+2)!/(9·2^(n+1)·(n−1)!) on the OEIS page.
- With m = 2n+1: 4n+5 = 2m+3 and n(n+1) = (m²−1)/4, so
  a(n) = (2m+3)(m²−1)·m!!/36. `d` is m!!, starting with `d=m=3` (n = 1);
  each pass adds 2 to `m` and multiplies `d` by it.
- Checked against the recurrence d(n,k) = (n−1)(d(n−1,k) + d(n−2,k−1)) of
  the associated Stirling numbers for n ≤ 80, and against the b-file.

**Notes**

- Exact integer arithmetic, correct for every n by the count above.
- The b-file has 16 terms; the bar is the whole b-file in 60 s. The program
  prints 1420 terms at once and then stops with a `ValueError` at the
  4300-digit int-to-str limit of Python 3.11+.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000907), CC BY-SA 4.0.
