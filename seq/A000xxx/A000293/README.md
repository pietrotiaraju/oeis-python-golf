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

### Python 3 — 135 bytes

```python
P=1,2,3,5,7;D={frozenset()}
while[print(len(D))]:D={S^{c}for S in D for s in S|{1}for p in P if{c//q for q in P if(c:=s*p)%q<1}<=S^{c}}
```

**How it works**

- A cell (a, b, c, d) is stored as the integer 2ᵃ·3ᵇ·5ᶜ·7ᵈ. Multiplying
  by a prime q ∈ {2, 3, 5, 7} is a step up along one axis, and when q
  divides c, c/q is the step down. Unique factorization makes this
  one-to-one.
- `D` holds every down-set with m cells, as frozensets, starting from the
  empty set for m = 0. Every down-set with m + 1 cells is S ∪ {c} for a
  down-set S with m cells and a maximal cell c (take any maximal cell out).
  Such a c is the origin 1 when S is empty, and otherwise one step up from
  one of its lower neighbours in S. So the candidates c = s·p with s in
  S ∪ {1} (`S|{1}`, which adds 1 only to the empty set) and p in
  `P=1,2,3,5,7` miss nothing; p = 1 just gives c = s.
- The test uses the symmetric difference `S^{c}`: it is S ∪ {c} when
  c ∉ S and S − {c} when c ∈ S. The set `{c//q for q in P if…%q<1}` is c
  itself (q = 1) together with its lower neighbours c/q. If c is already
  in S, c is not in S − {c} and the candidate is dropped. Otherwise the
  test says exactly that every lower neighbour is in S, that is, S ∪ {c}
  is a down-set, and `S^{c}` is that down-set. The set comprehension
  merges the copies of each new down-set.
- `(c:=s*p)` sits in the condition of the inner set, which runs before
  its first element (q = 1), so c is set before `c//q` and the outer
  `<=S^{c}` read it.
- At m = 0 only c = 1 passes (for c = q prime, 1 is missing), so the
  second layer is {{1}}: a(0) = a(1) = 1 come out in order.
- This is the template of [A000427](../A000427/) (7-dimensional
  partitions), with the empty start for offset 0.

**Notes**

- Plain enumeration with exact integers: right for every n, nothing
  conjectural.
- It keeps all a(m) sets of the current size, and each of the 5m
  candidates of a down-set builds a set of about m cells for `S^{c}`, even
  the ones that fail. Here 17 terms print in 60 s (a(16) after about 32 s),
  with about 0.5 GB in use by then.
- The previous record (145 bytes) listed the candidates as
  `{1,*{q*r for q in s for r in R}}-s` and tested
  `all(p%r or p//r in s for r in R)` with `R=2,3,5,7`. With
  [A000416](../A000416/)'s filter `{p//r for r in R if p%r<1}<=s` it is
  141 bytes and faster, since it builds a set only for the valid cells
  (18 terms in 22 s here), but building layer 18 took it past 1 GB.
  `{1,*S}` for `S|{1}` ties; `P=range(1,8)` (composites change nothing,
  as on the [A000334](../A000334/) page) is a byte longer.
- Storing a cell in base B instead (p + Bⁱ for a step up) needs a digit
  test for the axes where the coordinate is 0 and a B that grows with n;
  that is longer than the primes.
- The b-file has 73 terms (up to a(72)), from the large computations cited
  on the entry; the bar is 16 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 145 | first entry |
| 2026-11-07 | Python 3 | 135 | A000427's `S^{c}` test, with the origin added to the empty start |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000293), CC BY-SA 4.0.
