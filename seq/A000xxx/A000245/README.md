# A000245

> a(n) = 3*(2*n)!/((n+2)!*(n-1)!).
> — [OEIS A000245](https://oeis.org/A000245)

Offset 0: 0, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934, 41990, 149226, …

### Python 3 — 45 bytes

```python
c=m=1
while[print(-c+(c:=c*4*m//(m+3)))]:m+=2
```

**How it works**

- a(n) = C(n+1) − C(n), where C is the Catalan sequence
  [A000108](../A000108/). The loop carries `c` = C(n) and prints the
  difference between the new and the old value: `-c` is read before the
  walrus overwrites `c`, so `-c+(c:=…)` is C(n+1) − C(n) with no second
  variable.
- C(n+1) = C(n)·(4n+2)/(n+2). With m = 2n+1 that ratio is
  2m/((m+3)/2) = 4m/(m+3), so `m` steps by 2 and `c*4*m//(m+3)` is 4 bytes
  under `c*(4*n+2)//(n+2)`. The product c·4m is a multiple of m+3 because
  the quotient is the next Catalan number, so `//` is exact.
- Starting at C(0) = 1 with m = 1 gives C(1) = 1 and the first line
  0 = a(0), and `c=m=1` sets both at once.
- Also 45 bytes: the [A000108](../A000108/) update with n = k+2,
  `c=1;n=2` / `while[print(-c+(c:=4*c-6*c//n))]:n+=1` (the shorter step
  costs a longer start); printing a(n) = 3c − 6c/n directly,
  `while[print(a:=3*c-6*c//n)]:c+=a;n+=1`; and storing −C(n) so the print
  becomes `c-(c:=…)`, `c=m=-1` / `while[print(c-(c:=c*4*m//(m-3)))]:m-=2`.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (101 terms) prints at once; the program stops after a(7151), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000245), CC BY-SA 4.0.
