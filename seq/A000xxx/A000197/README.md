# A000197

> a(n) = (n!)!.
> — [OEIS A000197](https://oeis.org/A000197)

Offset 0: 1, 1, 2, 720, 620448401733239439360000, …

### Python 3 — 54 bytes

```python
from math import*
n=0
while[print(perm(perm(n)))]:n+=1
```

**How it works**

- `math.perm` with one argument is the factorial, 4 bytes under
  `factorial`, so the term is just `perm(perm(n))`.
- `while[print(…)]:` is a one-element list, always true, one byte under
  `while 1:print(…);`.
- Tried and longer: keeping f = n! as a running product,
  `f=n=1` / `while[print(perm(f))]:f*=n;n+=1` (55 bytes); a recursive
  factorial `f=lambda n:n<1or n*f(n-1)` instead of the import (59 bytes,
  `True` comes out as 1 because f(f(0)) = True·True); and a product loop
  that extends (n!)! to ((n+1)!)! without any import (65 bytes).

**Notes**

- Exact integer arithmetic, correct for every n. The b-file has the six
  terms a(0)…a(5) and they print at once. The program then prints a(6) = 720!
  (1747 digits) and stops at a(7) = 5040!, which has 16474 digits and passes
  the 4300-digit int-to-str limit of Python 3.11+. The bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000197), CC BY-SA 4.0.
