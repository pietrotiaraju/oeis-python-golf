# A001205

> Number of clouds with n points; number of undirected 2-regular labeled graphs; or number of n X n symmetric matrices with (0,1) entries, trace 0 and all row sums 2.
> — [OEIS A001205](https://oeis.org/A001205)

Offset 0: 1, 0, 0, 1, 3, 12, 70, 465, 3507, 30016, 286884, 3026655, …

### Python 3 — 57 bytes

```python
x=y=n=0;z=1
while[print(z)]:x,y,z=y,z,n*z+n*~-n//2*x;n+=1
```

**How it works**

- A 2-regular graph is a set of undirected cycles of length ≥ 3, so the
  e.g.f. is exp(Σ_{k≥3} x^k/(2k)) = exp(−x/2 − x²/4)/√(1−x).
- Its logarithmic derivative is x²/(2(1−x)), so 2(1−x)E′ = x²E, which on
  coefficients reads a(n+1) = n·a(n) + C(n,2)·a(n−2) (the recurrence on
  the OEIS entry).
- `x,y,z` are a(n−2), a(n−1), a(n). C(n,2)·x is written `n*~-n//2*x`:
  n(n−1) is even, so the floor is exact. The seeds a(−2) = a(−1) = 0 never
  matter, since they meet the factors 0 and C(1,2) = 0.

**Notes**

- The whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001205), CC BY-SA 4.0.
