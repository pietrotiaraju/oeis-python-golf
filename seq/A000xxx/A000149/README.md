# A000149

> a(n) = floor(e^n).
> — [OEIS A000149](https://oeis.org/A000149)

Offset 0: 1, 2, 7, 20, 54, 148, 403, 1096, 2980, 8103, 22026, 59874, …

### Python 3 — 76 bytes

```python
n=0
while 1:
 N=F=d=1
 while-N%F<n**d:N=N*d+n**d;F*=d;d+=1
 print(N//F);n+=1
```

**How it works**

- The inner loop sums the series e^n = Σ n^k/k! over a common
  denominator: at each test, with m = d − 1, F = m! and N/F is the partial
  sum up to the term L = n^m/m!. Moving to the next term multiplies N and F
  by d and adds n^d to N.
- N/F is a lower bound for e^n. Once m ≥ 2n − 1 the tail Σ_{k>m} n^k/k!
  is below L·n/(m+1−n) ≤ L.
- `-N%F` is F − N mod F (or 0 when F divides N), so (−N mod F)/F is the
  gap from N/F up to the next integer, and `n**d` over F is n·L. The loop
  stops when the gap is at least n·L. For n ≥ 1 that is at least L, which
  is more than the tail, so e^n stays below the next integer and
  floor(e^n) = N//F. When F divides N the test reads 0 < n^d and the loop
  goes on.
- Before m = 2n − 1 the tail bound may fail, but there L = n^m/m! ≥ 1 (pair
  the factors of (2n−2)! as i·(2n−1−i) < n²), so n·L ≥ 1 is more than any
  gap and the loop cannot stop early.
- For n = 0, `0**d` is 0 for every d ≥ 1, so the test fails at once and the
  program prints N//F = 1 = e^0. For n ≥ 1, e^n is irrational, so the gap
  tends to a positive limit while n·L tends to 0, and the loop always ends.

**Notes**

- The previous record (77 bytes) kept P = n^m in a variable, with
  `N=F=P=d=1` and `while-N%F<P:P*=n;N=N*d+P;F*=d;d+=1`, and stopped as soon
  as the gap reached L. Writing `n**d` in both places drops `P=` and
  `P*=n;` for 3 more bytes of `n**d`, one byte less in all; the test then
  asks for a gap of n·L, which only makes the loop run a little longer.
- Everything is exact integer arithmetic; each term needs about e·n terms
  of the series. The whole b-file (301 terms) prints in under 2 seconds;
  the program is a little slower than the 77-byte one (about 710 terms
  against 960 in 40 s). The bar is the whole b-file in 60 s.
- The test `N%F+n**d>=F` (both floors differ) is two bytes longer than
  `-N%F<n**d` and needs the space after `while`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 77 | first entry |
| 2026-11-05 | Python 3 | 76 | `n**d` in place of the variable P |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000149), CC BY-SA 4.0.
