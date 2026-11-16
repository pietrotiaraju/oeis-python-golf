# A001783

> n-phi-torial, or phi-torial of n: Product k, 1 <= k <= n, k relatively
> prime to n.
> — [OEIS A001783](https://oeis.org/A001783)

Offset 1: 1, 1, 2, 3, 24, 5, 720, 105, 2240, 189, 3628800, 385, 479001600, …

### Python 3 — 81 bytes

```python
from math import*
n=1
while[print(prod(k for k in range(1,n)if gcd(k,n)<2))]:n+=1
```

**How it works**

- The definition, term by term: `prod` multiplies the k with gcd(k, n) = 1.
- k = n itself is coprime to n only for n = 1, so `range(1,n)` loses
  nothing: for n = 1 the empty product is 1, which is a(1). `range(n)`
  would let k = 0 in at n = 1 (gcd(0, 1) = 1) and print 0.
- `while[print(…)]:n+=1` prints a(n) before moving to n + 1; the list is
  non-empty, so the loop never ends.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The
  b-file (200 terms) prints in 0.1 s; the bar is the whole b-file in 60 s.
- At a prime n the term is (n − 1)!; a(1567) has 4325 digits, past
  Python's 4300-digit int-to-str limit, which stops the program there (an
  interpreter limit, not a wrong term).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001783), CC BY-SA 4.0.
