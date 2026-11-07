# A000685

> Number of 3-colored labeled graphs on n nodes, divided by 3.
> — [OEIS A000685](https://oeis.org/A000685)

Offset 1: 1, 5, 41, 545, 11681, 402305, 22207361, 1961396225, …

### Python 3 — 109 bytes

```python
f=lambda m,n:m<2or sum(f(m-1,k:=i.bit_count())<<k*(n-k)for i in range(2**n))
n=1
while[print(f(3,n)//3)]:n+=1
```

**How it works**

- Let c_m(n) count labeled graphs on n vertices together with a proper
  colouring in colours 1..m (classes may be empty). Choosing the set S of
  vertices in colours 1..m−1 leaves colour m to the rest, the
  |S|(n−|S|) edges between S and the rest are free, and S itself carries an
  (m−1)-coloured graph: c_m(n) = Σ_S 2^{|S|(n−|S|)}·c_{m−1}(|S|), with
  c_1(n) = 1. This is the coefficient form of E(x)^m in the OEIS entry.
- `f(m,n)` does that sum over the bit masks `i < 2**n`, with the walrus
  `k:=i.bit_count()` passed straight into the recursive call. At the bottom
  `m<2or` returns `True`, which acts as 1 in `True<<k*(n-k)`.
- a(n) = c_3(n)/3.

**Notes**

- The division is exact for n ≥ 1: shifting all colours by one (mod 3)
  moves every colouring, so the colourings fall into orbits of size 3.
- About 3ⁿ steps per term: 16 terms in 60 s. The same recursion summed over
  k with `math.comb` is polynomial and prints the whole 50-term b-file in a
  second, but takes 120 bytes.
- The bar is 12 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 109 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000685), CC BY-SA 4.0.
