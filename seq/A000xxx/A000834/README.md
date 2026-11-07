# A000834

> Expansion of e.g.f. exp(x)*(1 + tan(x))/(1 - tan(x)).
> — [OEIS A000834](https://oeis.org/A000834)

Offset 0: 1, 3, 9, 35, 177, 1123, 8569, 76355, 777697, 8911683, 113466729, 1589173475, …

### Python 3 — 61 bytes

```python
t=1;r=[2]
while[print(t)]:r=[2*(t:=t+x)for x in[1-t]+r[::-1]]
```

**How it works**

- (1 + tan x)/(1 − tan x) = tan(x + π/4) = sec 2x + tan 2x.
- The program runs the weighted Seidel–Entringer (boustrophedon) triangle
  of [A000187](../A000187/) with weight 2: T(m,0) = u_m and
  T(m,k) = T(m,k−1) + 2·T(m−1,m−k). Its last column T(m,m) has e.g.f.
  (sec 2x + tan 2x)·U(x), where U is the e.g.f. of u (Millar, Sloane and
  Young's boustrophedon transform, rescaled by 2^m).
- Take U = eˣ, so u_m = 1 for every m: then T(m,m) = a(m).
- The list keeps every row doubled, `r` = 2·T(m,·), while the walrus `t`
  runs over T itself: `2*(t:=t+x)` adds x = 2·T(m−1,m−k) and stores the
  doubled sum. The weight costs 3 bytes over the plain
  [A000111](../A000111/) program, and a half-integer start such as
  u_0 = 1/2 is still an integer in the list.
- Row 0 is `t=1;r=[2]` (the stored 2 is 2·1). Each new row starts with
  `[1-t]`, so its first entry is t + 1 − t = 1 = u_m, and the last t is
  a(m).

**Notes**

- R. J. Mathar's formula in the entry (the binomial transform of
  [A000831](../A000831/)) is exactly what the start u_m = 1 does.
- Row m has m+1 entries, so a(n) costs about n²/2 big-integer additions.
  The whole b-file (162 terms) prints in a few hundredths of a second;
  the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1508) (about 2.5 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000834), CC BY-SA 4.0.
