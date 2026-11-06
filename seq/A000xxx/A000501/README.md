# A000501

> a(n) = floor(cosh(n)).
> — [OEIS A000501](https://oeis.org/A000501)

Offset 0: 1, 1, 3, 10, 27, 74, 201, 548, 1490, 4051, …

### Python 3 — 100 bytes

```python
n=0
while 1:
 N=F=1;d=0
 while d<2*n or -N%F<n**d:d+=2;N=N*d*(d-1)+n**d;F*=d*(d-1)
 print(N//F);n+=1
```

**How it works**

- `N/F` is the even Taylor sum for cosh(n), through degree `d`. Moving to
  degree d+2 multiplies both numerator and denominator by (d+1)(d+2),
  then adds n^(d+2) to the numerator.
- Once d ≥ 2n, successive omitted terms have ratio below 1/4. The entire
  positive tail is therefore smaller than the last included term n^d/d!.
  `-N%F` is the numerator of the distance to the next integer. The inner
  loop stops only when that distance is at least the tail bound, so the
  Taylor sum and cosh(n) have the same floor.
- n=0 gives 1 directly. For every positive integer n, cosh(n) is
  transcendental (otherwise e^n would satisfy a quadratic over the
  algebraic numbers), so the shrinking bounds eventually decide its floor.

**Notes**

- All bounds and divisions use integers; no fixed precision or floating
  point rounding is assumed.
- Very large outputs eventually meet Python 3.11+'s integer conversion limit.
- The reference file contains 30 terms from the published OEIS entry; the verification
  bar is 30 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 100 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000501), CC BY-SA 4.0.
