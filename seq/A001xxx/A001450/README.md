# A001450

> a(n) = binomial(5*n,2*n).
> — [OEIS A001450](https://oeis.org/A001450)

Offset 0: 1, 10, 210, 5005, 125970, 3268760, 86493225, 2319959400, …

### Python 3 — 53 bytes

```python
import math
n=0
while[print(math.comb(5*n,2*n))]:n+=1
```

**How it works**

- `math.comb(5*n,2*n)` is the binomial coefficient C(5n, 2n), computed
  exactly with Python's integers, so the program is right for every n.
- `print(…)` runs in the loop condition: it returns `None`, `[None]` is a
  non-empty list and so always true, and the body steps n, as in
  [A000027](../../A000xxx/A000027/).
- With a single use of `comb`, `import math` + `math.comb` is one byte
  shorter than `from math import*` + `comb`.

**Notes**

- Without the import, C(k, 2k/5) for k = 5n is a digit of (2^k + 1)^k in
  base 2^k: every coefficient of (1 + x)^k is below 2^k for k ≥ 1, so there
  are no carries, and `k=0` / `while[print((2**k+1)**k>>k*k*2//5&2**k-1)]:k+=5`
  is 51 bytes. It fails at n = 0 only, where the base 2^0 = 1 has no room
  for the coefficient 1; mending that with `|0**k` makes it 56 bytes.
- A running product a(n+1) = a(n)·(5n+1)⋯(5n+5)/((2n+1)(2n+2)(3n+1)(3n+2)(3n+3))
  is far longer than the import.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001450), CC BY-SA 4.0.
