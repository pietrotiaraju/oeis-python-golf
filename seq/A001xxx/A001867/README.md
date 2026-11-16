# A001867

> Number of n-bead necklaces with 3 colors.
> — [OEIS A001867](https://oeis.org/A001867)

Offset 0: 1, 3, 6, 11, 24, 51, 130, 315, 834, 2195, 5934, 16107, 44368, …

### Python 3 — 82 bytes

```python
import math
x=n=1
while[print(x)]:x=sum(3**math.gcd(j,n)for j in range(n))//n;n+=1
```

**How it works**

Burnside's lemma over the n rotations.

- Rotation by j splits the n beads into gcd(j, n) cycles, and a coloring is
  fixed by it exactly when each cycle has one color, so it fixes
  3^gcd(j, n) colorings. Summing over j = 0…n−1 and dividing by n gives the
  number of orbits, that is, of necklaces.
- This is the OEIS formula Σ φ(d)·3^(n/d) / n over d | n, with the divisor
  sum rewritten as a sum over j: φ(d) values of j have gcd(j, n) = n/d.
- `x=n=1` holds a(0) = 1 for the first print; each pass then computes
  a(n) into `x` and steps n, so the division by n only ever sees n ≥ 1. This
  is 2 bytes under printing a(0) apart with `print(n:=1)` and putting the
  sum inside the header's `print`.
- `gcd` is used once, so `import math` and `math.gcd` are a byte shorter
  than `from math import*` and `gcd`.
- The same Burnside sum with base 2 is [A000031](../../A000xxx/A000031/); the
  other bases of this family are [A001868](../A001868/) and [A001869](../A001869/).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes well under a second.
- a(9021) is the first term with more than 4300 digits, so Python 3.11+
  stops there with a `ValueError` from the int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001867), CC BY-SA 4.0.
