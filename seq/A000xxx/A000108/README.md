# A000108

> Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!).
> — [OEIS A000108](https://oeis.org/A000108)

Offset 0: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, …

### Python 3 — 39 bytes

```python
c=n=1
while[print(c)]:n+=1;c=4*c-6*c//n
```

**How it works**

- Consecutive Catalan numbers satisfy C(m) = C(m−1)·2(2m−1)/(m+1). Writing
  n = m + 1 moves the awkward `m+1` into a plain divisor: the step from
  C(n−2) to C(n−1) is a multiplication by (4n−6)/n.
- `c` holds the term just printed and `n` its index plus 2 (after the
  increment). The loop starts at c = C(0) = 1 and n = 1; the first pass bumps
  n to 2 and turns c into 1·2/2 = C(1), the next into 1·6/3 = C(2) = 2, then
  2·10/4 = 5, and so on.
- `print(c)` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).
- c·(4n−6)/n is split as 4c − 6c/n. Both 4c and the new term are integers, so
  6c/n is an integer too, and `6*c//n` (which Python reads as `(6*c)//n`)
  is exact. This is 2 bytes shorter than `c*=4*n-6;c//=n`.

**Notes**

- `c*=4*n-6;c//=n` (41 bytes) and `c=1;n=2` with `c=c*(4*n-6)//n;n+=1`
  (43 bytes) do the same with an explicit product and division.
- The closed form with `math.comb`, `from math import*`, `n=0`,
  `while[print(comb(2*n,n)//-~n)]:n+=1`, is 57 bytes.
- Python ints are exact, so the only limit is the 4300-digit int-to-str limit
  of Python 3.11+: the program prints C(0) to C(7152) and then stops with a
  `ValueError` at C(7153), the first term with more than 4300 digits. The
  values themselves were checked against `comb(2n,n)//(n+1)` up to n = 8000.
- The b-file has 1001 terms (up to C(1000), 598 digits) and all of them print
  in well under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000108), CC BY-SA 4.0.
