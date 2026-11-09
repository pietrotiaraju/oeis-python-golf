# A001190

> Wedderburn-Etherington numbers: unlabeled binary rooted trees (every node has outdegree 0 or 2) with n endpoints (and 2n-1 nodes in all).
> — [OEIS A001190](https://oeis.org/A001190)

Offset 0: 0, 1, 1, 1, 2, 3, 6, 11, 23, 46, 98, 207, 451, 983, 2179, 4850, …

### Python 3 — 95 bytes

```python
L=[0,1]
for x in L:print(x);n=len(L);L+=(sum(map(int.__mul__,L[1:],L[:0:-1]))+~n%2*L[n//2])//2,
```

**How it works**

- A binary rooted tree with n ≥ 2 leaves is an unordered pair of subtrees
  with i and n − i leaves, so 2a(n) = Σᵢ₌₁ⁿ⁻¹ a(i)·a(n−i) + [n even]·a(n/2):
  the ordered pairs count each pair of different subtrees twice and each
  pair of equal ones once, and adding a(n/2) brings those up to two.
- `for x in L` reads the list while it grows: each pass prints one term
  and appends the next. With n = len(L), `L[1:]` against `L[:0:-1]` pairs
  a(i) with a(n−i) for i = 1 … n−1, and `~n%2*L[n//2]` is the middle term
  for even n.
- `L=[0,1]` holds a(0) = 0 and a(1) = 1.

**Notes**

- The whole b-file (2629 terms) takes about 3.5 million big-integer
  products, some 8 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001190), CC BY-SA 4.0.
