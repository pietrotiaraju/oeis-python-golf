# A000277

> 3*n - 2*floor(sqrt(4*n+5)) + 5.
> — [OEIS A000277](https://oeis.org/A000277)

Offset 0: 1, 2, 5, 6, 9, 10, 13, 16, 17, 20, …

### Python 3 — 46 bytes

```python
P=k=2
while[print(3*P+~k-k)]:P+=1;k+=~k*~k<4*P
```

**How it works**

- `P` holds n+2 and `k` holds s = ⌊√(4n+5)⌋, so the term is
  3n+5−2s = 3P−1−2k, printed as `3*P+~k-k` (`~k` is −k−1).
- When n goes up by one, s goes up by at most one (√(4n+9) − √(4n+5) < 1),
  and it does so exactly when (s+1)² ≤ 4n+5 for the new n, that is
  (k+1)² ≤ 4P−3. Squares are 0 or 1 mod 4 and 4P−2, 4P−1 are 2 and 3 mod 4,
  so this is the strict test `~k*~k<4*P` (`~k*~k` is (k+1)²).
- Holding s itself and n+2 makes both counters start at 2 (s(0) = ⌊√5⌋ = 2),
  so the setup is the single assignment `P=k=2`.
- `while[print(…)]:` loops forever (a one-element list is truthy) and is a
  byte under `while 1:print(…);`.

**Notes**

- Integer arithmetic only, no `math.isqrt` and no floats, so it is correct
  for every n. It prints about 1.6 million terms in 5 s; the bar is the
  whole b-file (1001 terms) in 60 s.
- Same idea as [A000267](../A000267/) (s(n) is A000267(n+1)), but the term
  needs 3n next to the 4n of the test, so the counter steps by one and both
  multiplications are written out.
- Other routes tried: the negated counter `N=2;j=-3` / `print(3*N+j-~j)` /
  `j-=j*j<4*N` is 47 bytes, and so is stepping t = 3n+6 by three
  (`t+j-~j`, `3*j*j<4*t`); stepping by four to get the bare test `c*c<m`
  needs `3*m//4` in the print (49); `math.isqrt(4*n+5)` is 60; printing
  each block of the step-3 runs with `exec` is 55.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000277), CC BY-SA 4.0.
