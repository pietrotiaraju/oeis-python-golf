# A002175

> Excess of number of divisors of 12n+1 of form 4k+1 over those of form 4k+3.
> — [OEIS A002175](https://oeis.org/A002175)

Offset 0: 1, 2, 3, 2, 1, 2, 2, 4, 2, 2, 1, 0, …

### Python 3 — 62 bytes

```python
m=1
while[print(sum(~d%4-2for d in range(m)if m%~d>-1))]:m+=12
```

**How it works**

- a(n) = Σ_(D|m) χ(D) with m = 12n + 1 and χ the non-principal character
  modulo 4 (χ(D) = 1 for D ≡ 1 and −1 for D ≡ 3), which is the
  definition read as one sum. m is odd, so all its divisors are odd.
- d runs over 0, …, m − 1 and the divisor tested is D = d + 1, written
  through `~d` = −D:
  - `m%~d` is m mod (−D), which Python puts in (−D, 0]; it is `>-1`,
    that is 0, exactly when D divides m.
  - `~d%4` is (−D) mod 4, which is 3 for D ≡ 1 and 1 for D ≡ 3
    (mod 4), so `~d%4-2` is χ(D) for every odd D.
  This is one byte shorter than `2-d%4 … range(1,m+1) … m%d<1`.
- `while[print(…)]:m+=12` prints a(n) and steps to the next m.

**Notes**

- Exact integer arithmetic, right for every n.
- a(n) is also r₂(12n + 1)/4, the number of ways to write 12n + 1 as a
  sum of two squares divided by 4 (Jacobi's two-square theorem); counting
  those with `isqrt` would take O(√m) steps instead of m, but costs
  about 30 bytes more.
- Each term costs m = 12n + 1 divisibility tests, so the time grows like
  n²: the 6000th term comes at 18 reference seconds (30 s here). The
  b-file has 10001 terms; the bar is 6000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002175), CC BY-SA 4.0.
