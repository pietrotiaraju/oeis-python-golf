# A001108

> a(n)-th triangular number is a square: a(n+1) = 6*a(n) - a(n-1) + 2, with a(0) = 0, a(1) = 1.
> — [OEIS A001108](https://oeis.org/A001108)

Offset 0: 0, 1, 8, 49, 288, 1681, 9800, 57121, 332928, 1940449, 11309768, …

### Python 3 — 35 bytes

```python
a=b=1
while[print(a:=a-b)]:b-=4*a+2
```

**How it works**

- The [A001109](../A001109/) loop with a constant: before a(n) is printed,
  `a` is a(n−1) and `b` is a(n−1) − a(n), so `a:=a-b` in the print steps
  `a` to a(n).
- The recurrence a(n+1) = 6·a(n) − a(n−1) + 2 gives
  a(n) − a(n+1) = (a(n−1) − a(n)) − 4·a(n) − 2, which is `b-=4*a+2`.
- Running the recurrence backwards, a(−1) = 6·0 − 1 + 2 = 1 and
  a(−1) − a(0) = 1, so the two start values are equal again: `a=b=1`.

**Notes**

- Why this is the definition: t(t+1)/2 = m² is (2t+1)² − 8m² = 1, so
  2t + 1 = u(n) with u(n) + m√8 = (3+√8)ⁿ. The u(n) satisfy
  u(n+1) = 6u(n) − u(n−1), and t = (u − 1)/2 then satisfies
  t(n+1) = 6t(n) − t(n−1) + 2. The m are [A001109](../A001109/) and the
  squares t(t+1)/2 are [A001110](../A001110/).
- Another version that prints the same terms: halving u(n) − 1 with the
  Chebyshev pair, `a=b=1` / `while[print(a//2)]:a+=2*b;b+=2*a`: 38 bytes.
  An exhaustive search over two-statement updates with constants ±1, ±2
  (same space as on the A001109 page) found nothing under 35; the best
  without the walrus is `a=0;b=1` / `while[print(a)]:a+=b;b+=4*a+2`,
  37 bytes.
- Python's 4300-digit int-to-str limit stops the program at a(5618), the
  first term with 4301 digits.
- The b-file has 1305 terms (a(0) to a(1304), 998 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001108), CC BY-SA 4.0.
