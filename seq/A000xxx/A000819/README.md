# A000819

> E.g.f.: cos(x)^2 / cos(2x) = Sum_{n >= 0} a(n) * x^(2n) / (2n)!.
> — [OEIS A000819](https://oeis.org/A000819)

Offset 0: 1, 2, 40, 1952, 177280, 25866752, 5535262720, 1633165156352, 635421069967360, …

### Python 3 — 70 bytes

```python
r=[t:=1]
while[print(t)]:exec("r=[2*(t:=t+x)for x in[-t]+r[::-1]];"*2)
```

**How it works**

- cos²x = (1 + cos 2x)/2, so the e.g.f. is (1 + sec 2x)/2, the even part of
  (1 + sec 2x + tan 2x)/2 = cos x/(cos x − sin x). So a(n) is
  [A000828](../A000828/)(2n).
- The program is the A000828 program with two rows per pass: the
  weighted boustrophedon triangle T(m,k) = T(m,k−1) + 2·T(m−1,m−k) with
  U = 1/2 has T(m,m) = A000828(m) for m ≥ 1, because
  (1 + tan x)/(1 − tan x) = sec 2x + tan 2x and the last column of the
  triangle has e.g.f. (sec 2x + tan 2x)·U(x) (see
  [A000187](../A000187/)).
- Rows are stored doubled (`r` = 2·T, `t` runs over T), so U = 1/2 is the
  integer row `[1]`; `[-t]` starts every row at 0.
- `exec("…;"*2)` runs the row step twice, so after each pass t is the
  next even-indexed term.

**Notes**

- `exec` is 4 bytes under a `for _ in 0,0:` loop on its own line, and 1
  under testing the row length in the `while` header.
- Row m has m+1 entries, so a(n) costs about 4n² big-integer additions.
  The whole b-file (201 terms) prints in about a tenth of a second; the
  bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(754) (about 2.5 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000819), CC BY-SA 4.0.
