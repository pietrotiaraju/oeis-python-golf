# A002246

> a(1) = 3; for n > 1, a(n) = 4*phi(n); given a rational number r = p/q, where q>0, (p,q)=1, define its height to be max{|p|,q}; then a(n) = number of rational numbers of height n.
> — [OEIS A002246](https://oeis.org/A002246)

Offset 1: 3, 4, 8, 8, 16, 8, 24, 16, 24, 16, 40, 16, …

### Python 3 — 76 bytes

```python
import math
n=1
while[print(sum(math.gcd(n,k)<2for k in range(1,4*n)))]:n+=1
```

**How it works**

- **Counting the rationals.** A reduced p/q of height n ≥ 2 has either
  q = n and |p| < n coprime to n (2φ(n) choices of p, both signs), or
  |p| = n and q < n coprime to n (2φ(n) more): 4φ(n). Height 1 gives
  0/1, 1/1 and −1/1: 3.
- **One count for both cases.** The program counts the k in 1, …, 4n − 1
  coprime to n. For n ≥ 2 the range 1 … 4n holds four full residue
  systems mod n, and the missing k = 4n is not coprime to n, so the count
  is 4φ(n). For n = 1 it counts 1, 2, 3: exactly 3, with no special case.
- `while[print(…)]:n+=1` prints inside the loop test (a one-element list
  is true), which saves the `n=0` … `n+=1;` of the usual loop.

**Notes**

- Exact integers: right for every n.
- The count takes 4n gcds, so the run is quadratic: 8000 terms come in
  about 32 s here and the whole b-file (10000 terms) in about 51 s. The
  bar is 8000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002246), CC BY-SA 4.0.
