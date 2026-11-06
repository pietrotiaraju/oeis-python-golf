# A000365

> Number of genus 0 rooted planar maps with 4 faces and n vertices.
> — [OEIS A000365](https://oeis.org/A000365)

Offset 3: 5, 93, 1030, 8885, 65954, 442610, 2762412, 16322085, 92400330, 505403910, 2687477780, …

### Python 3 — 78 bytes

```python
n=3;c=20
while[print(n*~-n*((8*n+11<<2*n-3)-(4*n+1)*c)//24)]:n+=1;c=4*c-2*c//n
```

**How it works**

- The program prints the closed form

  a(n) = n(n−1)·((8n+11)·2^(2n−3) − (4n+1)·C(2n, n))/24,

  with `c` = C(2n, n) stepped by `c=4*c-2*c//n`, the split of
  c·(4n−2)/n into two pieces. The division is exact:
  2·C(2n−2, n−1)/n = 4·C(2n−2, n−1) − C(2n, n) is an integer.
- `8*n+11<<2*n-3` is (8n+11)·2^(2n−3): `<<` binds more loosely than `+`
  and `-`, so it needs no inner parentheses.

**Why the closed form holds**

- The OEIS gives the g.f. x²(1−s)(7+4x−2s)/(2(1−4x)⁴) with
  s = √(1−4x) (Walsh and Lehman, offset as corrected by V. Kotesovec).
  Since (1−s)(7+4x−2s) = (9−4x) − (9+4x)·s, it splits into a rational part
  x²(9−4x)/(2(1−4x)⁴) and an algebraic part −x²(9+4x)/(2(1−4x)^(7/2)).
- With m = n − 2, the rational part contributes
  4^m·(9·C(m+3, 3) − C(m+2, 3))/2 = 4^m·(m+1)(m+2)(8m+27)/12.
- With c(m) = [x^m] (1−4x)^(−7/2) = C(2m+6, m+3)·C(m+3, 3)/20 and
  c(m−1) = c(m)·m/(4m+10), the algebraic part contributes
  −(9c(m) + 4c(m−1))/2 = −5c(m)(4m+9)/(2(2m+5)), which is
  −(m+1)(m+2)(4m+9)·C(2m+4, m+2)/24 because
  C(2m+6, m+3)·(m+3)/(2m+5) = 2·C(2m+4, m+2).
- Adding the two and putting m = n − 2 gives the formula above. It is an
  identity of exact rational numbers, so the program is right for every n.

**Notes**

- `math.comb(2*n,n)` instead of the running `c` is 88 bytes with the
  import. The OEIS data also fit a recurrence of order 2 with quartic
  coefficients, which is much longer.
- The formula gives 0 at n = 1 and n = 2, so the loop starts at n = 3
  with C(6, 3) = 20.
- a(7126) is the first term with more than 4300 digits, so Python 3.11+
  stops there with a `ValueError` from the int-to-str limit, which is not
  counted as a failure.
- The b-file has 198 terms (n = 3 to 200); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000365), CC BY-SA 4.0.
