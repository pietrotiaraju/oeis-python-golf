# A000427

> Number of 7-dimensional partitions of n.
> — [OEIS A000427](https://oeis.org/A000427)

Offset 1: 1, 8, 36, 148, 554, 2024, 7134, 24796, 84625, 285784, …

### Python 3 — 167 bytes

```python
P=2,3,5,7,11,13,17,19;n=1
f=lambda S:n<=len(S)or sum(f(S|{c})for c in{s*p for s in S for p in P}if c>max(S)and{c//p for p in P if c%p<1}<=S)
while[print(+f({1}))]:n+=1
```

**How it works**

- A 7-dimensional partition is a weakly decreasing array of
  nonnegative heights. Replace each height by a stack of cells:
  its cells form a finite down-set of ℕ^8. Thus a(n) counts
  n-cell sets closed under decreasing any coordinate.
- Encode a cell (x₀, …, x_7) by the product of the powers of
  the 8 primes 2, 3, 5, 7, 11, 13, 17, 19. Unique factorization makes this
  an exact, unbounded coordinate encoding. A cell's immediate
  predecessors are c/p for the primes p dividing its encoding c.
- Start from {1}, the corner cell. Candidate cells are the
  products s*p one step above cells already present. The condition
  `{c//p for p in P if c%p<1}<=S` checks that every immediate
  predecessor is already in S, which preserves the down-set property.
- Integer order extends divisibility. Every down-set therefore
  has a unique increasing construction order. Requiring `c>max(S)`
  visits it exactly once, so no set of completed partitions or
  duplicate removal is needed.
- f(S) sums the ways to complete S to n cells. Its base case is
  True, the single completion when n cells have been placed;
  `+f({1})` converts that boolean to the integer 1 at n=1.

**Notes**

- This directly enumerates partitions in every size. No conjectured
  product formula or stored sequence terms are used. The same
  prime encoding is used by [A000334](../A000334/) and
  [A000390](../A000390/) in lower dimensions.
- Only the active construction path is retained, with recursion
  depth n. Running time still grows rapidly with the number of
  down-sets; CPython's recursion limit eventually applies.
- The b-file has 20 terms. The unchanged verification bar is
  the first 7 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 266 | first entry |
| 2026-11-06 | Python 3 | 167 | encode cells by prime exponents and enumerate each down-set once |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000427), CC BY-SA 4.0.
