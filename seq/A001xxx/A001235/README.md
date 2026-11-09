# A001235

> Taxi-cab numbers: sums of 2 cubes in more than 1 way.
> — [OEIS A001235](https://oeis.org/A001235)

Offset 1: 1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232, 65728, 110656, 110808, 134379, 149389, 165464, …

### Python 3 — 127 bytes

```python
m=0;k=1
while 1:L=sorted(a**3+b**3for b in range(k)for a in range(b+1));[print(m:=x)for x,y in zip(L,L[1:])if m<x==y<k**3];k*=2
```

**How it works**

- Each pass lists every a³ + b³ with 0 ≤ a ≤ b < k and sorts it. A number
  below k³ has all its representations in the list (b³ < k³), so a value
  below k³ that appears twice in a row is a taxicab number.
- Allowing a = 0 adds each cube b³ once, and a cube is never also a sum
  of two positive cubes (Fermat's last theorem for exponent 3, Euler), so
  it cannot make a false repeat.
- `m` is the last number printed: `m<x==y<k**3` prints each new taxicab
  number once (one with three representations repeats twice) and skips
  those an earlier pass printed. Then k doubles.

**Notes**

- A pass holds k²/2 sums, so memory grows fourfold per pass: about 11700
  terms (k = 2048, 2.1 million sums) in 13 s here; the next pass needs
  about 400 MB. The b-file has 30000 terms; the bar is 11000 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 127 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001235), CC BY-SA 4.0.
