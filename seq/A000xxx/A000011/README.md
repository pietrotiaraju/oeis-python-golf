# A000011

> Number of n-bead necklaces (turning over is allowed) where complements are
> equivalent.
> — [OEIS A000011](https://oeis.org/A000011)

Offset 0: 1, 1, 2, 2, 4, 4, 8, 9, 18, 23, 44, 63, 122, 190, 362, 612, …

### Python 3 — 111 bytes

```python
import math
n=1;k=0
while[print(sum((2-n//(g:=math.gcd(j,n))%2<<g)+(2<<n//2)for j in range(n))//4//n)]:n+=k;k=1
```

**How it works**

Burnside's lemma over the 4n symmetries (rotations, reflections, each with or
without complementing every bead): a(n) is the average number of strings each
symmetry fixes.

- Rotation by j splits the beads into g = gcd(j, n) cycles of length n/g, so
  it fixes 2^g strings. Rotation plus complement needs every cycle to
  alternate, which works only when n/g is even, and then it also fixes 2^g.
  Together: (2 − (n/g mod 2))·2^g, written `2-n//g%2<<g`.
- The n reflections fix n·2^(n/2+1) strings in all, for odd and even n alike
  (with complement, only the n/2 reflections through edges fix anything, when
  n is even). That is `2<<n//2` added once per j.
- The total is divided by 4n with `//4//n`. This is the OEIS formula
  a(n) = (A000013(n) + 2^⌊n/2⌋)/2 with A000013 expanded.
- n = 0 would divide by zero, but a(0) = a(1) = 1, so the loop simply prints
  n = 1 twice: `k` is 0 on the first pass, then 1.

**Notes**

- `print(1);n=1` with `n+=1` is one byte longer; `print(n:=1)` with `n+=1`
  ties.
- Counting canonical strings directly (each n-bit string compared with all
  its rotations, reversals and complements) is 156 bytes and exponential.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 112 | first entry |
| 2026-11-05 | Python 3 | 111 | `import math` instead of `from math import*` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000011), CC BY-SA 4.0.
