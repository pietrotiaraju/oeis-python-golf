# A001831

> Number of labeled graded partially ordered sets with n elements of height at most 1.
> — [OEIS A001831](https://oeis.org/A001831)

Offset 0: 1, 1, 3, 13, 87, 841, 11643, 227893, 6285807, 243593041, 13262556723, …

### Python 3 — 89 bytes

```python
import math
n=0
while[print(sum(math.comb(n,k)*(2**k-1)**(n-k)for k in range(n+1)))]:n+=1
```

**How it works**

- **Height at most 1.** In a poset whose chains have at most two elements,
  every element is minimal or lies above minimal elements only, so ranking
  the minimal elements 0 and the others 1 grades it: these are all the
  labeled posets of height ≤ 1. Such a poset is fixed by its set M of
  minimal elements and, for each other element, the nonempty set of
  elements of M below it. With |M| = k that gives
  a(n) = Σₖ C(n, k)·(2ᵏ − 1)ⁿ⁻ᵏ, Vladeta Jovovic's formula on the OEIS
  page. The k = 0 term is 0ⁿ, which Python evaluates as 1 for n = 0.
- **The program.** That sum, one term per line. `import math` with a single
  `math.comb` is 1 byte under `from math import*`.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 238.
- The b-file has 51 terms (n = 0 to 50); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001831), CC BY-SA 4.0.
