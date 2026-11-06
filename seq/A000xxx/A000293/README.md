# A000293

> a(n) = number of solid (i.e., three-dimensional) partitions of n.
> — [OEIS A000293](https://oeis.org/A000293)

Offset 0: 1, 1, 4, 10, 26, 59, 140, 307, 684, 1464, 3122, 6500, 13426, …

A solid partition of n is a three-dimensional array of non-negative integers,
weakly decreasing along each axis, with sum n. Replacing each entry h at
(x, y, z) by the h cells (x, y, z, 0), …, (x, y, z, h − 1) turns it into a
down-set of n cells in ℕ⁴ (a four-dimensional Ferrers diagram), and every
such down-set comes from exactly one solid partition. No generating function
is known (MacMahon's guess is [A000294](../A000294/), which differs from
n = 6 on: 140 against 141), so the program counts down-sets by brute force.

### Python 3 — 145 bytes

```python
R=2,3,5,7
S={frozenset()}
while[print(len(S))]:S={s|{p}for s in S for p in{1,*{q*r for q in s for r in R}}-s if all(p%r or p//r in s for r in R)}
```

**How it works**

- A cell (a, b, c, d) is stored as the integer 2ᵃ·3ᵇ·5ᶜ·7ᵈ. Multiplying
  by r ∈ {2, 3, 5, 7} is a step up along one axis, and when r divides p,
  p/r is the step down. Unique factorization makes this one-to-one.
- `S` holds every down-set with m cells. A set s ∪ {p} with p ∉ s is again
  a down-set exactly when every step down from p is in s, and
  `p%r or p//r in s` checks that for each axis (a coordinate 0 has no step
  down).
- Every down-set with m + 1 cells is some s ∪ {p} with p a maximal cell
  and s a down-set with m cells; p is the origin 1 when s is empty, and
  otherwise one step up from a cell of s. So the candidates
  `{1,*{q*r…}}-s` miss nothing, and the set comprehension merges the
  copies of each new down-set.

**Notes**

- Plain enumeration with exact integers: right for every n, nothing
  conjectural.
- It keeps all a(m) sets of the current size, so time and memory both grow
  with a(n): here a(15) prints after about 8 s, a(16) after 16 s and a(17)
  (416 849 sets) after 36 s, 18 terms in 60 s. The bar is 16 terms in
  60 s. The b-file (73 terms, to a(72)) comes from the large computations
  cited on the entry; it is only used to check the terms printed.
- Storing a cell in base B instead (p + Bⁱ for a step up) needs a digit
  test for the axes where the coordinate is 0 and a B that grows with n;
  that is longer than the primes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 145 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000293), CC BY-SA 4.0.
