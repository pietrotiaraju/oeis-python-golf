# A001304

> Expansion of 1/((1-x)^2*(1-x^2)*(1-x^5)).
> — [OEIS A001304](https://oeis.org/A001304)

Offset 0: 1, 2, 4, 6, 9, 13, 18, 24, 31, 39, 49, 60, 73, 87, 103, 121, 141, 163, 187, 213, 242, …

### Python 3 — 43 bytes

```python
s=9
while[print((s**3-31*s+270)//480)]:s+=2
```

**How it works**

- **What it counts.** 1/((1−x)(1−x²)(1−x⁵)) counts the (c, d, q) ≥ 0 with
  c + 2d + 5q = n; the second factor 1/(1−x) sums over n, so a(n) is the
  number of (c, d, q) ≥ 0 with c + 2d + 5q ≤ n. That is the nickel count of
  [A001299](../A001299/): coins 1, 5, 10, 25 for 5n cents, in units of 5
  cents, so a(n) = A001299(5n).
- **The cubic.** The pairs (c, d) with c + 2d ≤ s number g(s) = ⌊(s+2)²/4⌋,
  so a(n) = a(n−5) + g(n), and a(n) = g(n) for n < 5. Let s = 2n + 9 and
  E(n) = (s³ − 31s)/480. Then E(n) − E(n−5) = (s² − 10s + 23)/16
  = (n+2)²/4 − 1/8, while g(n) = (n+2)²/4 − 1/4 for odd n and (n+2)²/4 for
  even n. So δ(n) = a(n) − E(n) changes by ±1/8 when n grows by 5, with
  opposite signs for n and n + 5, and δ(n + 10) = δ(n) for every n ≥ 0.
- For n = 0, …, 9, δ(n) is 1/16, −1/16, 21/80, −1/16, −11/80, −1/16, 1/16,
  11/80, 1/16, −21/80: always within ±21/80. Adding 270/480 = 9/16 leaves
  E + 9/16 between a + 0.3 and a + 0.825, so
  a(n) = ⌊(s³ − 31s + 270)/480⌋ for every n. Any constant from 126 to 353
  works; 126 is Tani Akinari's ⌊(n+8)(2n²+11n+18)/120⌋ on the OEIS entry,
  and 270 the one [A001299](../A001299/) uses.
- The loop variable is s itself: it starts at 9 (n = 0) and steps by 2.
  `print` returns `None` and `[None]` is a non-empty list, so the loop never
  ends.

**Notes**

- Tani Akinari's formula with m = n + 8, `m=8` /
  `while[print(m*(2*m*m-21*m+58)//120)]:m+=1`, is 45 bytes. Partial sums of
  [A000115](https://oeis.org/A000115), round((n+4)²/20), as
  `a=0;n=4` / `while[print(a:=a+(n*n+10)//20)]:n+=1`, are 44.
- The running layer list of [A001301](../A001301/) (pennies twice, then 2
  and 5) is 59 bytes.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n³/60, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001304), CC BY-SA 4.0.
