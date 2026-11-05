# A000024

> Number of positive integers <= 2^n of form x^2 + 10 y^2.
> — [OEIS A000024](https://oeis.org/A000024)

Offset 0: 1, 1, 2, 2, 7, 10, 20, 36, 65, 118, 221, 409, 776, 1463, 2788, …

### Python 3 — 103 bytes

```python
n=0
while[print(len({v for x in range(2<<n//2)for y in range(1<<n//2)if(v:=x*x+10*y*y)<=2**n})-1)]:n+=1
```

**How it works**

The same program as [A000018](../A000018/) and [A000021](../A000021/), with
10 as the coefficient:

- Signs do not matter, so x, y ≥ 0. Any value up to 2ⁿ has x ≤ 2^(n/2) and
  y ≤ 2^(n/2)/√10, and `2<<n//2` and `1<<n//2` are above those bounds for
  every n.
- The set comprehension keeps each value ≤ 2ⁿ once, however many ways it can
  be written. The walrus in the condition names the value so it is computed
  only once.
- 0 = 0² + 10·0² is always in the set and is not positive, so `-1` removes
  it (shorter than testing `0<v`).

**Notes**

- Term n costs about 2ⁿ pairs, so the program prints a(0)…a(25) in a minute.
  The bar is 24 terms in 60 s; the b-file goes to n = 36.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000024), CC BY-SA 4.0.
