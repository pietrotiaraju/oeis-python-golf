# A000320

> Generalized tangent numbers d(5,n).
> — [OEIS A000320](https://oeis.org/A000320)

Offset 1: 4, 272, 55744, 23750912, 17328937984, 19313964388352, …

### Python 3 — 89 bytes

```python
r=[q:=4,s:=4]
while[print(s)]:
 for s in 0,(q:=10-9*q)&-4:r=[s:=s+x*5for x in[0]+r[::-1]]
```

**How it works**

- a(n) = (2n−1)!·[x^(2n−1)] sec 5x·(sin x + sin 3x) (Luschny's e.g.f. in
  the OEIS entry).
- The program runs the weighted Seidel–Entringer (boustrophedon) triangle
  of [A000187](../A000187/) and [A000191](../A000191/): T(m,0) = u_m and
  T(m,k) = T(m,k−1) + 5·T(m−1,m−k). B_m = T(m,m) then has e.g.f.
  (sec 5x + tan 5x)·U(x), where U is the e.g.f. of u (the A000187 page
  explains why).
- Take U = sin x + sin 3x, so u_m = 0 for even m and
  u_(2n+1) = (−1)ⁿ·(1 + 3^(2n+1)). U is odd, so sec 5x·U is odd and
  tan 5x·U is even: the odd rows carry the sequence,
  T(2n−1,2n−1) = a(n), and the even rows are only scaffolding.
- Each pass of the `while` computes two rows: an even row starting at 0,
  then an odd row starting at u_(2n+1). `s` is the `for` target, so it
  already holds the row's first value when the comprehension starts; the
  `[0]` in front of the reversed row makes the first element s + 0, and the
  walrus carries the running sum. After the odd row `s` is a(n), which the
  next `while` header prints.
- u_(2n+1) comes from q = p + 1, where p = (−1)ⁿ·3^(2n+1). Since p goes to
  −9p, q goes to 10 − 9q. A power 3^odd is 3 mod 4, so p is 3 mod 4 for
  even n and 1 mod 4 for odd n; q is then 0 or 2 mod 4, and `q&-4` is
  q = p + 1 or q − 2 = p − 1, that is p + (−1)ⁿ = u_(2n+1) in both cases.
  So one walrus carries both geometric terms, with no separate sign.
- The program starts from row 1 = [4, 4] with s = a(1) = 4 and q = 4
  (n = 0: p = 3), all three set by `r=[q:=4,s:=4]`.

**Notes**

- Exact integer arithmetic, correct for every n.
- Keeping p itself, `r=[4,s:=4];p=3` with `(p:=p*-9)+1&-4`, is 90 bytes.
  Deriving u from the previous odd row's first entry x = r[0] needs a
  sign, u = −9x + 8·sgn x, and is longer.
- `x*5for` saves the space of `5*x for`; the `SyntaxWarning` for `5for`
  goes to stderr.
- Row m has m + 1 entries, so a(n) costs about 4n² big-integer additions.
  The whole b-file (189 terms) prints in well under a second; the program
  stops after a(672), when the next term passes the 4300-digit int-to-str
  limit of Python 3.11+. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000320), CC BY-SA 4.0.
