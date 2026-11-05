# A000029

> Number of necklaces with n beads of 2 colors, allowing turning over (these
> are also called bracelets).
> — [OEIS A000029](https://oeis.org/A000029)

Offset 0: 1, 2, 3, 4, 6, 8, 13, 18, 30, 46, 78, 126, 224, 380, 687, 1224, …

### Python 3 — 98 bytes

```python
import math
a=n=1
while[print(a)]:a=sum(2**~-math.gcd(j,n)+2**(n-j%2>>1)for j in range(n))//n;n+=1
```

**How it works**

Burnside's lemma over the 2n symmetries of the dihedral group: the n
rotations x → x + j and the n reflections x → j − x, for j = 0…n−1. a(n) is
the average number of strings each one fixes, so a(n) is the sum over j of
half of what rotation j and reflection j fix together, divided by n.

- Rotation by j splits the beads into gcd(j, n) cycles and fixes
  2^gcd(j, n) strings. Half of that is `2**~-math.gcd(j,n)` (`~-g` is g − 1;
  g ≥ 1, so it never goes negative).
- Reflection j pairs bead x with bead j − x. The beads with 2x ≡ j (mod n)
  stay put: one of them for odd n, two for even n and even j, none for even
  n and odd j. So it fixes 2^((n+1)/2), 2^(n/2+1) or 2^(n/2) strings, and
  half of that is 2^((n − j mod 2) div 2) in all three cases:
  `2**(n-j%2>>1)`.
- The sum is exactly n·a(n), so `//n` is exact. This is the OEIS formula
  Σ φ(d)·2^(n/d)/(2n) over d | n, plus 2^((n−1)/2) for odd n or
  2^(n/2−1) + 2^(n/2−2) for even n, with the divisor sum written as a sum
  over j and the reflection term spread over the n values of j.
- a(0) = 1 but a(1) = 2, so the A000013 trick of printing n = 1 twice does
  not work, and n = 0 would divide by zero. Instead the loop prints the
  previous term: `a=n=1` makes the first line a(0) = 1, then each pass
  computes a(n) into `a` and steps n. `while[print(a)]:` is always true,
  since `[None]` is a non-empty list.
- `gcd` is used once, so `import math` with `math.gcd` is a byte shorter
  than `from math import*` with `gcd`.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The whole
  b-file (301 terms) prints in about 0.1 s; the bar is the whole b-file in
  60 s.
- a(14300) is the first term with more than 4300 digits, so Python 3.11+
  stops there with a `ValueError` from the int-to-str limit.
- Variants that came out longer: `from math import*` with `gcd` is 99
  bytes; printing a(0) with `print(n:=1)` and the term inside `print` is
  100; the reflections as one closed form,
  `sum(2<<math.gcd(j,n)for j in range(n))//n+(3+n%2<<n//2)>>2`, is 99.
- sympy's `necklaces` and `bracelets` only generate the bracelets one by
  one, which is exponential, and `from sympy import*` costs more than
  `import math`, so there is no sympy entry.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000029), CC BY-SA 4.0.
