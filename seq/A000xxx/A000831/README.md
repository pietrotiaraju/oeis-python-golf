# A000831

> Expansion of e.g.f. (1 + tan(x))/(1 - tan(x)).
> — [OEIS A000831](https://oeis.org/A000831)

Offset 0: 1, 2, 4, 16, 80, 512, 3904, 34816, 354560, 4063232, 51733504, 724566016, 11070525440, …

### Python 3 — 60 bytes

```python
t=1;r=[2]
while[print(t)]:r=[2*(t:=t+x)for x in[-t]+r[::-1]]
```

**How it works**

- (1 + tan x)/(1 − tan x) = tan(x + π/4) = sec 2x + tan 2x.
- The program runs the weighted Seidel–Entringer (boustrophedon) triangle
  of [A000187](../A000187/) with weight 2: T(m,0) = u_m and
  T(m,k) = T(m,k−1) + 2·T(m−1,m−k). Its last column T(m,m) has e.g.f.
  (sec 2x + tan 2x)·U(x), where U is the e.g.f. of u (Millar, Sloane and
  Young's boustrophedon transform, rescaled by 2^m).
- Take U = 1 (u_0 = 1, all other u_m = 0): then T(m,m) = a(m), which is
  also 2ᵐ·E_m with E_m the Euler zigzag numbers [A000111](../A000111/).
- The list keeps every row doubled, `r` = 2·T(m,·), while the walrus `t`
  runs over T itself: `2*(t:=t+x)` adds x = 2·T(m−1,m−k) and stores the
  doubled sum. The weight costs 3 bytes over the plain
  [A000111](../A000111/) program, and a half-integer start such as
  u_0 = 1/2 is still an integer in the list.
- Row 0 is `t=1;r=[2]` (the stored 2 is 2·1). Each new row starts with
  `[-t]`, so its first entry is t − t = 0 = u_m, and the last t is a(m).

**Notes**

- [A000828](../A000828/) runs the same program from `r=[t:=1]`
  (U = 1/2); for n ≥ 1 its terms are half of these.
- Row m has m+1 entries, so a(n) costs about n²/2 big-integer additions.
  The whole b-file (433 terms) prints in about a tenth of a second; the
  bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1508) (about 2.5 s here).
- Printing `t<<len(r)-1` from the [A000111](../A000111/) program, or
  `r[-1]` from the A000828 program, costs more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000831), CC BY-SA 4.0.
