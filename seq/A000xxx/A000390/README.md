# A000390

> Number of 5-dimensional partitions of n.
> — [OEIS A000390](https://oeis.org/A000390)

Offset 1: 1, 6, 21, 71, 216, 657, 1907, 5507, 15522, 43352, 119140, 323946, …

A 5-dimensional partition of n is a 5-dimensional array of non-negative
integers with sum n that decreases weakly along every axis. Replacing each
entry v by the v cells stacked above it turns it into a finite down-set of
n cells in ℕ⁶ (a set that contains every cell below each of its cells), so
a(n) counts the n-element down-sets of ℕ⁶. There is no product formula
(MacMahon's guess is [A000391](../A000391/), which differs from a(6) on),
so the program counts them directly. This is the
[A000334](../A000334/) program (4-dimensional partitions) with a sixth
prime.

### Python 3 — 137 bytes

```python
P=range(1,14);D={frozenset({1})}
while[print(len(D))]:D={S^{c}for S in D for s in S for p in P if{c//q for q in P if(c:=s*p)%q<1}<=S^{c}}
```

**How it works**

- **Cells as numbers.** The cell (x₀, …, x₅) is the number
  2^x₀·3^x₁·5^x₂·7^x₃·11^x₄·13^x₅. Moving one step along axis i multiplies by
  the i-th prime, a cell lies below another exactly when it divides it,
  and the cells just below c are c/q for the primes q dividing c. No
  coordinate bound is needed, so the encoding works for every n.
- **Layer by layer.** `D` holds every down-set with m cells, as
  frozensets, starting from {{1}} (the corner cell) for m = 1. Every
  down-set with m + 1 cells is S ∪ {c} for a down-set S with m cells and a
  maximal cell c (take any maximal cell out), and c is a lower neighbour
  s ∈ S times a prime. So the candidates c = s·p with s in S and p in `P`
  miss nothing; the set comprehension merges the copies of each new
  down-set.
- **The test.** `S^{c}` (symmetric difference) is S ∪ {c} when c ∉ S and
  S − {c} when c ∈ S. The set `{c//q for q in P if…%q<1}` is c itself
  (q = 1) together with every c/q for q dividing c. If c is already in S,
  c is not in S − {c} and the candidate is dropped (p = 1 always gives
  such a c). Otherwise the test says that every c/q is in S, that is,
  S ∪ {c} is a down-set, and `S^{c}` is that down-set. `(c:=s*p)` sits in
  the condition of the inner set, which runs before its first element, so
  c is set before `c//q` and the outer `<=S^{c}` read it.
- **Composites in `P`.** `range(1,14)` also holds the composites up to
  13, which change nothing. If a composite r divides c and t is a prime
  factor of r, then c/r divides c/t, so for a down-set S, c/t ∈ S already
  gives c/r ∈ S; and a candidate s·r with r composite is either dropped or
  a valid cell that the primes also reach. Every cell stays 13-smooth,
  with exponents only on the 6 primes up to 13.
- This is the template of [A000427](../A000427/) (7-dimensional
  partitions); `print(len(D))` in the header prints a(m) before the next
  layer is built.

**Notes**

- Exact enumeration with no formula, so the program is right for every n.
- Each layer holds a(m) frozensets, and every candidate builds a set of
  about m cells for `S^{c}`, even the ones that fail.
  Here 11 terms print in 60 s (the 11th after about 24 s), with
  about 0.35 GB in use by then.
- Listing the primes, `P=1,2,3,5,7,11,13`, is 141 bytes; with
  fewer candidates it is faster (12 terms in 60 s, but about 0.9 GB).
  [A000416](../A000416/)'s form, `S={s|{p}…}` with the candidates
  `{q*r for q in s for r in R}-s` and the filter
  `{p//r for r in R if p%r<1}<=s`, is 143 bytes.
- The previous record (161 bytes) counted each down-set once by adding
  cells in increasing order, `c>max(S)`, in a recursive function that needs
  almost no memory:

  ```python
  P=2,3,5,7,11,13;n=1
  f=lambda S:n<=len(S)or sum(f(S|{c})for c in{s*p for s in S for p in P}if c>max(S)and{c//p for p in P if c%p<1}<=S)
  while[print(+f({1}))]:n+=1
  ```

  Passing the last cell as a parameter instead of taking `max(S)` is
  2 bytes longer and a little faster; cells as numbers in base n with the
  digit test `c//p%n` are 172 bytes.
- The b-file has 30 terms (up to a(30)), from Suresh Govindarajan; the bar
  is 10 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 161 | first entry |
| 2026-11-07 | Python 3 | 137 | layer by layer with A000427's `S^{c}` test, `P=range(1,14)` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000390), CC BY-SA 4.0.
