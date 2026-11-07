# A000683

> Number of colorings of labeled graphs on n nodes using exactly 2 colors, divided by 4.
> — [OEIS A000683](https://oeis.org/A000683)

Offset 1: 0, 1, 6, 40, 360, 4576, 82656, 2122240, 77366400, …

### Python 3 — 78 bytes

```python
n=1
while[print(sum(1<<(k:=i.bit_count())*(n-k)for i in range(2**n))>>2)]:n+=1
```

**How it works**

- A labeled graph with a proper colouring in colours 1 and 2 is a set S of
  vertices (colour 1) together with any subset of the |S|(n−|S|) edges
  between S and the rest, so there are b(n) = Σ_S 2^{|S|(n−|S|)} of them
  ([A047863](https://oeis.org/A047863)). Using exactly 2 colours removes
  S = ∅ and S = all vertices, one graph each, and the sequence divides by 4:
  a(n) = (b(n) − 2)/4.
- The program runs over every subset as a bit mask `i < 2**n`, with
  k = `i.bit_count()` vertices in S, and sums `1<<k*(n-k)`.
- For n ≥ 1, b(n) ≡ 2 (mod 4): for 0 < k < n each term 2^{k(n−k)} is even
  and S and its complement give equal terms, so these add up to a multiple
  of 4, while the two extreme subsets give 2. So `>>2` is exactly
  (b(n) − 2)/4.

**Notes**

- Exact integer sums; no theorem beyond the counting above.
- The loop takes 2ⁿ steps: 25 terms in 60 s. Summing over the size k
  with `math.comb` instead of over subsets is polynomial and prints the
  whole 50-term b-file at once, but takes 84 bytes.
- The bar is 20 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000683), CC BY-SA 4.0.
