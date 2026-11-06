# A000127

> Maximal number of regions obtained by joining n points around a circle by
> straight lines. Also number of regions in 4-space formed by n-1 hyperplanes.
> — [OEIS A000127](https://oeis.org/A000127)

Offset 1: 1, 2, 4, 8, 16, 31, 57, 99, 163, 256, 386, 562, 794, 1093, 1471, …

The terms are **a(n) = C(n,4) + C(n,2) + 1**: the first five are powers of
2, and then the pattern breaks.

### Python 3 — 41 bytes

```python
m=0
while[print((m*m-m+5)**2//24+m)]:m+=1
```

**How it works**

- Put m = n − 1, so m runs 0, 1, 2, … Expanding C(n,4) + C(n,2) + 1 gives
  24·a(n) = m⁴ − 2m³ + 11m² + 14m + 24.
- The square of m² − m + 5 is m⁴ − 2m³ + 11m² − 10m + 25, which matches
  the first three terms. What is left over is 24m − 1, so
  **24·a(n) = (m² − m + 5)² + 24m − 1**.
- Dividing by 24: `(m*m-m+5)**2//24` is ((m² − m + 5)² − 1)/24, because
  the identity makes (m² − m + 5)² one more than a multiple of 24, and
  floor division drops the extra 1/24. Adding `m` gives a(n).
- `while[print(…)]` is always true because `[None]` is a non-empty list, as
  in [A000027](../A000027/), so the loop prints a(1), a(2), … forever.

**Notes**

- Exact integer arithmetic and an algebraic identity, so it is right for
  every n. The terms reach Python's 4300-digit int-to-str limit only near
  n = 10¹⁰⁷⁵.
- Counting down with `k=0`, `k-=1` and `(k*k+k+5)**2//24-k` is also 41
  bytes.
- Longer versions that print the same terms:
  - keeping t = m² − m + 5 in a variable (it grows by 2m each step),
    `t=5;m=0` + `while[print(t*t//24+m)]:t+=2*m;m+=1`: 43 bytes;
  - the difference table, a(n + 1) = a(n) + C(n−1,0) + … + C(n−1,3), with
    the four sums kept in variables that each add the next one,
    `a=b=c=d=1` + `while[print(a)]:a+=b;b+=c;c+=d;d+=1`: 45 bytes;
  - the factored form 24(a(n) − 1) = n(n − 1)(n² − 5n + 18), as
    `n*~-n*(n*n-5*n+18)//24+1` with n from 1: 47 bytes;
  - the Horner form from the OEIS entry, `n*(n*(n*(n-6)+23)-18)//24+1`:
    50 bytes.
- The `+m` cannot be folded into the square: for a quadratic Q = m² + pm + q,
  matching the m³ and m² terms of 24·a(n) forces p = −1 and q = 5, which
  always leaves 24m − 1 over.
- The whole b-file (1000 terms) prints in a fraction of a second; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000127), CC BY-SA 4.0.
