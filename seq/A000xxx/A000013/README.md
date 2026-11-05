# A000013

> Definition (1): Number of n-bead binary necklaces with beads of 2 colors
> where the colors may be swapped but turning over is not allowed.
> — [OEIS A000013](https://oeis.org/A000013)

Offset 0: 1, 1, 2, 2, 4, 4, 8, 10, 20, 30, 56, 94, 180, 316, 596, 1096, …

### Python 3 — 97 bytes

```python
import math
n=1;k=0
while[print(sum(1<<(g:=math.gcd(j,n))>>n//g%2for j in range(n))//n)]:n+=k;k=1
```

**How it works**

Burnside's lemma over the 2n symmetries: the n rotations, each with or
without complementing every bead.

- Rotation by j splits the beads into g = gcd(j, n) cycles of length n/g and
  fixes 2^g strings. With the complement, each cycle has to alternate, so it
  fixes 2^g strings when n/g is even and none when it is odd.
- So the two symmetries for j fix 2·2^g or 2^g strings together, and half of
  that is `1<<g>>n//g%2`: 2^g, shifted right once when n/g is odd.
- Summing over j and dividing by n gives the average over all 2n symmetries.
  This is the OEIS formula Σ φ(2d)·2^(n/d) / (2n) over d | n, with the
  divisor sum rewritten as a sum over j.
- a(0) = a(1) = 1, so the loop prints n = 1 twice instead of dividing by
  zero at n = 0: `k` is 0 on the first pass, then 1 (as in
  [A000011](../A000011/)).
- `%2for` raises a `SyntaxWarning` on stderr, which the rules allow.

**Notes**

- `(2-n//g%2<<g)//2` style terms, as in A000011, cost a byte more.
- A000011 is (A000013(n) + 2^⌊n/2⌋)/2, but writing it from this program is a
  byte longer than its own record.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 98 | first entry |
| 2026-11-05 | Python 3 | 97 | `import math` instead of `from math import*` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000013), CC BY-SA 4.0.
