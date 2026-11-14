# A001728

> Expansion of cos x / cos 4x.
> — [OEIS A001728](https://oeis.org/A001728)

Offset 0: 1, 15, 1185, 230895, 83860545, 48942778575, 41893214676705, …

### Python 3 — 75 bytes

```python
r=[s:=1]
while[print(s)]:
 for s in 0,-r[0]:r=[s:=s+x*4for x in[0]+r[::-1]]
```

**How it works**

- a(n) = (2n)!·[x^(2n)] cos x·sec 4x. As in [A000281](../../A000xxx/A000281/)
  (cos x / cos 2x) and [A000436](../../A000xxx/A000436/), it comes from a
  weighted Seidel–Entringer (boustrophedon) triangle: T(m,0) = u_m and
  T(m,k) = T(m,k−1) + c·T(m−1,m−k). Then B_m = T(m,m) has e.g.f.
  (sec cx + tan cx)·U(x), where U is the e.g.f. of u.
- Here c = 4 and U = cos x (u_(2n) = (−1)ⁿ, odd u = 0). U is even, so the
  even part of the output is sec 4x·cos x and T(2n,2n) = a(n); the odd
  rows only carry the sums.
- Each row is a running sum over the previous row read backwards, with a
  `[0]` in front, so it starts at s, the `for` target: 0 for the odd row,
  −r[0] for the even row. The tuple `0,-r[0]` is built before either row,
  while r is still the previous even row, whose first entry is
  u_(2n−2); that gives u_(2n) = −u_(2n−2) with no counter or sign
  variable.
- After the even row, s is T(2n,2n) = a(n), which the next header prints.
  It starts from row 0 = [1], with s = a(0) = 1.

**Notes**

- Exact integers, so the program is right for every n. Row m has m+1
  entries, so a(n) costs about 2n² big-integer additions; the 51 terms of
  the b-file print in well under a second. The bar is the whole b-file in
  60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(690) (4296 digits); a(691) has 4304.
- The weight −2 trick of A000281 (an `[s]` in front, so the row starts at
  s − 2s = −s) does not carry over: with weight −4 the row would start at
  −3s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001728), CC BY-SA 4.0.
