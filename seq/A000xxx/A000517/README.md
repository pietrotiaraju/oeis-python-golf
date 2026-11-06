# A000517

> Number of permutations of length n with exactly three valleys.
> — [OEIS A000517](https://oeis.org/A000517)

Offset 7: 272, 7936, 137216, 1841152, 21253376, 222398464, 2174832640, 20261765120, 182172651520, 1594922762240, …

### Python 3 — 100 bytes

```python
n=7
while 1:print((8**n+(4-2*n)*6**n+(2*n*n-8*n+4)*4**n+(-4*n**3+24*n*n-26*n-12)*2**n//3)//128);n+=1
```

**How it works**

- Partial fractions of the OEIS generating function
  16x⁷(17−184x+636x²−720x³)/((1−2x)⁴(1−4x)³(1−6x)²(1−8x))
  give a polynomial times each of 2^n, 4^n, 6^n and 8^n.
- The program evaluates those four contributions. The cubic multiplying
  2^n is always divisible by 3 after that multiplication, so its inner
  division is exact, as is the final division by 128.
- The offset n=7 is the minimum length permitting three valleys.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 194 terms from the OEIS b-file; the verification
  bar is 194 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 100 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000517), CC BY-SA 4.0.
