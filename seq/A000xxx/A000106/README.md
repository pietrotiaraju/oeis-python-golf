# A000106

> 2nd power of rooted tree enumerator; number of linear forests of 2 rooted trees.
> — [OEIS A000106](https://oeis.org/A000106)

Offset 2: 1, 2, 5, 12, 30, 74, 188, 478, 1235, 3214, 8450, 22370, 59676, 160140, …

### Python 3 — 111 bytes

```python
F=1,;n=0
while[print(sum(map(int.__mul__,F,F[::-1])))]:n-=1;F+=sum(d*F[~d]*sum(F[d::d])for d in range(n,0))//n,
```

**How it works**

- a(m) is the x^m coefficient of T(x)², where T(x) = x + x² + 2x³ + 4x⁴ + …
  counts rooted trees ([A000081](../A000081/)): a linear forest of two rooted
  trees is an ordered pair, so **a(m) = Σ r(i)·r(m−i)** over 0 < i < m.
- `F` holds rooted forests, F(k) = r(k+1) (removing the root of a tree with
  k+1 nodes leaves a forest with k nodes), so T(x) = x·Σ F(k)·x^k and
  a(m) = Σ F(i)·F(m−2−i) over 0 ≤ i ≤ m−2: the self-convolution of F at
  m−2. When the tuple holds F(0) … F(K), `map(int.__mul__,F,F[::-1])` pairs
  F(i) with F(K−i) and the sum is a(K+2).
- Listing forests rather than trees is what lets the print sit in the loop
  condition: the starting tuple `F=1,` already prints a(2) = 1.
- Forests satisfy the Euler-transform recurrence
  **k·F(k) = Σ_d d·F(d−1)·Σ_{j≥1} F(k−jd)**, summed over 1 ≤ d ≤ k, as in
  [A000055](../A000055/). After `n-=1`, `n` is −k and the tuple holds F(0) …
  F(k−1), so with d running over −k … −1, `F[~d]` is F(|d|−1), the slice
  `F[d::d]` walks back from F(k−|d|) in steps of |d|, and dividing the
  negative sum by `n` gives F(k).
- `while[print(…)]` prints and loops forever because `[None]` is a non-empty
  list; `F+=…,` concatenates a one-item tuple.

**Notes**

- Exact integer arithmetic, so the program is right for every n: the
  division is exact because the recurrence gives an integer.
- Each term costs O(n log n) big-integer operations. The whole b-file (999
  terms, n up to 1000) prints in under a second, and about 3500 terms print
  in 60 s. The bar is the whole b-file in 60 s.
- a(n) ~ 0.8798 · 2.9558ⁿ · n^(−3/2) (Kotesovec), so from about n = 9150 its
  decimal form passes Python's 4300-digit int-to-str limit.
- Listing the trees themselves, `r=[n:=0,1]` as in A000081, is 114 bytes:
  the convolution of `[0, 1]` is 0, so the print has to move after the
  append (`while 1:` … `;print(…)`).
- Ties at 112: `F=[1]` with no `n`, and the recurrence written as
  `sum(e*x*sum(F[-e::-e])for e,x in enumerate(F,1))//len(F)`.
- `math.sumprod(F,F[::-1])` (Python 3.12) is 13 bytes shorter than the
  `sum(map(…))`, but `from math import*` costs 18.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 112 | first entry |
| 2026-11-06 | Python 3 | 111 | use a tuple for the initial F state |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000106), CC BY-SA 4.0.
