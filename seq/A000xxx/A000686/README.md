# A000686

> Number of 4-colored labeled graphs on n nodes, divided by 4.
> — [OEIS A000686](https://oeis.org/A000686)

Offset 1: 1, 7, 85, 1777, 63601, 3882817, 403308865, 71139019777, …

### Python 3 — 109 bytes

```python
f=lambda m,n:m<2or sum(f(m-1,k:=i.bit_count())<<k*(n-k)for i in range(2**n))
n=1
while[print(f(4,n)//4)]:n+=1
```

**How it works**

- Same recursion as [A000685](../A000685/): c_m(n) counts labeled graphs
  with a proper colouring in colours 1..m (classes may be empty), and
  c_m(n) = Σ_S 2^{|S|(n−|S|)}·c_{m−1}(|S|) over the set S of vertices in
  colours 1..m−1, with c_1(n) = 1 (the coefficient form of E(x)⁴ in the
  OEIS entry).
- `f(m,n)` sums over the bit masks `i < 2**n` with `k:=i.bit_count()`;
  `m<2or` returns `True`, which is 1 in `True<<k*(n-k)`.
- a(n) = c_4(n)/4.

**Notes**

- The division is exact for n ≥ 1: shifting all colours by one (mod 4)
  moves every colouring, so the colourings fall into orbits of size 4.
- About 4ⁿ steps per term: 12 terms in 60 s. The same recursion summed over
  k with `math.comb` is polynomial and prints the whole 16-term b-file at
  once, but takes 120 bytes.
- The bar is 9 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 109 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000686), CC BY-SA 4.0.
