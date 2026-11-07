# A000464

> Expansion of e.g.f. sin(x)/cos(2*x).
> — [OEIS A000464](https://oeis.org/A000464)

Offset 0: 1, 11, 361, 24611, 2873041, 512343611, 129570724921, 44110959165011, 19450718635716001, 10784052561125704811, …

sin x/cos 2x is odd, and a(n) is its (2n+1)-th e.g.f. coefficient:
a(n) = (2n+1)!·[x^(2n+1)] sin x·sec 2x.

### Python 3 — 77 bytes

```python
r=[1,s:=1]
while[print(s)]:
 for s in 0,-r[0]:r=[s:=s+x*2for x in[0]+r[::-1]]
```

**How it works**

- **The triangle.** The program runs a weighted Seidel–Entringer
  (boustrophedon) triangle, as in [A000187](../A000187/) and
  [A000191](../A000191/): T(m, 0) = u_m and T(m, k) = T(m, k−1) +
  2·T(m−1, m−k). With weight 1 this is the boustrophedon transform of
  Millar, Sloane and Young (1996): B_m = T(m, m) has e.g.f.
  (sec x + tan x)·U(x), U the e.g.f. of u. With weight c, T(m, k) =
  c^m·T′(m, k) for the weight-1 triangle T′ started from u_m/c^m, so B has
  e.g.f. (sec cx + tan cx)·U(x).
- **The start column.** Take c = 2 and U = sin x: u_m = 0 for even m and
  u_(2n+1) = (−1)ⁿ. sec 2x·sin x is odd and tan 2x·sin x is even, so the
  odd rows carry the sequence, T(2n+1, 2n+1) = a(n), and the even rows
  are scaffolding.
- **Two rows per pass.** The tuple `0,-r[0]` is built before either row,
  while `r` is still the previous odd row, whose first entry is
  u_(2n−1); so the even row starts at 0 and the odd row at
  u_(2n+1) = −u_(2n−1), with no counter.
- `s` is the `for` target, so it holds the row's first value when the
  comprehension starts; the extra `[0]` makes the first element s + 0,
  and the walrus carries the running sum. After the odd row, `s` is a(n),
  which the next `while` header prints. The start `r=[1,s:=1]` is row 1
  (row 0 is [0]) with s = a(0) = 1.

**Notes**

- Other versions that print the same terms: the convolution of the
  e.g.f. identity cos 2x·F = sin x, a(n) = (−1)ⁿ −
  Σ_{k=1}^{n} C(2n+1, 2k)·(−4)^k·a(n−k), with `math.comb`: 122 bytes,
  with n big products per term where the triangle only adds (754 terms
  in 22 s instead of 2.5 s).
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 216 terms print in 0.1 s here. The b-file has 216 terms (up
  to a(215)); the bar is the whole b-file in 60 s.
- a(754) is the first term with more than 4300 digits, so printing stops
  there (after about 2.5 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 123 | first entry |
| 2026-11-06 | Python 3 | 122 | use a shorter math import |
| 2026-11-07 | Python 3 | 77 | weighted Seidel triangle with u = sin x |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000464), CC BY-SA 4.0.
