# A000490

> Generalized Euler numbers c(4,n).
> — [OEIS A000490](https://oeis.org/A000490)

Offset 0: 1, 16, 1280, 249856, 90767360, 52975108096, 45344872202240, 53515555843342336, 83285910482761809920, 165262072909347030040576, …

a(n) = (2n)!·[x^(2n)] sec(4x) (Peter Luschny's formula in the entry), that
is, 16ⁿ times the secant number E₂ₙ of [A000364](../A000364/).

### Python 3 — 71 bytes

```python
r=[t:=1]
while[print(t)]:
 for t in 0,0:r=[t:=t+x*4for x in[0]+r[::-1]]
```

**How it works**

- The program runs a weighted Seidel–Entringer (boustrophedon) triangle:
  T(m,0) = 0 for m ≥ 1, T(0,0) = 1 and T(m,k) = T(m,k−1) + 4·T(m−1,m−k), so
  each row is a running sum over the previous row read backwards. With
  weight 1 its right edge T(m,m) is the zigzag number E_m, with e.g.f.
  sec x + tan x (Millar, Sloane and Young 1996). Every entry of row m has m
  factors of the weight, so with weight 4 the right edge is 4^m·E_m, and the
  even rows give 4^(2n)·E₂ₙ = a(n).
- Each pass of the `while` builds two rows, an odd one and an even one, and
  leaves `t` = T(2n, 2n), which the next pass prints.
- `t` is the `for` target, so it is 0 when the comprehension starts, and
  the extra `[0]` in front of the reversed row produces the leading
  T(m,0) = 0 = t + 4·0. The walrus `t:=t+x*4` then accumulates the row;
  `x*4for` needs no space.
- This is the [A000187](../A000187/) / [A000192](../A000192/) template with
  U(x) = 1, so no starting values have to be injected.

**Notes**

- Other versions that print the same terms: one row per pass storing
  4·T(m,k) so that `[-t]` starts the row,
  `t=1;r=[4]` / `while[len(r)%2and print(t)]:r=[4*(t:=t+x)for x in[-t]+r[::-1]]`,
  72 bytes; the [A000364](../A000364/) program with
  `print(t<<(2*len(r)-2&~2))`, 82 bytes; the convolution
  a(n) = −Σ_{k=1}^{n} C(2n, 2k)·(−16)^k·a(n−k) with `math.comb`, 114 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 195 terms (up to a(194)); the bar is the whole b-file in
  60 s. All of it prints in 0.1 s here.
- a(691) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there, after about 2.5 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 115 | first entry |
| 2026-11-06 | Python 3 | 114 | use a shorter math import |
| 2026-11-07 | Python 3 | 71 | weighted Seidel triangle, two rows per pass |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000490), CC BY-SA 4.0.
