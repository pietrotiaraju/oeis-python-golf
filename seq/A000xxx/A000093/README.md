# A000093

> a(n) = floor(n^(3/2)).
> — [OEIS A000093](https://oeis.org/A000093)

Offset 0: 0, 1, 2, 5, 8, 11, 14, 18, 22, 27, 31, 36, 41, 46, 52, 58, …

### Python 3 — 41 bytes

```python
n=k=0
while k:=k-1:n+=k*k>n**3!=print(~k)
```

**How it works**

- a(n) = ⌊√(n³)⌋ is one less than the smallest j with j² > n³. The loop walks
  j = 1, 2, 3, … once, as k = −j, and keeps n as the index of the next term.
- `k*k>n**3!=print(~k)` is a chained comparison: it means
  `k*k>n**3 and n**3!=print(~k)`. The `print` only runs when j² > n³, and
  then `n**3!=None` is `True`. So the chain is `True` exactly when a term is
  printed, and `n+=` moves on to the next index.
- k is negative so that `~k` = −k − 1 = j − 1 is the term: `print(k-1)` with
  a positive k would cost two more bytes.
- One pass over j is enough because the sequence increases strictly:
  (n+1)^(3/2) − n^(3/2) > 1 for n ≥ 1, and a(0) = 0 < a(1) = 1. After a(n)
  is printed at j = a(n) + 1, that same j satisfies j² ≤ (n+1)³, so going on
  from j + 1 skips nothing, and the next hit is j = a(n+1) + 1.
- `while k:=k-1:` steps k and is always true, since k is never 0 again. It is
  the same length as `while 1:k-=1;`.

**Notes**

- Exact integer arithmetic, so the program is right for every n. It needs
  about n^(3/2) steps for the first n terms; the whole b-file (501 terms)
  prints in a few hundredths of a second. The bar is the whole b-file in 60 s.
- The direct `import math` + `n=0` + `while[print(math.isqrt(n**3))]:n+=1`
  is 51 bytes, and `from math import*` costs one more. `int(n**1.5)` is
  shorter but uses floats, which cannot stay exact once n^(3/2) passes 2⁵³.
- The terms only reach Python's 4300-digit int-to-str limit for n with about
  2870 digits, far beyond any run.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000093), CC BY-SA 4.0.
