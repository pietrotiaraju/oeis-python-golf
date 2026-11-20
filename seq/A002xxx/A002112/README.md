# A002112

> Glaisher's H numbers.
> — [OEIS A002112](https://oeis.org/A002112)

Offset 1: 3, 33, 903, 46113, 3784503, 455538993, 75603118503, 16546026500673, …

### Python 3 — 87 bytes

```python
r=[s:=1]
while 1:
 for s in 0,-r[0]:r=[s:=s+x*3for x in[0]+r[::-1]]
 print(3*s>>len(r))
```

**How it works**

- **Triangle.** The loop is the program of [A000436](../A000436/), a
  weighted boustrophedon triangle T(m, 0) = u_m,
  T(m, k) = T(m, k−1) + 3·T(m−1, m−k), whose diagonal has e.g.f.
  (sec 3x + tan 3x)·U(x) (weight c scales row m by c^m). With
  U = cos x (u_(2j) = (−1)^j, u_odd = 0; `-r[0]` flips the sign of the
  last even row's start) the even diagonal is
  s_n = (2n)!·[x^(2n)] sec 3x·cos x = A000436(n), which ends each pass,
  and `r` is then row 2n, of length 2n + 1.
- **Glaisher's H.** H(n) = 3·H′(n), where H′ = [A002114](../A002114/)
  has e.g.f. ½/(2 cos x − 1) = ½·cos(x/2)/cos(3x/2) (from
  cos 3y = cos y·(2 cos 2y − 1)); scaling x by 2 gives
  H′(n) = A000436(n)/2^(2n+1), so H(n) = 3·A000436(n)/2^(2n+1)
  (Deléham's formula in the entry): `3*s>>len(r)`, exact since 2^(2n+1)
  divides s. Printing after the first pass starts at H(1) = 3.

**Notes**

- The b-file has 100 terms (n = 1 to 100), and the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002112), CC BY-SA 4.0.
