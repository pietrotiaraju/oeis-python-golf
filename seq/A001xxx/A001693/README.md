# A001693

> Number of degree-n irreducible polynomials over GF(7); dimensions of free Lie algebras.
> — [OEIS A001693](https://oeis.org/A001693)

Offset 0: 1, 7, 21, 112, 588, 3360, 19544, 117648, 720300, 4483696, 28245840, …

### Python 3 — 90 bytes

```python
g=lambda n:7**n-sum(g(d)for d in range(1,n)if n%d<1)
n=0
while[print(g(n)//(n or 1))]:n+=1
```

**How it works**

- Each word of length n over a 7-letter alphabet is, in exactly one way, a
  power of a primitive word of length d | n, and the d rotations of a
  primitive word are distinct; so if a(d) counts the classes (Lyndon words,
  or equally the monic irreducible polynomials of degree d over GF(7),
  or by Witt's formula the dimension of the degree-d part of the free Lie
  algebra on 7 generators), then Σ_{d|n} d·a(d) = 7ⁿ. Möbius inversion
  is the formula a(n) = (1/n) Σ_{d|n} μ(d)·7^(n/d).
- `g(n)` = n·a(n) = 7ⁿ − Σ g(d) over the proper divisors d of n: the
  inversion done by subtraction, with no μ.
- g(0) = 7⁰ − 0 = 1 is a(0) itself, so the division is by `n or 1`.

**Notes**

- The same program with 2 is [A001037](../A001037/) (GF(2)); with 5 it is
  [A001692](../A001692/).
- Exact integer arithmetic. The recursion is not memoized; it visits each
  chain of divisors of n once, and the whole b-file (1187 terms, a(0) to
  a(1186)) prints in about a second; the bar is the whole b-file in 60 s.
  a(5093) is the first term over 4300 digits, where Python's int-to-str
  limit would stop the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 90 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001693), CC BY-SA 4.0.
