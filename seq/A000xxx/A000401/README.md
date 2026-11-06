# A000401

> Numbers of form x^2 + y^2 + 2*z^2.
> — [OEIS A000401](https://oeis.org/A000401)

Offset 1: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, …

### Python 3 — 61 bytes

```python
n=0
while[print(n)]:
 m=n=n+1
 while m%4<1:m//=4
 n+=m%16==14
```

**How it works**

- Dickson's characterization, cited by the OEIS, says that a nonnegative
  integer is represented by x² + y² + 2z² exactly when it is not of the
  form 4^k(16m + 14), for nonnegative integers k and m.
- Start by printing 0. `[print(n)]` is always a nonempty list, so the
  outer loop keeps going.
- `m=n=n+1` advances to the next candidate and copies it into `m`.
  This candidate is positive, so dividing `m` by 4 while `m%4<1`
  always terminates. The resulting `m` is the candidate with every
  factor of 4 removed.
- `m%16==14` identifies an excluded candidate. Adding that boolean
  skips it; otherwise `n` stays at the candidate. Every excluded
  number is even, so the number immediately after it is odd and
  represented. Thus one increment suffices, and the loop prints every
  term exactly once in increasing order.

**Notes**

- Exact integer arithmetic, correct for every n by Dickson's theorem.
  The first excluded values are 14, 30, 46, 56, 62, 78, 94, 110, 120,
  126, …; 56 = 4·14 and 224 = 16·14 check successive factors of 4.
- Keeping the zero case outside the division loop saves its explicit
  guard: the loop only ever examines positive candidates.
- The b-file has 1000 terms (indices 1 through 1000, ending at 1089).
  The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000401), CC BY-SA 4.0.
