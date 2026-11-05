# A000031

> Number of n-bead necklaces with 2 colors when turning over is not allowed;
> also number of output sequences from a simple n-stage cycling shift
> register; also number of binary irreducible polynomials whose degree
> divides n.
> — [OEIS A000031](https://oeis.org/A000031)

Offset 0: 1, 2, 3, 4, 6, 8, 14, 20, 36, 60, 108, 188, 352, 632, 1182, 2192, …

### Python 3 — 84 bytes

```python
import math
print(n:=1)
while[print(sum(2**math.gcd(j,n)for j in range(n))//n)]:n+=1
```

**How it works**

Burnside's lemma over the n rotations.

- Rotation by j splits the beads into gcd(j, n) cycles, so it fixes
  2^gcd(j, n) strings. Summing over j = 0…n−1 and dividing by n gives the
  number of necklaces.
- This is the OEIS formula Σ φ(d)·2^(n/d) / n over d | n, with the divisor
  sum rewritten as a sum over j: φ(d) values of j have gcd(j, n) = n/d.
- a(0) = 1 but a(1) = 2, so the trick of [A000013](../A000013/) (printing
  n = 1 twice) does not work here. `print(n:=1)` prints a(0) and starts the
  loop at n = 1. With the `n+=1` it costs 17 bytes, the same as that trick's
  `n=1;k=0` and `n+=k;k=1`.
- `gcd` is used once, so `import math` and `math.gcd` are a byte shorter
  than `from math import*` and `gcd`.

**Notes**

- The whole b-file (3334 terms) takes about 1.5 s.
- a(14299) is the first term with more than 4300 digits, so Python 3.11+
  stops there with a `ValueError` from the int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000031), CC BY-SA 4.0.
