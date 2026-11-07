# A000800

> Sum of upward diagonals of Eulerian triangle.
> — [OEIS A000800](https://oeis.org/A000800)

Offset 0: 1, 1, 1, 2, 5, 13, 38, 125, 449, 1742, 7269, 32433, 153850, 772397, 4088773, …

### Python 3 — 84 bytes

```python
P=[]
while 1:P+=(1,0),;print(sum(sum(P,())));k=0;P=[((k:=k+1)*(u+w),-u)for u,w in P]
```

**How it works**

- a(n) = Σₖ E(n−k, k), with E(m, k) the Eulerian numbers of
  [A173018](https://oeis.org/A173018) (E(0,0) = 1), so the g.f. is
  G(x) = Σₘ xᵐ Eₘ(x) with Eₘ(t) = Σₖ E(m,k) tᵏ.
- Euler's identity Eₘ(t)/(1−t)^(m+1) = Σ_{j≥0} (j+1)ᵐ tʲ, with t = x and
  summed over m, gives the formal power series
  G(x) = (1−x) · Σ_{j≥0} xʲ / (1 − (j+1)x(1−x)).
- Let b_j(t) = [xᵗ] 1/(1 − (j+1)x(1−x)), so
  b_j(t) = (j+1)(b_j(t−1) − b_j(t−2)), b_j(0) = 1, b_j(−1) = 0. Then
  a(n) = Σ_{j≤n} (b_j(n−j) − b_j(n−j−1)).
- `P` holds one pair per j, (u, w) = (b_j(t), −b_j(t−1)), so a(n) is just
  the sum of everything in `P`: `sum(sum(P,()))`. A step is
  (u, w) → ((j+1)(u+w), −u), with the walrus counter k = j+1 reset by
  `k=0`, and each round first appends (1, 0) for the new j = n.

**Notes**

- Exact integer arithmetic, O(n) multiplications per term (plus the
  tuple flattening); the whole b-file (601 terms) prints in about half a
  second, and it is the bar.
- Building the Eulerian triangle row by row and adding each row into a
  diagonal accumulator was 139 bytes; the explicit double sum
  Σ (−1)ⁱ C(m+1, i)(n−m−i+1)ᵐ with `comb` about 121.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000800), CC BY-SA 4.0.
