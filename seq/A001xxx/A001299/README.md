# A001299

> Number of ways of making change for n cents using coins of 1, 5, 10, 25 cents.
> — [OEIS A001299](https://oeis.org/A001299)

Offset 0: 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 9, …

### Python 3 — 54 bytes

```python
s=9
while[exec("print((s**3-31*s+270)//480);"*5)]:s+=2
```

**How it works**

- **Count in nickels.** Pennies pay whatever is left, so with t = ⌊n/5⌋,
  a(n) = f(t), the number of (c, d, q) ≥ 0 with c + 2d + 5q ≤ t (nickels,
  dimes, quarters). The pairs (c, d) with c + 2d ≤ s number
  g(s) = ⌊(s+2)²/4⌋, so f(t) = f(t−5) + g(t), and f(t) = g(t) for t < 5.
- **The cubic.** Let s = 2t + 9 and E(t) = (s³ − 31s)/480. Then
  E(t) − E(t−5) = (s² − 10s + 23)/16 = (t+2)²/4 − 1/8, while
  g(t) = (t+2)²/4 − 1/4 for odd t and (t+2)²/4 for even t. So
  δ(t) = f(t) − E(t) changes by ±1/8 when t grows by 5, with opposite signs
  for t and t + 5 (5 is odd), and δ(t + 10) = δ(t) for every t ≥ 0.
- For t = 0, …, 9, δ(t) is 1/16, −1/16, 21/80, −1/16, −11/80, −1/16, 1/16,
  11/80, 1/16, −21/80: always within ±21/80. Adding 270/480 = 9/16 leaves
  E + 9/16 between f + 0.3 and f + 0.825, so
  f(t) = ⌊(s³ − 31s + 270)/480⌋ for every t (any constant from 126 to 353
  works; 270 is Kirchner's rounding formula on the OEIS entry in integer
  form).
- **Five equal terms per pass.** a(n) depends only on ⌊n/5⌋, so the loop
  runs over s = 9, 11, 13, … and `exec` runs the `print` five times:
  n = 5t, …, 5t + 4. The `None` from `exec` in `[…]` keeps the loop going.

**Notes**

- Looping over n instead, `n=0` /
  `while[print(((s:=n//5*2+9)**3-31*s+270)//480)]:n+=1`, is 55 bytes;
  printing five copies with `print(*[…]*5,sep="
")` is 56. Summing
  g(t − 5q) directly, `m=10` /
  `while[print(sum(j*j//4for j in range(m//5,0,-5)))]:m+=1`, is 60.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n³/7500, far from the 4300-digit int-to-str limit.
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes about half a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001299), CC BY-SA 4.0.
