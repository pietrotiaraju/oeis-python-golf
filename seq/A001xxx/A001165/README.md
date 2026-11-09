# A001165

> Position of first even digit after decimal point in sqrt(n).
> — [OEIS A001165](https://oeis.org/A001165)

Offset 1: 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 1, 1, 2, 1, 3, 1, …

### Python 3 — 79 bytes

```python
import math
n=1
while 1:
 k=1
 while math.isqrt(n*100**k)%2:k+=1
 print(k);n+=1
```

**How it works**

- `math.isqrt(n*100**k)` is ⌊√n·10ᵏ⌋, exact for every n, and its last digit
  is the k-th digit of √n after the decimal point. Only its parity matters,
  so the loop raises k while that number is odd.
- A perfect square has all digits 0, so its term is 1 (a(1) = a(4) = 1).

**Notes**

- For every n the term exists if √n has an even digit at all; no n is known
  for which it does not, and the program would search forever for one.
- The largest term in the b-file is 7 (n = 76); all 1000 terms take well
  under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001165), CC BY-SA 4.0.
