# A000487

> Number of permutations of length n with exactly two valleys.
> — [OEIS A000487](https://oeis.org/A000487)

Offset 5: 16, 272, 2880, 24576, 185856, 1304832, 8728576, 56520704, 357888000, 2230947840, …

### Python 3 — 66 bytes

```python
n=5
while 1:print((6**n+(2-2*n)*4**n+(2*n*n-4*n-1)*2**n)//32);n+=1
```

**How it works**

Use the closed form listed by the OEIS, derived by partial
fractions from 16x⁵(1-3x)/((1-2x)³(1-4x)²(1-6x)).
Combining all terms over the common denominator 32 keeps
the calculation integral. The loop starts at n=5.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 196 terms in 60 s; the official b-file contains 196 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000487), CC BY-SA 4.0.
