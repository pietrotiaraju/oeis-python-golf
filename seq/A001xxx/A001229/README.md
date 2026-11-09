# A001229

> Numbers k such that phi(sigma(k)) = k.
> — [OEIS A001229](https://oeis.org/A001229)

Offset 1: 1, 2, 8, 12, 128, 240, 720, 6912, 32768, 142560, 712800, 1140480, 1190400, 3345408, 3571200, 5702400, 14859936, …

### Python 3 — 115 bytes

```python
import math
r=[1]
for n in r:r+=n+1,;s=sum(d*(n%d<1)for d in r);sum(math.gcd(j,s)<2for j in range(s))-n or print(n)
```

**How it works**

- A direct search over every k: compute s = σ(k) and print k when
  φ(s) = k. No property of the solutions is assumed, so it is right for
  every n.
- `r` is the queue `[1, 2, …]`. The loop reads it while appending to it,
  so `for n in r:` runs forever. When n is handled, `r` holds 1, …, n+1,
  and `sum(d*(n%d<1)for d in r)` is σ(n). The extra entry n + 1 never
  divides n.
- φ(s) counts the j in [0, s) with gcd(j, s) = 1. For s = 1 that is
  j = 0, since gcd(0, 1) = 1, so 1 is a term. `…-n or print(n)` prints
  exactly when the count equals n.

**Notes**

- A candidate k costs about k + σ(k) steps, so the time grows like the
  square of the terms. 6912 comes in about 16 s here, and 32768 would
  take some 20 times longer. The bar is 8 terms in 60 s. The b-file has
  30 terms, up to 665725132800.
- Those 8 terms fit in a table shorter than the program, so it needs a
  review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 115 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001229), CC BY-SA 4.0.
