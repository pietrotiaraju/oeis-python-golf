# A000552

> Number of labeled rooted trees of height 3 with n nodes.
> — [OEIS A000552](https://oeis.org/A000552)

Offset 4: 24, 300, 3360, 38850, 475776, 6231960, 87530400, 1316954430, 21173760960, 362670636900, …

### Python 3 — 128 bytes

```python
f=lambda n,p,h:n|h<1or sum(((2**n+1)**n>>n*k)%2**n*p**k*f(n-k,k,h-1)for k in range(1,n*h+1))
n=4
while[print(n*f(n-1,1,3))]:n+=1
```

**How it works**

- **Layers.** Pick the root (n ways) and sort the other n − 1 labels by their
  distance from it. Height exactly 3 means three non-empty layers, and the
  tree is the same as a parent in the previous layer for every node. Let
  f(n, p, h) count the ways to fill h more non-empty layers with n labels
  when the layer above has p nodes: choose the k labels of the next layer
  and a parent for each of them, then go on with k parents, so

  f(n, p, h) = Σ_{k=1}^{n} C(n, k)·p^k·f(n − k, k, h − 1),

  with f(0, p, 0) = 1, f(n, p, 0) = 0 for n > 0 and f(0, p, h) = 0 for h > 0.
  Then a(n) = n·f(n − 1, 1, 3), the root being the single node of layer 0.
- **Base cases.** For n, h ≥ 0, `n|h<1` holds only at n = h = 0, where `True`
  is returned. `range(1,n*h+1)` is empty when h = 0 or n = 0, so the sum is 0
  in the other base cases. For h ≥ 2 the range runs past k = n; those terms
  have C(n, k) = 0, and their calls f(n − k, …) return at once, because
  n − k < 0 makes `n|h` negative.
- **Binomials.** `((2**n+1)**n>>n*k)%2**n` is C(n, k): the base-2^n digits of
  (2^n + 1)^n are the binomials C(n, j), all below 2^n (see
  [A000551](../A000551/)), and for k > n the shift by nk ≥ n(n + 1) bits
  leaves 0, since (2^n + 1)^n < 2^(n²+1). This is 3 bytes under
  `import math` plus `math.comb(n,k)`.

**Notes**

- Other versions: with `import math` and `math.comb` it is 131 bytes; the
  same recursion with `if h else n<1`, `range(1,n+1)` and
  `from math import*` was 135. [A000553](../A000553/) (height 4) is the
  same program with `n=5` and `f(n-1,1,4)`.
- Exact integer arithmetic, so the program is right for every n.
- The recursion visits every composition of n − 1 into three parts (plus
  the cut-off calls), so a term costs O(n³) big-number steps: the whole
  b-file prints in about 0.1 s here, and about 100 terms in 60 s. The b-file
  has 16 terms (up to a(19)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 179 | first entry |
| 2026-11-06 | Python 3 | 135 | count nonempty distance layers directly |
| 2026-11-07 | Python 3 | 128 | one base-case test n or h, range cut by h, binomials from (2^n + 1)^n |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000552), CC BY-SA 4.0.
