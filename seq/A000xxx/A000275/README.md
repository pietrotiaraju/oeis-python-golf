# A000275

> Coefficients of a Bessel function (reciprocal of J_0(z)); also pairs of permutations with rise/rise forbidden.
> — [OEIS A000275](https://oeis.org/A000275)

Offset 0: 1, 1, 3, 19, 211, 3651, 90921, 3081513, 136407699, 7642177651, …

### Python 3 — 94 bytes

```python
b=n=1;c=[1]
for x in c:print(abs(x));c+=-sum(c[~k]*(b:=b*(k-n)//~k)**2for k in range(n)),;n+=1
```

**How it works**

- The OEIS recurrence a(n) = Σ_{r<n} (−1)^(r+n+1) C(n,r)² a(r) loses its
  signs if the list holds c(r) = (−1)^r a(r): then c(n) = −Σ_{r<n} C(n,r)² c(r),
  which is Σ_{r≤n} C(n,r)² c(r) = 0 for n ≥ 1, i.e. (1/J₀)·J₀ = 1 with
  J₀(2√x) = Σ (−x)^r/r!². Printing `abs(x)` gives a(n) back.
- The sum starts from the newest term: `c[~k]` = c(n−1−k) goes with
  C(n,n−1−k) = C(n,k+1) for k = 0, …, n−1. `b` runs through C(n,1), …, C(n,n)
  by b·(n−k)/(k+1), written `b*(k-n)//~k` (both signs flipped; `~k` is a byte
  under `-~k`). The division is exact because C(n,k)·(n−k) = C(n,k+1)·(k+1).
- The last step leaves b = C(n,n) = 1, so `b` is ready for the next n with no
  reset; only the first pass needs `b=1`.
- `for x in c:` reads the list while it grows (each pass appends one term), so
  it never ends and hands out c(0), c(1), … in order.

**Notes**

- Integer arithmetic only, so it is exact for every n. The whole b-file
  (262 terms) takes well under a second; about 884 terms come out before a(n)
  passes CPython's 4300-digit int-to-str limit, which is an interpreter limit.
  The bar is the whole b-file in 60 s.
- Other routes tried: `from math import*` with `comb(n,k)**2*c[k]` is
  101 bytes; `-~k` instead of `~k` is 95. Keeping a(r) unsigned and running
  the signed square u = (−1)^k C(n,k+1)² instead of `b` drops `abs` and the
  minus, but u ends at (−1)^(n−1), so it needs `u=-1;` every pass (96 bytes).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 94 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000275), CC BY-SA 4.0.
