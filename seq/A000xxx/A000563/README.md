# A000563

> Number of discordant permutations.
> — [OEIS A000563](https://oeis.org/A000563)

Offset 5: 13, 192, 1085, 3880, 10656, 24626, 50380, 94128, 163943, 270004, …

### Python 3 — 70 bytes

```python
n=5
while 1:print(n*((((81*n-1350)*n+8595)*n-24870)*n+27704)//40);n+=1
```

**How it works**

- OEIS gives P(n)=(81n⁵−1350n⁴+8595n³−24870n²+27704n)/40
  for the polynomial tail. The program factors out n and evaluates
  the remaining quartic in Horner form.
- This polynomial also gives the published offset value P(5)=13.
  Starting the loop at n=5 therefore includes the initial term without
  a separate print or an added correction.
- The final division by 40 is exact; no floating point coefficients
  or previously computed sequence values are needed.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 29 terms from the OEIS b-file; the verification
  bar is 29 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000563), CC BY-SA 4.0.
