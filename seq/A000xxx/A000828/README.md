# A000828

> E.g.f. cos(x)/(cos(x) - sin(x)).
> — [OEIS A000828](https://oeis.org/A000828)

Offset 0: 1, 1, 2, 8, 40, 256, 1952, 17408, 177280, 2031616, 25866752, 362283008, 5535262720, …

### Python 3 — 59 bytes

```python
r=[t:=1]
while[print(t)]:r=[2*(t:=t+x)for x in[-t]+r[::-1]]
```

**How it works**

- cos x/(cos x − sin x) = 1/(1 − tan x) = (1 + (1 + tan x)/(1 − tan x))/2,
  so the e.g.f. is (1 + sec 2x + tan 2x)/2, and a(n) = 2ⁿ⁻¹·E_n for
  n ≥ 1, with E_n the Euler zigzag numbers [A000111](../A000111/).
- (1 + tan x)/(1 − tan x) = tan(x + π/4) = sec 2x + tan 2x.
- The program runs the weighted Seidel–Entringer (boustrophedon) triangle
  of [A000187](../A000187/) with weight 2: T(m,0) = u_m and
  T(m,k) = T(m,k−1) + 2·T(m−1,m−k). Its last column T(m,m) has e.g.f.
  (sec 2x + tan 2x)·U(x), where U is the e.g.f. of u (Millar, Sloane and
  Young's boustrophedon transform, rescaled by 2^m).
- Take U = 1/2 (u_0 = 1/2, all other u_m = 0): then T(m,m) = a(m) for
  m ≥ 1, and the "+1/2" of the e.g.f. only changes a(0).
- The list keeps every row doubled, `r` = 2·T(m,·), while the walrus `t`
  runs over T itself: `2*(t:=t+x)` adds x = 2·T(m−1,m−k) and stores the
  doubled sum. The weight costs 3 bytes over the plain
  [A000111](../A000111/) program, and a half-integer start such as
  u_0 = 1/2 is still an integer in the list.
- Row 0 is `r=[t:=1]`: the stored 1 is 2·(1/2), while t = 1 is a(0).
  Each new row starts with `[-t]`, so its first entry is t − t = 0 = u_m,
  and the last t is a(m).

**Notes**

- [A000831](../A000831/) is the same triangle with U = 1 and
  [A000834](../A000834/) with U = eˣ; the even terms are
  [A000819](../A000819/).
- Row m has m+1 entries, so a(n) costs about n²/2 big-integer additions.
  The whole b-file (201 terms) prints in a few hundredths of a second;
  the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1508) (about 2.5 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000828), CC BY-SA 4.0.
