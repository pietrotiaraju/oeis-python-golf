# A001474

> w such that w^3+x^3+y^3+z^3=0, w>|x|>|y|>|z|, is soluble.
> — [OEIS A001474](https://oeis.org/A001474)

Offset 1: 6, 9, 12, 16, 19, 20, 25, 27, 28, 29, 34, 39, 40, 41, 44, 46, 51, 53, 54, 55, 58, …

### Python 3 — 139 bytes

```python
import math
w=1
while[any(w**3==x**3+y**3+z**3for x in range(w)for y in range(x)if math.gcd(w,x,y)<2for z in range(-y,y))and print(w)]:w+=1
```

**How it works**

- **Primitive solutions only.** The title does not say so, but the data
  counts only solutions with gcd(w, x, y, z) = 1, as the entry's
  Mathematica program does: 18 is missing although 18³ = 15³ + 12³ + 9³
  (three times 6³ = 5³ + 4³ + 3³). A brute-force check of both readings
  against the 65-term b-file (w ≤ 139) confirms the primitive one, and the
  program follows it.
- **The signs.** With w > |x| > |y| > |z|, x must be negative (if x > 0,
  then w³ + x³ + y³ + z³ ≥ w³ + x³ − |y|³ − |z|³ > 0), and then y must be
  negative too (if y > 0, then y³ + z³ > 0 and w³ + x³ > 0). Writing x, y
  for −x, −y and z for −z, the
  condition becomes w³ = x³ + y³ + z³ with w > x > y > |z| ≥ 0 and z of
  either sign; z = 0 is allowed by the title (it never occurs, by Fermat's
  theorem for cubes, but the program does not need that).
- **One gcd for four numbers.** When w³ = x³ + y³ + z³, a prime dividing
  w, x and y has its cube dividing z³, so it divides z: gcd(w, x, y, z) =
  gcd(w, x, y). The program checks `math.gcd(w,x,y)<2` before trying the z.
- **The search.** For each w it tries every x < w, y < x and z from −y to
  y − 1 (z = −y would need w = x), and prints w when one triple works;
  `while[…]:` is always true. Exact integer arithmetic, so it is right for
  every w.

**Notes**

- The cost per w is about w³/3 triples, so up to w the total is about
  w⁴/12; the whole b-file (w ≤ 139) takes about 15 s on a slow PC. The bar
  is the whole b-file (65 terms) in 60 s.
- `import math` with `math.gcd` is one byte shorter than `from math
  import*`. Looking z up in a set of cubes is faster (w² pairs per w) but
  longer, since the set needs the bound |z| < y.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 139 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001474), CC BY-SA 4.0.
