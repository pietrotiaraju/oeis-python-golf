# A002101

> Nearest integer to 4 * Pi * n^3 / 3.
> — [OEIS A002101](https://oeis.org/A002101)

Offset 0: 0, 4, 34, 113, 268, 524, 905, 1437, 2145, 3054, 4189, 5575, 7238, 9203, …

### Python 3 — 101 bytes

```python
t=l=3;q=z=16;n=0
while z*n**3//t<(a:=(z+q)*n**3//t)or[print(a+1>>1),n:=n+1]:q*=l//2;z=z*l+q;t*=l;l+=2
```

**How it works**

- **A shrinking interval around π.** The state is the halved form of
  Gibbons' spigot used for ⌊πⁿ⌋ in [A001672](../../A001xxx/A001672/):
  π = 2u, u = 1 + 1/3·(1 + 2/5·(1 + 3/7·(1 + …))), each tail lying in
  [1, 2]. Here the start is scaled by 8/3: q = z = 16, t = 3 puts 8π/3 in
  [z/t, (z+q)/t] = [16/3, 32/3], and the linear updates keep the scale.
  Taking in the k-th term (l = 2k + 1) is `q*=l//2;z=z*l+q;t*=l`, which
  multiplies the width q/t by k/(2k+1) < ½; starting `l` at 3 and stepping
  it last saves the usual `t=l=1`.
- **Rounding.** With X = 4πn³/3, round(X) = ⌊X + ½⌋ = (⌊2X⌋ + 1) div 2, and
  2X = 8πn³/3 lies in [z·n³/t, (z+q)·n³/t]. When both ends have the same
  integer part a, so does 2X, and the program prints `a+1>>1` and steps n;
  otherwise it takes in another term of the series and tries again.
- **Every n.** For n ≥ 1, 8πn³/3 is irrational, so it is not an integer
  and the narrowing interval eventually has both ends between the same two
  integers (no ties either: X + ½ is never an integer). For n = 0 both ends
  are 0 at once. Every printed value is certified by exact integer bounds.

**Notes**

- Comparing the rounded ends, `z*n**3//t+1>>1<(a:=…+1>>1)`, is five bytes
  longer, and a lambda for the two ends saves nothing.
- The interval only narrows as far as needed (about 40 bits for n = 1000),
  so the whole b-file (1001 terms, n = 0 to 1000) comes in a fraction of a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 101 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002101), CC BY-SA 4.0.
