# A001671

> Powers of e rounded up.
> — [OEIS A001671](https://oeis.org/A001671)

Offset 0: 1, 3, 8, 21, 55, 149, 404, 1097, 2981, 8104, 22027, 59875, 162755, …

### Python 3 — 79 bytes

```python
n=0
while 1:
 N=F=d=1
 while-N%F<n**d:N=N*d+n**d;F*=d;d+=1
 print(0--N//F);n+=1
```

**How it works**

The loop is the one of [A000149](../../A000xxx/A000149/) (⌊eⁿ⌋), with the
ceiling of the partial sum printed instead of its floor.

- The inner loop sums eⁿ = Σ nᵏ/k! over a common denominator: at each test,
  with m = d − 1, F = m! and N/F is the partial sum up to the term
  L = nᵐ/m!. The next term multiplies N and F by d and adds nᵈ to N.
- `-N%F` is the gap from N/F up to the next integer, times F, and `n**d`
  over F is n·L. The loop stops when the gap is at least n·L. Once
  m ≥ 2n − 1 the tail of the series is below L ≤ n·L, so eⁿ lies strictly
  between N/F and the next integer; before that, n·L ≥ 1 exceeds every gap
  and the loop cannot stop (see A000149 for both bounds).
- For n ≥ 1 the gap at the stop is at least n·L > 0, so N/F is not a whole
  number and eⁿ (irrational) lies strictly inside the same unit interval:
  ⌈eⁿ⌉ = ⌈N/F⌉. `0--N//F` is 0 − ⌊−N/F⌋ = ⌈N/F⌉, one byte shorter than
  `-(-N//F)`.
- For n = 0, `0**d` is 0, the test fails at once, and the program prints
  ⌈1⌉ = 1 = e⁰, which `N//F+1` would get wrong.

**Notes**

- Exact integer arithmetic, and eⁿ is irrational for n ≥ 1 (Lindemann), so
  the loop always ends and every term is right.
- The whole b-file (501 terms) prints in about 15 s here; the bar is the
  whole b-file in 60 s.
- `print(N//F+(n>0))` is three bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001671), CC BY-SA 4.0.
