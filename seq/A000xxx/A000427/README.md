# A000427

> Number of 7-dimensional partitions of n.
> — [OEIS A000427](https://oeis.org/A000427)

Offset 1: 1, 8, 36, 148, 554, 2024, 7134, 24796, 84625, 285784, …

A 7-dimensional partition of n is an array of nonnegative integers indexed by
ℕ⁷, weakly decreasing in every coordinate, with sum n. Stacking each entry as a
column of cells turns it into an n-cell down-set of ℕ⁸ (a set closed under
lowering any coordinate), and a(n) counts those.

### Python 3 — 147 bytes

```python
P=1,2,3,5,7,11,13,17,19;D={frozenset({1})}
while[print(len(D))]:D={S^{c}for S in D for s in S for p in P if{c//q for q in P if(c:=s*p)%q<1}<=S^{c}}
```

**How it works**

- A cell (x₁, …, x₈) is the number 2^x₁·3^x₂·…·19^x₈. Unique factorization
  makes this injective, raising coordinate i is multiplying by the i-th
  prime, and the cells just below c are the c/q for the primes q dividing c.
- D is the set of all down-sets with k cells, as frozensets, starting from
  {{1}} (the corner cell). A down-set with k + 1 cells minus one of its
  maximal cells is a down-set with k cells, so every (k+1)-cell down-set is
  S ∪ {c} for some S in D and some c outside S whose lower neighbours are all
  in S; such a c is s·p for a cell s of S (a lower neighbour of c times a
  prime) unless S is empty. The set comprehension builds all of them, and
  being a set it keeps each new down-set once. `len(D)` is a(k).
- `(c:=s*p)` names the candidate inside the inner comprehension. Since P
  also contains 1, the inner set {c//q : q | c} contains c itself, so
  `…<=S^{c}` says both that c ∉ S (otherwise `S^{c}` is S without c, which
  misses c) and that every lower neighbour of c is in S. `S^{c}` is then
  S ∪ {c}, the new down-set. The factor p = 1 only produces c ∈ S, which
  the test rejects.

**Notes**

- Building each down-set once by adding cells in increasing numeric order,
  as a recursion `f=lambda S:n<=len(S)or sum(f(S|{c})for c in{…}if
  c>max(S)and…)` with a counter n: 167 bytes, but faster and with little
  memory (9 terms in about 4 s here).
- Brute force over exact integers, so the program is right for every n.
- 8 terms in about 3 s here, a(9) at about 13 s and a(10) at about 54 s. D
  holds all a(k) down-sets at once: about 60 MB of frozensets for a(9) and
  several hundred MB for a(10).
- The b-file has 20 terms (up to a(20)); the bar is 7 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 266 | first entry |
| 2026-11-06 | Python 3 | 167 | encode cells by prime exponents and enumerate each down-set once |
| 2026-11-07 | Python 3 | 147 | grow all down-sets level by level in a set; 1 in P makes `S^{c}` test c ∉ S |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000427), CC BY-SA 4.0.
