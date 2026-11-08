# A000985

> Number of n X n symmetric matrices with nonnegative entries and all row sums 2.
> — [OEIS A000985](https://oeis.org/A000985)

Offset 0: 1, 1, 3, 11, 56, 348, 2578, 22054, 213798, 2313638, 27627434, …

### Python 3 — 75 bytes

```python
a=b=c=m=0;d=1
while[print(d-c)]:m+=1;a,b,c,d=m*b,m*c,m*d,2*m*d-~-m*c-b+a//2
```

**How it works**

- E.g.f. S(x) = (1−x)^(−1/2) exp(x²/4 + x/(2(1−x))) (in the entry; it is
  the exponential formula for the components: cycles, double edges and
  paths ended by diagonal 1s or a single diagonal 2).
- The program runs P = S/(1−x) = (1−x)^(−3/2) exp(x²/4 + x/(2(1−x)))
  instead. Its logarithmic derivative gives 2(1−x)²P′ = (4 − 2x − 2x² + x³)P,
  so p(n) = n!·[xⁿ]P satisfies

  p(n+1) = 2(n+1)p(n) − n²p(n−1) − n(n−1)p(n−2) + n(n−1)(n−2)p(n−3)/2.

- The states are kept factorial-scaled: `d` = p(n), `c` = n·p(n−1),
  `b` = n(n−1)p(n−2), `a` = n(n−1)(n−2)p(n−3). With `m` = n+1 the recurrence
  is p(m) = 2m·d − (m−1)c − b + a/2, and the next states are just `m*b`,
  `m*c`, `m*d`: no falling factorials in the code. `a` holds a product of
  three consecutive integers, so `a//2` is exact.
- S = (1−x)P gives s(n) = p(n) − n·p(n−1) = `d-c`, the printed term.
- P counts [A000987](../A000987/) shifted by two, which uses the same
  machine. The direct machine for S, `(2*m-1)*d-(m-2)*c-b+a//2` with
  `print(d)`, is 4 bytes longer.

**Notes**

- Exact integer arithmetic; it rests on the e.g.f. above (the recurrence
  is Kotesovec's in the entry, shifted).
- The program stops at Python's 4300-digit `int`-to-`str` limit after
  1552 terms (well under a second); the b-file has 101 terms and the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000985), CC BY-SA 4.0.
