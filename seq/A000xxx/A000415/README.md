# A000415

> Numbers that are the sum of 2 but no fewer nonzero squares.
> — [OEIS A000415](https://oeis.org/A000415)

Offset 1: 2, 5, 8, 10, 13, 17, 18, 20, 26, 29, …

### Python 3 — 106 bytes

```python
n=1;s={1};k=2
while 1:
 if n==k*k:s.add(n);k+=1
 if n not in s and any(n-x in s for x in s):print(n)
 n+=1
```

**How it works**

Use the exact two-square membership test of [A000404](../A000404/).
The extra condition `n not in s` removes all single nonzero squares,
so two nonzero squares are necessary as well as sufficient.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 106 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000415), CC BY-SA 4.0.
