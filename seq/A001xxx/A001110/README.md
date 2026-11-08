# A001110

> Square triangular numbers: numbers that are both triangular and square.
> — [OEIS A001110](https://oeis.org/A001110)

Offset 0: 0, 1, 36, 1225, 41616, 1413721, 48024900, 1631432881, 55420693056, …

### Python 3 — 36 bytes

```python
a=b=1
while[print(a:=a-b)]:b-=32*a+2
```

**How it works**

- a(n) = m(n)², where m(n) = [A001109](../A001109/)(n): t(t+1)/2 = m² is
  the Pell equation (2t+1)² − 8m² = 1, whose solutions are
  (2t+1) + m√8 = (3+√8)ⁿ.
- With r = 3+√8, m(n) = (rⁿ − r⁻ⁿ)/√32, so
  a(n) = (r²ⁿ + r⁻²ⁿ − 2)/32. Since r² + r⁻² = 34, this gives
  a(n+1) = 34·a(n) − a(n−1) + 2 for every n, and the program runs that
  recurrence directly instead of squaring.
- It is the [A001108](../A001108/) loop with 34 in place of 6: `b` is
  a(n−1) − a(n), the walrus `a:=a-b` steps `a`, and
  a(n) − a(n+1) = (a(n−1) − a(n)) − 32·a(n) − 2 is `b-=32*a+2`. Backwards,
  a(−1) = 34·0 − 1 + 2 = 1, so `a=b=1`.

**Notes**

- Other versions that print the same terms: squaring the A001109 pair,
  `a=0;b=1` / `while[print(a*a)]:a+=b;b+=4*a`: 37 bytes; squaring the
  A001109 walrus loop, `a=b=-1` / `while[print((a:=a-b)**2)]:b-=4*a`:
  39 bytes; (u² − 1)/8 with the Chebyshev u = 2t + 1,
  `a=b=1` / `while[print(a*a>>3)]:a+=2*b;b+=2*a`: 40 bytes. The search on
  the A001109 page (two-statement updates with constants, squares and
  walruses in the print) found nothing under 36.
- Exact integers, so every term is right. Python's 4300-digit int-to-str
  limit stops the program at a(2810), the first term with 4301 digits.
- The b-file has 601 terms (a(0) to a(600), 918 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001110), CC BY-SA 4.0.
