# A000906

> Exponential generating function: 2*(1+3*x)/(1-2*x)^(7/2).
> — [OEIS A000906](https://oeis.org/A000906)

Offset 0: 2, 20, 210, 2520, 34650, 540540, 9459450, 183783600, 3928374450, …

### Python 3 — 37 bytes

```python
d=1;k=2
while[print(d*k)]:k+=2;d*=k+1
```

**How it works**

- n!·[xⁿ](1−2x)^(−7/2) = 7·9·…·(2n+5) = (2n+5)!!/15, so
  a(n) = 2·((2n+5)!! + 3n·(2n+3)!!)/15 = 2(n+1)·(2n+3)!!/3, which matches
  the OEIS formulas a(n) = (2n+5)!!/3 − (2n+3)!! and
  (2n+3)!/(3!·n!·2^(n−1)).
- With k = 2n+2 that is k·(k+1)!!/3. `d` is (k+1)!!/3 (an integer, since
  (k+1)!! contains the factor 3), starting at 3!!/3 = 1; each pass adds 2
  to `k` and multiplies `d` by the new odd factor k+1.
- Keeping d = m!! with m = 2n+3 lets the start share a value
  (`d=m=3`, `print(d*~-m//3)`) but costs 38 bytes.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. The program prints 1421 terms at once and then stops with a
  `ValueError` at the 4300-digit int-to-str limit of Python 3.11+.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000906), CC BY-SA 4.0.
