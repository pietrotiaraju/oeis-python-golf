# A000208

> Number of even sequences with period 2n.
> — [OEIS A000208](https://oeis.org/A000208)

Offset 0: 1, 1, 3, 4, 12, 28, 94, 298, 1044, 3658, …

### Python 3 — 107 bytes

```python
import math
x=n=1
while[print(x)]:x=sum(1<<(g:=math.gcd(k,2*n))+(2>>n%2+n%g)for k in range(2*n))//8//n;n+=1
```

**How it works**

- a(n) counts binary words of length 2n with an even number of 1s, up to
  rotation and swapping 0 ↔ 1 (Gilbert and Riordan). Burnside's lemma over the
  group Z<sub>2n</sub> × Z<sub>2</sub> of order 4n gives a(n) = (1/4n) Σ fix.
- Rotation by k splits the 2n positions into g = gcd(k, 2n) cycles of length
  L = 2n/g.
  - Rotation alone: a fixed word is constant on each cycle, so there are 2<sup>g</sup>
    of them, with L·(number of 1-cycles) ones. All of them are even when L is
    even, and half of them when L is odd: 2<sup>g−1</sup>(1 + [L even]).
  - Rotation and swap: each cycle must alternate, so L must be even, and then
    there are 2<sup>g</sup> fixed words, each with exactly g·L/2 = n ones. They count
    only when n is even.
- L is even exactly when g | n. Adding both halves,
  8n·a(n) = Σ<sub>k&lt;2n</sub> 2<sup>g+e</sup> with e = 0 if g ∤ n, 1 if g | n and n is odd,
  2 if g | n and n is even.
- e is `2>>n%2+n%g`. When g ∤ n the shift is at least 2: for odd n because
  n%2 = 1 and n%g ≥ 1; for even n because g | 2n but g ∤ n forces
  v<sub>2</sub>(g) = v<sub>2</sub>(n) + 1, so 2<sup>v<sub>2</sub>(n)</sup> ≥ 2 divides n, g and therefore the
  nonzero remainder n%g. Three bytes under `(n%g<1)*(2-n%2)`.
- The formula divides by n, so a(0) = 1 (the empty word) cannot come out of
  it. The loop prints `x` before computing the next term, and `x` starts at 1:
  5 bytes, against 8 for `0**n or`.

**Notes**

- Exact integers and a direct Burnside count, so it is correct for every n.
  It agrees with the OEIS formula a(n) = (A000013(2n) + [n even]·A000013(n))/2.
- a(n) has about 0.6n digits, so Python's 4300-digit int-to-str limit stops
  the output near n = 7140; that is an interpreter limit, not a failure.
- About 3400 terms in 15 s here. The bar is the whole b-file (n ≤ 1000) in 60 s.
- `from math import*` with a bare `gcd` is one byte longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000208), CC BY-SA 4.0.
