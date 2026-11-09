# A001300

> Number of ways of making change for n cents using coins of 1, 5, 10, 25, 50 cents.
> — [OEIS A001300](https://oeis.org/A001300)

Offset 0: 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 9, …

### Python 3 — 74 bytes

```python
m=60
while[print(sum((m-5*j)//50*(j*j//4)for j in range(m//5,0,-5)))]:m+=1
```

**How it works**

- **Count in nickels.** Pennies pay whatever is left, so with t = ⌊n/5⌋,
  a(n) is the number of (c, d, q, h) ≥ 0 with c + 2d + 5q + 10h ≤ t
  (nickels, dimes, quarters, halves). If quarters and halves make 5r
  nickels, q + 2h = r has ⌊r/2⌋ + 1 solutions, and the pairs (c, d) with
  c + 2d ≤ t − 5r number ⌊(t − 5r + 2)²/4⌋. So
  a(n) = Σ_{r ≤ t/5} (⌊r/2⌋ + 1)·⌊(t − 5r + 2)²/4⌋.
- With m = n + 60, j runs from ⌊m/5⌋ = t + 12 down in steps of 5: j = t + 12
  − 5i. For i = r + 2 the term `j*j//4` is ⌊(t − 5r + 2)²/4⌋. The weight is
  `(m-5*j)//50`: m − 5j = 25i + (n mod 5), so it is ⌊i/2⌋ = ⌊r/2⌋ + 1, and
  0 for the two extra first values i = 0, 1. The range stops before j = 0;
  j = 1 adds `1//4` = 0 and j ≥ 2 is exactly t − 5r ≥ 0.
- This is the 5-cent-unit version of the sum behind
  [A000008](../../A000xxx/A000008/) (coins 1, 2, 5, 10), with ⌊j²/4⌋ in
  place of ⌊j/2⌋ because pennies add one more free coin.

**Notes**

- Writing the weight as `(m//5-j)//10` is 75 bytes; a double sum over
  halves and quarters, `sum(j*j//4for k in range(m//5,0,-10)for j in
  range(k,0,-5))`, is 83; summing the cubic of [A001299](../A001299/) over
  the halves is 78, and the weighted sum with five prints per pass is 80.
  Unlike A001299, no formula ⌊P(t)⌋ with a single polynomial P exists:
  the generating function in t has a double pole at −1, which adds an
  unbounded (−1)^t·t/160 term.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁴/1500000, far from the 4300-digit int-to-str limit.
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001300), CC BY-SA 4.0.
