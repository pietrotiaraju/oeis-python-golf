# A000117

> Number of even sequences with period 2n (bisection of A000011).
> — [OEIS A000117](https://oeis.org/A000117)

Offset 0: 1, 2, 4, 8, 18, 44, 122, 362, 1162, 3914, 13648, 48734, 176906, 649532, …

a(n) = [A000011](../A000011/)(2n): binary necklaces of 2n beads where turning
over is allowed and a necklace counts the same as its complement.

### Python 3 — 107 bytes

```python
import math
k=1
while[print(sum((2-k//(g:=math.gcd(j,k))%2<<g)+(2<<k//2)for j in range(k))//4//k)]:k+=2-k%2
```

**How it works**

The sum is the [A000011](../A000011/) program, evaluated at k beads.

Burnside's lemma over the 4k symmetries (rotations, reflections, each with or
without complementing every bead): A000011(k) is the average number of strings
each symmetry fixes.

- Rotation by j splits the beads into g = gcd(j, k) cycles of length k/g, so
  it fixes 2^g strings. Rotation plus complement needs every cycle to
  alternate, which works only when k/g is even, and then it also fixes 2^g.
  Together: (2 − (k/g mod 2))·2^g, written `2-k//g%2<<g`.
- The k reflections fix k·2^(⌊k/2⌋+1) strings in all, with or without
  complement. That is `2<<k//2` added once per j.
- `//4//k` divides by the 4k symmetries.
- **Order of k.** k runs 1, 2, 4, 6, 8, … through `k+=2-k%2`. The even values
  give a(n) = A000011(2n) for n ≥ 1. The first value k = 1 stands in for
  n = 0: A000011(1) = 1 = a(0), so the program never divides by zero and
  needs no separate `print(1)`.

**Notes**

- Correct for every n: it is Burnside's lemma, in exact integer arithmetic.
  This is the OEIS formula a(n) = (A000013(2n) + 2ⁿ)/2 with A000013 expanded.
- The b-file has 501 terms (n = 0 to 500); they print in about 0.1 s. The bar
  is the whole b-file in 60 s.
- Other ways to get a(0) = 1 cost more: `k=2;print(1)` with `k+=2` is
  112 bytes, and starting at k = 0 with `-~sum(…)//(k*4or 1)` is 110.
  `k=k+2&-2` ties with `k+=2-k%2`. Writing the rotation term as
  `1<<g+~k//g%2` (~k//g has the opposite parity of k/g) is 1 byte longer.
  So is adding the reflections once, as `+(1<<~-k//2)` = 2^(⌈k/2⌉−1) after
  the division: the parentheses around the rotation term go, but `<<g for`
  then needs a space.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000117), CC BY-SA 4.0.
