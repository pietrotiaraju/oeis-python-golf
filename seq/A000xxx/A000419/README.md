# A000419

> Numbers that are the sum of 3 but no fewer nonzero squares.
> — [OEIS A000419](https://oeis.org/A000419)

Offset 1: 3, 6, 11, 12, 14, 19, 21, 22, 24, 27, …

### Python 3 — 147 bytes

```python
n=1;s={1};t={2};k=2
while 1:
 if n==k*k:s.add(n);t|={n+x for x in s};k+=1
 if n not in s and n not in t and any(n-x in t for x in s):print(n)
 n+=1
```

**How it works**

Use the exact three-square construction of [A000408](../A000408/).
Before the three-square test, exclude candidates in s (one nonzero
square) or t (two nonzero squares). The remaining accepted numbers
therefore require exactly three nonzero squares.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 147 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000419), CC BY-SA 4.0.
