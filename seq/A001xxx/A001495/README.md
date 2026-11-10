# A001495

> Number of symmetric 0-1 (n+1) X (n+1) matrices with row sums 2 and first row starting 1,1 for n > 0, a(0)=1.
> — [OEIS A001495](https://oeis.org/A001495)

Offset 0: 1, 1, 1, 3, 13, 70, 462, 3592, 32056, 322626, 3611890, …

### Python 3 — 80 bytes

```python
p=q=n=0;r=s=1
while[print(r)]:p,q,r,s=q,r,s,(n-~n)*s-n*~-n*(2*r+(n-2)*p)//2;n+=1
```

**Why the recurrence**

- Read a symmetric 0-1 matrix as a graph on its rows: an off-diagonal 1 is
  an edge, a diagonal 1 a loop that adds 1 to the row sum. Row sums 2 then
  mean that the components are cycles of length ≥ 3 and paths of j ≥ 2
  vertices with a loop at both ends. There are (j − 1)!/2 labelled cycles
  and j!/2 labelled paths on j vertices, so the number M(m) of such m × m
  matrices ([A000986](https://oeis.org/A000986)) has the e.g.f.

  E(x) = exp(½(−log(1 − x) − x − x²/2) + x²/(2(1 − x))),

  and differentiating gives 2(1 − x)²E′ = (2x − x³)E.
- In an (n + 1) × (n + 1) matrix whose first row starts 1, 1, vertex 1 has
  a loop and its other neighbour is vertex 2, so it is the end of a path.
  A path from vertex 1 through j − 1 more vertices, in order, leaves
  M(n + 1 − j) choices for the rest; dividing the count with vertex 1 at a
  path end by n (its neighbour is any of the other n vertices, all alike)
  gives a(n) = (n − 1)!·Σ_{i<n} M(i)/i! for n ≥ 1. So the e.g.f. A of the
  sequence has A′ = E/(1 − x), which turns the equation for E into

  2(1 − x)²A″ = (2 − x³)A′,

  that is, for n ≥ 0,

  **a(n+2) = (2n+1)·a(n+1) − n(n−1)·a(n) − n(n−1)(n−2)/2 · a(n−2).**

  (This proves the e.g.f. that the entry gives as "it appears", and
  Israel's recursion there.) A brute-force count of the matrices agrees for
  n ≤ 5.

**How it works**

- `p, q, r, s` hold a(n−2), a(n−1), a(n), a(n+1); the pass prints a(n) and
  shifts in a(n+2). The weights of a(n) and a(n−2) vanish while n < 3, so
  the zeros standing in for a(−2), a(−1) never count.
- n(n − 1) is even, so `//2` is exact; `n-~n` is 2n + 1 and `n*~-n` is
  n(n − 1).

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(1552)
  has more than 4300 digits, where Python's int-to-str limit stops it.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 80 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001495), CC BY-SA 4.0.
