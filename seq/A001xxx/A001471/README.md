# A001471

> Number of degree-n permutations of order exactly 3.
> — [OEIS A001471](https://oeis.org/A001471)

Offset 0: 0, 0, 0, 2, 8, 20, 80, 350, 1232, 5768, 31040, 142010, 776600, 4874012, 27027728, …

### Python 3 — 52 bytes

```python
a=b=c=n=1
while[print(a-1)]:a,b,c=b,c,c+n*-~n*a;n+=1
```

**How it works**

- 3 is prime, so a permutation whose order divides 3 has order 1 (only
  the identity) or exactly 3: a(n) = [A001470](../A001470/)(n) − 1.
- A001470: every cycle has length 1 or 3, and point n is fixed or in one
  of (n−1)(n−2) 3-cycles, so A(n) = A(n−1) + (n−1)(n−2)·A(n−3) with
  A(0) = A(1) = A(2) = 1.
- `a`, `b`, `c` hold A(m−1), A(m), A(m+1) with `n` = m, so
  `c+n*-~n*a` = A(m+2); the start m = 1 is all ones. The program prints
  A − 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n; the
  4300-digit int-to-str limit stops it at about n = 2214.
- The b-file has 101 terms (n = 0 to 100); all of them print instantly,
  and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001471), CC BY-SA 4.0.
