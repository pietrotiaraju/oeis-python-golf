# A000507

> Number of permutations of [n] with exactly 3 increasing runs of length at least 2.
> — [OEIS A000507](https://oeis.org/A000507)

Offset 6: 61, 1385, 19028, 206276, 1949762, 16889786, 137963364, 1081702420, 8236142455, 61386982075, …

### Python 3 — 91 bytes

```python
n=6
while 1:print((3*7**n-(6*n-9)*5**n+(6*n*n-18*n+3)*3**n-4*n**3+18*n*n-8*n-15)//192);n+=1
```

**How it works**

- The program evaluates the closed formula recorded in OEIS:
  (3·7^n − (6n−9)·5^n + (6n²−18n+3)·3^n −4n³+18n²−8n−15)/192.
- Equivalently the ordinary generating function is
  x⁶(61−445x+963x²−675x³)/((1−5x)²(1−x)⁴(1−3x)³(1−7x)).
  Expanding its partial fractions gives precisely the polynomial times
  powers in the expression above.
- The first admissible length is n=6. At that length the numerator is
  11712, giving the first term 61.

**Notes**

- Every division is exact. Repeated exponentiation is short enough here
  that maintaining a longer recurrence gives no practical advantage.
- Python's integer conversion limit eventually applies.
- The reference file contains 18 terms from the OEIS b-file; the verification
  bar is 18 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000507), CC BY-SA 4.0.
