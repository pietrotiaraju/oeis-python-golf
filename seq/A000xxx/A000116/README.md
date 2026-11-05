# A000116

> Number of even sequences with period 2n (bisection of A000013).
> — [OEIS A000116](https://oeis.org/A000116)

Offset 0: 1, 2, 4, 8, 20, 56, 180, 596, 2068, 7316, 26272, 95420, 349716, 1290872, …

### Python 3 — 92 bytes

```python
import math
n=1
while[print(sum(1<<(g:=math.gcd(j,n))-n//g%2for j in range(n))//n)]:n+=2-n%2
```

**How it works**

a(n) is [A000013](../A000013/)(2n), the number of binary necklaces of
length 2n where the two colours may be swapped, so this is the A000013
program run on even lengths only.

- Burnside's lemma over the 2N symmetries of a necklace of length N: the N
  rotations, each with or without complementing every bead. Rotation by j
  splits the beads into g = gcd(j, N) cycles of length N/g and fixes 2^g
  strings; with the complement each cycle has to alternate, which fixes
  2^g strings when N/g is even and none when it is odd.
- Half of what the two symmetries for j fix is 2^g, or 2^(g−1) when N/g is
  odd: `1<<g-n//g%2`. Subtracting the parity in the exponent is a byte
  shorter than A000013's `1<<g>>n//g%2`. Summing over j and dividing by N
  gives the average over all 2N symmetries, the OEIS formula
  Σ φ(2d)·2^(2n/d) / (4n) over d | 2n.
- The walrus assigns `g` before `n//g` is evaluated, since Python reads
  the left operand of `-` first.
- a(0) = 1 would divide by zero at N = 0, but A000013(1) is also 1, so the
  loop starts at N = 1 and then steps through 2, 4, 6, …: `n+=2-n%2`
  adds 1 to an odd `n` and 2 to an even one.
- `%2for` raises a `SyntaxWarning` on stderr, which the rules allow.

**Notes**

- `n=n+2&-2` and `n-=n%2-2` are the same length as `n+=2-n%2`; starting at
  N = 0 and special-casing it (`if n else 1`) costs more.
- `for g in map(math.gcd,range(n),[n]*n)` instead of the walrus is 2 bytes
  longer.
- a(n) ~ 4^(n−1)/n, so a(1000) has about 600 digits, far below Python's
  4300-digit `str` limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000116), CC BY-SA 4.0.
