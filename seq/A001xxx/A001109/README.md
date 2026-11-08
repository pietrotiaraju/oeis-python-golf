# A001109

> a(n)^2 is a triangular number: a(n) = 6*a(n-1) - a(n-2) with a(0)=0, a(1)=1.
> — [OEIS A001109](https://oeis.org/A001109)

Offset 0: 0, 1, 6, 35, 204, 1189, 6930, 40391, 235416, 1372105, 7997214, …

### Python 3 — 34 bytes

```python
a=b=-1
while[print(a:=a-b)]:b-=4*a
```

**How it works**

- `b` holds minus the first difference: before a(n) is printed, `a` is
  a(n−1) and `b` is a(n−1) − a(n), so the walrus `a:=a-b` in the print
  steps `a` to a(n).
- The recurrence a(n+1) = 6·a(n) − a(n−1) gives
  a(n) − a(n+1) = (a(n−1) − a(n)) − 4·a(n), which is `b-=4*a`.
- The start is one step before a(0), with the recurrence run backwards:
  a(−1) = 6·0 − 1 = −1 and a(−1) − a(0) = −1, so `a=b=-1`. This is the
  [A001090](../A001090/) program with 6 in place of 8.

**Notes**

- Why the squares are triangular: m² = t(t+1)/2 is (2t+1)² − 8m² = 1, a
  Pell equation whose solutions are (2t+1) + m√8 = (3+√8)ⁿ, and the m part
  is this a(n). The t part is [A001108](../A001108/) and the squares a(n)²
  are the square triangular numbers [A001110](../A001110/); all three use
  the same loop.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, with or without a constant ±1, ±2, either order), the same
  with a walrus in the print, and start values `a=b=c` or `a=c;b=d` for
  small c, d, found nothing shorter. The best without the walrus is
  `a=0;b=1` / `while[print(a)]:a+=b;b+=4*a`, 35 bytes.
- Python's 4300-digit int-to-str limit stops the program at a(5618), the
  first term with 4301 digits, after printing a(0) to a(5617).
- The b-file has 1305 terms (a(0) to a(1304), 998 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001109), CC BY-SA 4.0.
