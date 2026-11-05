# A000015

> Smallest prime power >= n.
> — [OEIS A000015](https://oeis.org/A000015)

Offset 1: 1, 2, 3, 4, 5, 7, 7, 8, 9, 11, 11, 13, 13, 16, 16, 16, 17, 19, …

1 counts as a prime power (p⁰).

### Python 3 — 83 bytes

```python
from math import*
n=m=L=1
while[print(m)]:
 n+=1
 while L%m<1or m<n:L=lcm(L,m);m+=1
```

**How it works**

- `m` is the current answer. It only moves when it falls behind n, and then
  it walks forward to the next prime power.
- `L` is lcm(1, …, m−1). A number m ≥ 2 that is not a prime power splits as
  a·b with a, b > 1 coprime and both below m, so m divides `L`. A prime
  power pᵏ does not: `L` holds only pᵏ⁻¹. So `L%m<1` means "not a prime
  power".
- The inner loop adds m to the lcm before stepping past it, which keeps
  `L` equal to lcm(1, …, m−1) at every test.
- a(1) = 1 is printed from the start values, so m = 1 is never tested.
- `1or` raises a `SyntaxWarning` on stderr, which the rules allow.

**Notes**

- `L` has about 1.44·m bits, which is no burden: the program prints about
  300 000 terms a minute.
- Without the import, testing m with
  `any(m%d<1<=d**m%m for d in range(2,m))` (some divisor d whose powers are
  not divisible by m) is 85 bytes and about 30 000 terms a minute. The shorter
  `any(d**m%m>m%d*m for d in range(2,m))` is 84 bytes, but it raises every d
  to the m-th power and misses the bar (about 2 600 terms a minute).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000015), CC BY-SA 4.0.
