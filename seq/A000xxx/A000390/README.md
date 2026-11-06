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

### Python 3 — 161 bytes

```python
P=2,3,5,7,11,13;n=1
f=lambda S:n<=len(S)or sum(f(S|{c})for c in{s*p for s in S for p in P}if c>max(S)and{c//p for p in P if c%p<1}<=S)
while[print(+f({1}))]:n+=1
```

**How it works**

- **Cells as numbers.** The cell (x₀, …, x₅) is the number
  2^x₀·3^x₁·5^x₂·7^x₃·11^x₄·13^x₅. Moving one step along axis i
  multiplies by the i-th prime, a cell lies below another exactly when it
  divides it, and the cells just below c are c/p for the primes p dividing
  c. No coordinate bound is needed, so the encoding works for every n.
- **Each down-set once.** Divisibility implies ≤, so the integer order
  extends the order of the cells, and every prefix of a down-set listed in
  increasing order is again a down-set. So each n-element down-set is
  built exactly once by starting from {1} (the corner cell) and adding one
  cell at a time, each larger than all cells so far (`c>max(S)`) and with
  every cell just below it already present
  (`{c//p for p in P if c%p<1}<=S`). The candidates are the cells one step
  above some cell of S, `{s*p for s in S for p in P}`.
- `f(S)` counts the ways to complete S to n cells: True (= 1) once
  `n<=len(S)`, otherwise the sum over all valid next cells. The loop runs
  n = 1, 2, … and prints `+f({1})`; the `+` turns the True of n = 1
  into 1.

**Notes**

- The count is exact for every n, but the search visits every down-set of
  each size up to n, so the running time grows like a(n) itself (by about
  2.7 per term). The recursion is only n deep.
- 13 terms in 60 s here (the 13th after about 56 s); the b-file has 30
  terms (from Suresh Govindarajan), and the bar is 10 terms in 60 s.
- Passing the last cell as a parameter instead of taking `max(S)` is
  2 bytes longer and somewhat faster; cells as numbers in base n with the
  digit test `c//p%n` are 172 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 161 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000390), CC BY-SA 4.0.
