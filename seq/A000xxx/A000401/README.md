# A000401

> Numbers of form x^2 + y^2 + 2*z^2.
> — [OEIS A000401](https://oeis.org/A000401)

Offset 1: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, …

### Python 3 — 61 bytes

```python
n=0
while[print(n)]:
 m=n=n+1
 while m%4<1:m//=4
 n+=m%16==14
```

**How it works**

- Dickson's characterization, cited by the OEIS, says that a nonnegative
  integer is represented by x²+y²+2z² exactly when it is not of the
  form 4ᵏ(16m+14), for nonnegative integers k and m.
- Start by printing 0. `[print(n)]` is always a nonempty list, so the
  outer loop keeps going even though `print` returns `None`.
- `m=n=n+1` advances to the next candidate and copies it into `m`.
  The candidate is positive, so `while m%4<1:m//=4` terminates, leaving
  that candidate with every factor of 4 removed. Testing zero here
  would loop forever; printing it before the first increment avoids
  needing a separate guard.
- `m%16==14` identifies an excluded candidate. Adding that boolean
  skips it; otherwise n remains unchanged. Every excluded number is
  even, so the immediately following odd number is represented. A
  single increment suffices, and the increasing output misses no term.

**Notes**

- Exact integer arithmetic, correct for every candidate by Dickson's
  theorem. No search bound on x, y or z is needed.
- The first exclusions are 14, 30, 46, 56, 62, 78, 94, 110, 120,
  126, … . For 56, the inner loop leaves 14; for 224=16·14 it also
  leaves 14. Thus both are skipped for the same reason as 14.
- The theorem saves enumerating three coordinates or storing a growing
  set of represented integers. Only n and a temporary reduced copy are
  retained; testing a candidate uses at most O(log n) divisions by 4.
- The indexing starts at 1, but a(1)=0: the OEIS offset is an output
  position, not the smallest represented positive integer.
- The b-file has 1000 terms (indices 1 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000401), CC BY-SA 4.0.
