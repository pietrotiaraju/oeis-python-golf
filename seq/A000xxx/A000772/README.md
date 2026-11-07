# A000772

> E.g.f. exp(tan(x) + sec(x) - 1).
> — [OEIS A000772](https://oeis.org/A000772)

Offset 0: 1, 1, 2, 6, 23, 107, 583, 3633, 25444, 197620, 1684295, 15618141, 156453857, 1683050189, 19344093070, …

### Python 3 — 83 bytes

```python
s=a=1;R=[],[]
while[print(a)]:R=[[s:=s+x for x in[0]+r[::-1]]for r in R];s=a=a+s>>1
```

**How it works**

- Let f = sec x + tan x, the e.g.f. of the Euler zigzag numbers
  [A000111](../A000111/), and A = exp(f − 1). Since 1 + tan² x = sec² x,
  f′ = sec x·f = (1 + f²)/2, so A′ = f′·A = (A + f·(f·A))/2:
  a(n+1) = (a(n) + k(n))/2, where k is the boustrophedon transform of the
  boustrophedon transform of a.
- Multiplying an e.g.f. by f is the boustrophedon transform: in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young) the last entry of row n is the n-th term of f·U. Row n needs only
  u(n), so both triangles run as a stream: a(n) starts row n of the first,
  whose last entry h(n) starts row n of the second, whose last entry is
  k(n).
- `R=[[…]for r in R]` builds both new rows with one walrus sum `s`: it
  starts at a(n), and the leading `[0]` keeps it as the first entry of the
  first row; it ends that row at h(n), which the next `[0]` makes the first
  entry of the second row; it ends at k(n). Then `s=a=a+s>>1` is a(n+1),
  exactly, and also the start of the next pass.

**Notes**

- This is the ODE behind Peter Bala's formula a(n) = Dⁿ(eˣ) at x = 0 with
  D = (1 + x + x²/2)·d/dx: y = f − 1 satisfies y′ = 1 + y + y²/2.
- The values were checked for every printed term against the exponential
  formula a(n+1) = Σₖ C(n,k)·E(k+1)·a(n−k), with E = [A000111](../A000111/).
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1648); the 1648 terms
  before it print in about three seconds.
- The b-file has 479 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000772), CC BY-SA 4.0.
