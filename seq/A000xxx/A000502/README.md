# A000502

> Number of genus 0 rooted maps with 6 faces and n vertices.
> — [OEIS A000502](https://oeis.org/A000502)

Offset 5: 42, 1586, 31388, 442610, 5030004, 49145460, 429166584, 3435601554, 25658464260, 181055975100, …

### Python 3 — 103 bytes

```python
from math import*
n=5
while[print(comb(n,4)*((64*n*n+432*n+83<<2*n-7)-(n-~n)**2*comb(2*n,n))//30)]:n+=1
```

**How it works**

- Sean A. Irvine's g.f. in the entry is
  x⁴(1 − s)(105 + 92x − (84 + 76x)s)/(1 − 4x)⁷ with s = √(1 − 4x).
  Multiplying out with s² = 1 − 4x turns it into
  x⁴·((189 − 168x − 304x²)/(1 − 4x)⁷ − (189 + 168x)/(1 − 4x)^(13/2)).
- Both pieces expand by the binomial series: [xᵏ](1 − 4x)⁻⁷ = C(k+6, 6)·4ᵏ,
  and [xᵏ](1 − 4x)^(−13/2) is C(2k, k) times a polynomial of degree 6 in k
  over 10395. Collecting the coefficient of xⁿ gives
  a(n) = C(n, 4)·((64n² + 432n + 83)·2^(2n−7) − (2n + 1)²·C(2n, n))/30;
  this agrees with the exact series of the g.f. for n ≤ 40 and with the
  whole b-file.
- `64*n*n+432*n+83<<2*n-7` is the first term (`<<` binds looser than `+`,
  and 2n − 7 ≥ 3 for n ≥ 5); `(n-~n)**2` is (2n + 1)², since
  n − ~n = 2n + 1.
- The `//30` is exact: the quotient is the integer a(n).

**Notes**

- `import math` with `math.comb` twice is 4 bytes longer than
  `from math import*`. The same formula with `while 1:…;n+=1`, `*4**(n-4)`
  and `(2*n+1)**2` is 109 bytes. Stepping m = 2n + 1 instead
  (`comb(m//2,4)*((16*m*m+184*m-117<<m-8)-m*m*comb(m-1,m//2))//30`) ties
  at 103.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 496 terms (up to a(500)); the bar is the whole b-file in
  60 s. All of it prints in 0.1 s here.
- a(7110) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there, after about 37 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 109 | first entry |
| 2026-11-07 | Python 3 | 103 | power of 4 as a shift, `(n-~n)**2`, `while[print(…)]` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000502), CC BY-SA 4.0.
