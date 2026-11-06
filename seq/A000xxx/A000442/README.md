# A000442

> a(n) = (n!)^3.
> — [OEIS A000442](https://oeis.org/A000442)

Offset 0: 1, 1, 8, 216, 13824, 1728000, 373248000, 128024064000, 65548320768000, 47784725839872000, …

### Python 3 — 36 bytes

```python
a=1;n=0
while[print(a)]:n+=1;a*=n**3
```

**How it works**

Start with (0!)³ = 1. At each step, (n!)³ = n³*((n-1)!)³,
so multiplying the state by the cube of the new counter proves
the invariant for every n.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 101 terms in 60 s; the official b-file contains 101 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000442), CC BY-SA 4.0.
