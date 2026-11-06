# A000191

> Generalized tangent numbers d(3, n).
> — [OEIS A000191](https://oeis.org/A000191)

Offset 0: 2, 46, 3362, 515086, 135274562, 54276473326, 30884386347362, …

### Python 3 — 79 bytes

```python
r=[2,s:=2]
while[print(s)]:
 for s in 0,-4*r[0]:r=[s:=s+x*3for x in[0]+r[::-1]]
```

**How it works**

- Luschny's e.g.f. in the OEIS entry is 2 sin x/(2 cos 2x − 1), odd terms
  only. Since cos 3x = cos x·(2 cos 2x − 1), this is sin 2x·sec 3x, so
  a(n) = (2n+1)!·[x^(2n+1)] sec 3x·sin 2x.
- The program runs the same weighted Seidel–Entringer (boustrophedon)
  triangle as [A000187](../A000187/), with weight 3: T(m,0) = u_m and
  T(m,k) = T(m,k−1) + 3·T(m−1,m−k). B_m = T(m,m) then has e.g.f.
  (sec 3x + tan 3x)·U(x), where U is the e.g.f. of u.
- Take U = sin 2x, so u_m = 0 for even m and u_(2n+1) = 2·(−4)ⁿ. U is odd,
  so sec 3x·U is odd and tan 3x·U is even: the odd rows carry the sequence,
  T(2n+1,2n+1) = a(n), and the even rows are only scaffolding.
- Each pass of the `while` computes two rows: an even row starting at 0,
  then an odd row starting at u_(2n+1). The tuple `0,-4*r[0]` is built
  before either row, while `r` is still the previous odd row, whose first
  entry is u_(2n−1); so u_(2n+1) = −4·r[0] needs no counter or power.
- The program starts from row 1 = [2, 2] (row 0 is [0]) with s = a(0) = 2.
- `s` is the `for` target, so it already holds the row's first value when
  the comprehension starts; the extra `[0]` in front of the reversed row
  makes the first element s + 0, and the walrus carries the running sum.
  After the odd row, `s` is a(n), which the next `while` header prints.

**Notes**

- Same length, printing even rows instead:
  `r=[s:=2]` / `for s in 3*s,-4*r[0]:` with the same comprehension. Here
  U = 2 cos 2x + 3F(x), F = sin 2x·sec 3x, and the even part of the
  output is sec 3x·2 cos 2x + tan 3x·3F = F′, so T(2n,2n) = a(n) and the
  odd row after it starts at 3·a(n) = 3s.
- Row m has m+1 entries, so a(n) costs about 2n² big-integer additions.
  The whole b-file (251 terms) prints in about 0.1 s; the bar is the
  whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(715) (4299 digits); a(716) has 4306.
- `x*3for` instead of `3*x for`: a digit followed by a keyword needs no
  space (`3for` tokenizes as `3` and `for`, with only a SyntaxWarning on
  stderr), 1 byte less.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 80 | first entry |
| 2026-11-06 | Python 3 | 79 | `x*3for` drops a space (found while golfing A000318) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000191), CC BY-SA 4.0.
