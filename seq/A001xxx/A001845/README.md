# A001845

> Centered octahedral numbers (crystal ball sequence for cubic lattice).
> — [OEIS A001845](https://oeis.org/A001845)

Offset 0: 1, 7, 25, 63, 129, 231, 377, 575, 833, 1159, 1561, 2047, 2625, …

### Python 3 — 35 bytes

```python
k=1
while[print(k*(k*k+5)//6)]:k+=2
```

**How it works**

- The crystal ball of the cubic lattice counts the points of Z³ with
  |x| + |y| + |z| ≤ n: a(n) = Σₖ 2ᵏ·C(3, k)·C(n, k) (choose the k nonzero
  coordinates, their signs, and their absolute values: k positive integers
  with sum ≤ n, C(n, k) ways), the Delannoy number D(n, 3), with g.f.
  (1 + x)³/(1 − x)⁴. Since C(n, k) is a polynomial in n, a(n) is a cubic in n,
  and it equals (2n + 1)(2n² + 2n + 3)/3 (the OEIS formula): two cubics
  that agree at n = 0, 1, 2, 3 agree for every n.
- With k = 2n + 1, 2n² + 2n + 3 = (k² + 5)/2, so a(n) = k(k² + 5)/6, and the
  division is exact. `k` runs over the odd numbers.

**Notes**

- The recurrence shared by all crystal balls (see [A001848](../A001848/)),
  `a,b=b,a+(7*b-a)//n`, is 49 bytes here.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001845), CC BY-SA 4.0.
