# A000184

> Number of genus 0 rooted maps with 3 faces with n vertices.
> — [OEIS A000184](https://oeis.org/A000184)

Offset 2: 2, 22, 164, 1030, 5868, 31388, 160648, 795846, 3845020, 18211380, …

### Python 3 — 48 bytes

```python
v=n=1
while[print((v:=4*v+6*v//n)+~n*4**n)]:n+=1
```

**How it works**

- Greubel's formula on the OEIS page, a(n) = n·(2(2n+1)·C(2n,n) − 3·4^n)/12,
  splits into a(n) = v(n) − n·4^(n−1) with v(n) = n(2n+1)·C(2n,n)/6
  (the coefficient of x^(n−1) in (1−4x)^(−5/2); the g.f. is
  x/(1−4x)^(5/2) − x/(1−4x)^2).
- v(n) is hypergeometric: v(n+1)/v(n) = (4n+6)/n, starting from v(1) = 1.
  Since n divides (4n+6)·v(n), it also divides 6·v(n), so
  v(n+1) = 4v(n) + 6v(n)/n holds with `//`: `4*v+6*v//n` is 2 bytes under
  `v*(4*n+6)//n`.
- The walrus moves v to v(n+1) inside `print`, and the same pass subtracts
  (n+1)·4^n, written `+~n*4**n` because `~n` is −(n+1). With `n` running from
  1 the first line is v(2) − 2·4 = 2 = a(2), so the start is just `v=n=1`.
  Updating `v` in the loop body instead costs 4 more bytes (`v=10;n=1`
  and `v+=3*v+6*v//n` after `n+=1`).

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (499 terms) prints at once; the program stops after a(7133), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000184), CC BY-SA 4.0.
