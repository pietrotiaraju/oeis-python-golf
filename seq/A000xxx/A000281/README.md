# A000281

> Expansion of cos(x)/cos(2x).
> — [OEIS A000281](https://oeis.org/A000281)

Offset 0: 1, 3, 57, 2763, 250737, 36581523, 7828053417, …

### Python 3 — 75 bytes

```python
r=[s:=1]
while[print(s)]:
 for s in 0,r[0]:r=[s:=s-2*x for x in[s]+r[::-1]]
```

**How it works**

- a(n) = (2n)!·[x^(2n)] cos x·sec 2x. This is Shanks' c(2,n), so it fits
  the weighted Seidel–Entringer (boustrophedon) triangle used for
  [A000187](../A000187/) and [A000191](../A000191/): T(m,0) = u_m and
  T(m,k) = T(m,k−1) + c·T(m−1,m−k). Then B_m = T(m,m) has e.g.f.
  (sec cx + tan cx)·U(x), where U is the e.g.f. of u.
- With c = 2 and U = cos x (u_(2n) = (−1)ⁿ, odd u = 0), U is even, so the
  even part of the output is sec 2x·cos x and T(2n,2n) = a(n). The odd
  rows only carry the sums.
- The program uses c = −2. If T′ is the weight −2 triangle, then
  (−1)^m·T′(m,k) satisfies the weight 2 recurrence, so even rows come out
  the same and odd rows only change sign. a(n) is still the last entry of
  row 2n.
- The weight −2 version is shorter. Each row is a running sum over the
  previous row read backwards, with an extra `[s]` in front. The first
  entry is then s − 2s = −s, where s is the `for` target. So the odd row
  starts at −0 = 0, and the even row starts at −r[0]. The tuple `0,r[0]`
  is built before either row, while `r` is still the previous even row,
  whose first entry is u_(2n−2). That gives u_(2n) = −u_(2n−2) with no
  counter, no sign variable and no minus in the tuple (1 B under
  `0,-r[0]` with weight 2 and a `[0]` prefix).
- The walrus carries the running sum. After the even row, `s` is a(n),
  which the next `while` header prints. It starts from row 0 = [1], with
  s = a(0) = 1.

**Notes**

- Row m has m+1 entries, so a(n) costs about 2n² big-integer additions.
  The whole b-file (216 terms) prints in well under a second; the bar is
  the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(754) (4299 digits); a(755) has 4305.
- A triangle built from Somos's continued fraction, with factors
  h_j = 4j² − (j mod 2) (Bala, in the OEIS entry), needs the index j
  and comes out longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000281), CC BY-SA 4.0.
