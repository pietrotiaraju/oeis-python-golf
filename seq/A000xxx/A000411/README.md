# A000411

> Generalized tangent numbers d(6,n).
> — [OEIS A000411](https://oeis.org/A000411)

Offset 1: 6, 522, 152166, 93241002, 97949265606, 157201459863882, 357802951084619046, 1096291279711115037162, 4350684698032741048452486, 21709332137467778453687752842, …

### Python 3 — 90 bytes

```python
r=[6,s:=6];q=5
while[print(s)]:
 for s in 0,(q:=q*-25)-1|2:r=[s:=s+x*6for x in[0]+r[::-1]]
```

**How it works**

- Luschny's formula in the entry: a(n) = (2n−1)!·[x^(2n−1)] sec 6x·U(x)
  with U(x) = sin x + sin 5x. (Chapoton's form 2 sin 3x/(2 cos 4x − 1) is
  the same series, since cos 6x = cos 2x·(2 cos 4x − 1).)
- The program runs the weighted Seidel (boustrophedon) triangle of
  [A000187](../A000187/) and [A000191](../A000191/) with weight 6:
  T(m, 0) = u_m and T(m, k) = T(m, k−1) + 6·T(m−1, m−k). Its diagonal
  T(m, m) has e.g.f. (sec 6x + tan 6x)·U(x) when u_m are the coefficients
  of U. U is odd, so sec 6x·U is odd and tan 6x·U even: the odd rows give
  a(n) = T(2n−1, 2n−1), and the even rows (which start with u = 0) are
  scaffolding.
- `r=[s:=s+x*6for x in[0]+r[::-1]]` builds a row from the previous one:
  `s` already holds T(m, 0) as the `for` target, the `[0]` makes the
  first entry s + 0, and the walrus carries the running sum over the
  reversed previous row.
- u_(2n−1) = (−1)^(n−1)·(1 + 5^(2n−1)) = q ± 1 with q = 5·(−25)^(n−1), the
  sign being that of q. Since −25 ≡ −1 (mod 8), q ≡ 5 (mod 8) when q > 0
  and q ≡ 3 (mod 8) when q < 0. So q − 1 ≡ 4 or 2 (mod 8), and `|2`
  turns it into q + 1 or leaves q − 1: `(q:=q*-25)-1|2` is the next odd
  start, built in the tuple before either row of the pass.
- The start is row 1 = [6, 6] (u₁ = 6) with `s` = a(1) = 6 and q = 5;
  each `while` pass prints `s` and then builds an even and an odd row.

**Notes**

- u is not geometric, so the `-4*r[0]` start of [A000191](../A000191/)
  does not carry over; the `|2` rounding is the [A000192](../A000192/)
  trick. The recurrence from (2 cos 4x − 1)·A(x) = 2 sin 3x with
  `math.comb` was 127 bytes.
- Exact integer arithmetic; correctness for every n rests on the
  triangle's e.g.f. (Millar, Sloane and Young; see A000187) and on
  Luschny's e.g.f.
- The b-file has 184 terms (up to a(184)) and prints in about 0.1 s; the
  bar is the whole b-file in 60 s.
- a(659) is the first term with more than 4300 digits, so printing stops
  there, after about 2 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 128 | first entry |
| 2026-11-06 | Python 3 | 127 | use a shorter math import |
| 2026-11-07 | Python 3 | 90 | weighted Seidel triangle with U = sin x + sin 5x |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000411), CC BY-SA 4.0.
