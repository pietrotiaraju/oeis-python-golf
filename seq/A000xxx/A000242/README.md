# A000242

> 3rd power of rooted tree enumerator; number of linear forests of 3 rooted trees.
> — [OEIS A000242](https://oeis.org/A000242)

Offset 3: 1, 3, 9, 25, 69, 186, 503, 1353, 3651, 9865, 26748, 72729, 198447, …

A linear forest of three rooted trees is an ordered triple, so a(n) is the xⁿ
coefficient of T(x)³, where T(x) = x + x² + 2x³ + 4x⁴ + … counts rooted trees
([A000081](../A000081/)). Removing the root of a tree with k+1 nodes leaves a
rooted forest with k nodes, so T(x) = x·F(x) with F the forest series, and
a(n) = c(n−3) for C(x) = F(x)³.

### Python 3 — 107 bytes

```python
*L,n=1,1,0
while[print(L[-2])]:
 n-=2
 for h in 3,1:L+=h*sum(d*L[~d]*sum(L[d::d])for d in range(n,0,2))//n,
```

**How it works**

- F is the Euler transform of the tree counts, F(x) = ∏ₖ (1 − xᵏ)^(−F(k−1)),
  so its cube is the Euler transform of three times the same counts,
  C(x) = ∏ₖ (1 − xᵏ)^(−3F(k−1)). Both satisfy the log-derivative recurrence
  **m·F(m) = Σₖ k·F(k−1)·Σⱼ F(m − jk)** and
  **m·c(m) = 3·Σₖ k·F(k−1)·Σⱼ c(m − jk)**, over k = 1…m and j ≥ 1: the same
  weight, with a factor `h` = 3 or 1.
- One list holds both, interleaved as in [A000235](../A000235/):
  `L` = [c(0), F(0), c(1), F(1), …]. Each round appends c(m) and then F(m),
  and the loop condition prints `L[-2]` = c(m) = a(m+3). The start
  `*L,n=1,1,0` prints a(3) = 1.
- With n = −2m, `d` runs over −2m, −2m+2, …, −2, that is d = −2k. Before
  c(m) is appended the list has 2m entries, so `L[d::d]` starts at index
  2m − 2k and steps back by 2k: c(m−k), c(m−2k), …. Before F(m) is appended
  it has 2m+1 entries and the same slice reads F(m−k), F(m−2k), ….
- The weight `L[~d]` sits at index 2k − 1, which is F(k−1) in both passes
  (for k = m it is F(m−1), already in the list). The factor 2 in d cancels
  against the 2 in n.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n.
- About 2900 terms in 60 s here; the bar is the whole b-file (198 terms) in
  60 s. a(n) ~ 3·0.4399·2.9558ⁿ·n^(−3/2) (Kotesovec), so the 4300-digit
  int-to-str limit is only reached near n = 9150.
- Squaring the forest list with `sum(map(int.__mul__,F,F[::-1]))` as in
  [A000106](../A000106/) and then convolving once more needs a second list
  and a second dot product, well over 107 bytes. A lambda for the update,
  called as `L+=f(3),;L+=f(1),`, is 9 bytes longer, and computing both new
  entries from the old list in one comprehension needs a slice offset
  (`L[d+h//2::d]`) and is longer too.
- Moving `n-=2` into the loop condition (`while[print(L[-2]),n:=n-2]:`)
  costs 1 byte.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000242), CC BY-SA 4.0.
