# A000024

> Number of positive integers <= 2^n of form x^2 + 10 y^2.
> — [OEIS A000024](https://oeis.org/A000024)

Offset 0: 1, 1, 2, 2, 7, 10, 20, 36, 65, 118, 221, 409, 776, 1463, 2788, …

### Python 3 — 101 bytes

```python
n=0
while[print(len([r:=range(2<<n//2)]and{v for x in r for y in r if(v:=x*x+10*y*y)<=2**n})-1)]:n+=1
```

**How it works**

The same program as [A000018](../A000018/) and [A000021](../A000021/), with
10 as the coefficient:

- Signs do not matter, so x, y ≥ 0. Any value up to 2ⁿ has x, y ≤ 2^(n/2),
  and `range(2<<n//2)` goes past that bound for every n, so one range
  serves both variables.
- A walrus may not appear in a comprehension's iterable, so
  `[r:=range(2<<n//2)]and{…}` names the range in a one-element list just
  before the set. The list is truthy, so `and` returns the set. Writing
  the range once is 2 bytes shorter than two separate ranges, at the cost
  of twice the pairs.
- The set comprehension keeps each value ≤ 2ⁿ once, however many ways it can
  be written. The walrus in the condition names the value so it is computed
  only once.
- 0 = 0² + 10·0² is always in the set and is not positive, so `-1` removes
  it (shorter than testing `0<v`).

**Notes**

- Term n costs about 2ⁿ⁺¹ pairs and the set grows to a(n) elements, so the
  program prints a(0)…a(23) in about 18 s and a(24) at about 42 s. The bar
  is 24 terms in 60 s; the b-file goes to n = 36.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 103 | first entry |
| 2026-11-05 | Python 3 | 101 | one range for x and y, named by a walrus before the set |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000024), CC BY-SA 4.0.
