# A000562

> Number of discordant permutations.
> — [OEIS A000562](https://oeis.org/A000562)

Offset 4: 9, 95, 420, 1225, 2834, 5652, 10165, 16940, 26625, 39949, …

### Python 3 — 65 bytes

```python
print(9)
n=5
while 1:print(n*(((27*n-270)*n+921)*n-1078)//8);n+=1
```

**How it works**

- OEIS gives P(n)=(27n⁴−270n³+921n²−1078n)/8 for n>4.
  The program factors out n and evaluates the cubic inside it in
  Horner form, using the coefficients 27, −270, 921, −1078.
- The offset term is a(4)=9, whereas P(4)=7. Printing 9 separately
  preserves this exception; the polynomial loop starts at n=5.
- Clearing the rational denominators before the final division keeps
  the evaluation exact, with no floating point coefficients.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 36 terms from the OEIS b-file; the verification
  bar is 36 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000562), CC BY-SA 4.0.
