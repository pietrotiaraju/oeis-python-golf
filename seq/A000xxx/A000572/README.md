# A000572

> A Beatty sequence: [ n(e+1) ].
> — [OEIS A000572](https://oeis.org/A000572)

Offset 1: 3, 7, 11, 14, 18, 22, 26, 29, 33, 37, …

### Python 3 — 46 bytes

```python
n=F=1;M=3
while[print(M//F)]:F*=n;n+=1;M=M*n+1
```

**How it works**

- **Truncating the series is exact.** Let S_n = 1/0! + 1/1! + … + 1/n!.
  Then n!·e = N + r with N = n!·S_n an integer and 0 < r = 1/(n+1) +
  1/((n+1)(n+2)) + … < 1/n ≤ 1. So n·e = (N + r)/(n−1)!, and since N < N + r
  < N + 1, ⌊n·e⌋ = ⌊N/(n−1)!⌋ = ⌊n·S_n⌋. (This is the argument behind the
  irrationality of e; no approximation bound is needed.)
- **The numerator.** Hence a(n) = ⌊n·(S_n + 1)⌋ = ⌊M/F⌋ with
  M = n!·(S_n + 1) and F = (n−1)!. Both satisfy one-line recurrences:
  M(n) = n·M(n−1) + 1 (the new term n!/n! = 1), with M(1) = 1!·(2 + 1) = 3,
  and F(n) = (n−1)·F(n−1).
- **The loop.** `F*=n` runs with the old n, then `n+=1`, then `M=M*n+1`
  with the new one. This is the [A000210](../A000210/) program
  (⌊n(e − 1)⌋) with the start value M = 3 instead of 1: changing the constant
  term of S_n + c only changes M(1).

**Notes**

- Other versions that print the same terms: the A000210 loop with the
  difference added at the end, `n=M=F=1` / `while[print(M//F+2*n)]:…`:
  48 bytes.
- Integers only, no floats, so the program is right for every n.
- M and F grow like n!, so a term costs time proportional to log n!. The
  b-file has 59 terms (up to a(59), the entry's data); the bar is the whole
  b-file in 60 s, and the program prints it at once.
- a(n) < 4n, so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |
| 2026-11-07 | Python 3 | 46 | exact truncation ⌊n·e⌋ = ⌊n·S_n⌋, the A000210 loop with M(1) = 3 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000572), CC BY-SA 4.0.
