# A001037

> Number of degree-n irreducible polynomials over GF(2); number of n-bead necklaces with beads of 2 colors when turning over is not allowed and with primitive period n; number of binary Lyndon words of length n.
> — [OEIS A001037](https://oeis.org/A001037)

Offset 0: 1, 2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335, 630, 1161, 2182, 4080, …

### Python 3 — 90 bytes

```python
g=lambda n:2**n-sum(g(d)for d in range(1,n)if n%d<1)
n=0
while[print(g(n)//(n or 1))]:n+=1
```

**How it works**

- Each binary word of length n is, in exactly one way, a power of a
  primitive word of length d | n, and each Lyndon word of length d has d
  distinct rotations, the primitive words of its class; so
  Σ_{d|n} d·a(d) = 2ⁿ, which is the formula
  a(n) = (1/n) Σ_{d|n} μ(d)·2^(n/d) before inversion.
- `g(n)` = n·a(n) = 2ⁿ − Σ g(d) over the proper divisors d: Möbius
  inversion by subtraction, with no μ.
- g(0) = 2⁰ − 0 = 1 is a(0) itself, so the division is by `n or 1`.

**Notes**

- Exact integer arithmetic.
- The recursion is not memoized; it visits each chain of divisors of n
  once. The whole b-file (3334 terms) prints in about 3 s; the bar is the
  whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 90 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001037), CC BY-SA 4.0.
