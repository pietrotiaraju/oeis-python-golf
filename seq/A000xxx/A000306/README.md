# A000306

> Number of trees of diameter 8.
> — [OEIS A000306](https://oeis.org/A000306)

Offset 9: 1, 4, 19, 66, 219, 645, 1813, 4802, 12265, 30198, 72396, 169231, …

A tree of diameter 8 has a central vertex, and rooted there it has height
exactly 4 with at least two branches of height exactly 3. Let g, c and p
count rooted trees of height at most 4, 3 and 2, shifted so that g(m)
counts trees with m + 1 nodes, as in [A000299](../A000299/). A tree rooted
at the centre is a multiset of branches of height at most 3: all such
multisets give g(m), those with no branch of height 3 give c(m), and those
with exactly one give Σ c(v)·(c − p)(m − 1 − v), the branch of height 3
times a multiset of lower ones. So

a(m + 1) = g(m) − c(m) − Σ_{v=0…m−1} c(v)·(c(m − 1 − v) − p(m − 1 − v)),

which is the PARI program's r₄ − r₃·s₃ on the OEIS page.

### Python 3 — 178 bytes

```python
L=[1]*3;n=0
while[n>-24or print(L[-3]-L[-2]-sum(L[-i-2]*(L[i-2]-L[i-1])for i in range(n,0,3)))]:
 n-=3
 for h in 1,1,0:L+=sum(d*L[n-d-2]**h*sum(L[d::d])for d in range(n,0,3))//n,
```

**How it works**

- The last two lines are the [A000299](../A000299/) program: `L` holds
  g, c and p interleaved, [g(0), c(0), p(0), g(1), …], and each round
  appends g(m), c(m) and p(m) with the Euler-transform recurrence
  **m·s(m) = Σₖ k·w(k − 1)·Σⱼ s(m − jk)** (weight c for g, p for c, 1 for p;
  see that page for the indexing). `L=[1]*3;n=0` is a byte under its
  `*L,n=1,1,1,0`.
- In the loop condition, after round m, n = −3m and `L[-3]-L[-2]` is
  g(m) − c(m). With i = −3w for w = m…1, `L[-i-2]` is c(w − 1) (position
  3w − 2), and `L[i-2]`, `L[i-1]` are c(m − w) and p(m − w), counted from
  the end. So the sum is the convolution above with v = w − 1.
- a(n) = 0 for n < 9, so `n>-24or` skips the rounds m < 8 and printing
  starts at a(9) = 1, the path on 9 nodes.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(4442) has 1000 digits, so the 4300-digit int-to-str limit is
  far beyond what the program reaches.
- About 3350 terms in 60 s here (n ≤ 3354); the b-file has 4434 terms
  (n ≤ 4442), so the bar is 2500 terms in 60 s.
- Printing only the nonzero values with `(v:=…)<1or print(v)` instead of
  `n>-24or` is 3 bytes longer. Shifting the summation index (for example
  `L[i]-L[i+1]` with `range(n-2,-2,3)`) or running it upwards with
  `range(2,-n,3)` does not get shorter, and dot products of slices with
  `map(int.__mul__,…)` are longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 178 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000306), CC BY-SA 4.0.
