# A000564

> Number of discordant permutations.
> — [OEIS A000564](https://oeis.org/A000564)

Offset 6: 20, 371, 2588, 11097, 35645, 94457, 218124, 454220, 872648, 1571715, …

### Python 3 — 94 bytes

```python
print(20)
n=7
while 1:print(n*(((((81*n-2025)*n+20565)*n-106335)*n+280714)*n-303480)//80);n+=1
```

**How it works**

- OEIS gives P(n)=(81n⁶−2025n⁵+20565n⁴−106335n³+
  280714n²−303480n)/80 for n>6. Factoring out n and nesting the
  remaining coefficients gives the Horner form used in the program.
- At the offset n=6, the required term is 20 but P(6)=18. The first
  print handles this exception, and the loop begins at n=7.
- Every polynomial evaluation uses integer multiplications and additions;
  the final division by 80 is exact.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 25 terms from the OEIS b-file; the verification
  bar is 25 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 94 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000564), CC BY-SA 4.0.
