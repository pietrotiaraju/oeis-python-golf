# A000436

> Generalized Euler numbers c(3,n).
> — [OEIS A000436](https://oeis.org/A000436)

Offset 0: 1, 8, 352, 38528, 7869952, 2583554048, 1243925143552, 825787662368768, 722906928498737152, 806875574817679474688, …

a(n) is the coefficient of x^(2n)/(2n)! in cos(x)/cos(3x).

### Python 3 — 75 bytes

```python
r=[s:=1]
while[print(s)]:
 for s in 0,-r[0]:r=[s:=s+x*3for x in[0]+r[::-1]]
```

**How it works**

- This is the weighted Seidel–Entringer (boustrophedon) triangle of
  [A000187](../A000187/): T(m,0) = u_m and T(m,k) = T(m,k−1) + 3·T(m−1,m−k),
  each row a running sum over the previous row read backwards. With weight c
  the diagonal B_m = T(m,m) has e.g.f. (sec cx + tan cx)·U(x), where U is the
  e.g.f. of u.
- Take c = 3 and U = cos x, so u_m = 0 for odd m and u_(2n) = (−1)ⁿ. U is
  even, so tan 3x·cos x is odd and only feeds the odd rows; the even part
  sec 3x·cos x = cos x / cos 3x is the e.g.f. of a(n), so T(2n,2n) = a(n).
- Each pass of the `while` computes two rows: an odd row starting at 0, then
  an even row starting at u_(2n). The tuple `0,-r[0]` is built once, from the
  previous even row, whose first entry is u_(2n−2) = (−1)ⁿ⁻¹; so `-r[0]` is
  u_(2n) with no sign counter.
- `s` is the `for` target, so it already holds the row's first value when
  the comprehension starts; the extra `[0]` in front of the reversed row
  makes the first element s + 0, and the walrus carries the running sum.
  After the even row, `s` is a(n), which the next `while` header prints.
  `r=[s:=1]` is row 0 and a(0) = 1.

**Notes**

- The 110-byte previous entry used R. J. Mathar's recurrence
  b(n) = 1 − Σ_{k≥1} C(2n,2k)·9^k·b(n−k) for b(n) = (−1)ⁿa(n), with
  `math.comb`; the triangle needs neither the import nor binomials.
- `x*3for`: a digit followed by a keyword needs no space (only a
  SyntaxWarning on stderr).
- Exact integer arithmetic, so the program is right for every n. Row m has
  m+1 entries, so a(n) costs about 2n² big-integer additions.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s, which takes a few hundredths of a second here.
- a(716) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there (716 terms, well under 60 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 123 | first entry |
| 2026-11-06 | Python 3 | 122 | use a shorter math import |
| 2026-11-06 | Python 3 | 120 | remove addition of zero in the binomial argument |
| 2026-11-07 | Python 3 | 110 | signed values (−1)ⁿa(n) and the k = 0 term from `a[0]` |
| 2026-11-07 | Python 3 | 75 | weighted boustrophedon triangle of A000187 with U = cos x |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000436), CC BY-SA 4.0.
