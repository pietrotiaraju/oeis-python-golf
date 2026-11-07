# A000684

> Number of colored labeled n-node graphs with 2 interchangeable colors.
> — [OEIS A000684](https://oeis.org/A000684)

Offset 1: 1, 3, 13, 81, 721, 9153, 165313, 4244481, 154732801, …

### Python 3 — 77 bytes

```python
n=1
while[print(sum(1<<(k:=i.bit_count())*(n-k)for i in range(2**~-n)))]:n+=1
```

**How it works**

- A graph properly coloured with 2 colours is a vertex set S (one colour)
  plus any subset of the |S|(n−|S|) edges between S and the rest. With
  interchangeable colours, count each colouring once by letting S be the
  vertices whose colour differs from that of vertex n: S is any subset of
  the other n − 1 vertices, so
  a(n) = Σ_{S ⊆ {1..n−1}} 2^{|S|(n−|S|)} = Σ_k C(n−1,k)·2^{k(n−k)}
  (Bala's formula in the OEIS entry).
- The program runs over the bit masks `i < 2**~-n` (2ⁿ⁻¹ subsets), with
  k = `i.bit_count()`, and adds `1<<k*(n-k)`.

**Notes**

- Exact integer sums; no theorem beyond the counting above.
- The loop takes 2ⁿ⁻¹ steps: 26 terms in 60 s. The same sum over k with
  `math.comb` is polynomial and prints the whole 100-term b-file at once,
  but takes 82 bytes.
- The bar is 20 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000684), CC BY-SA 4.0.
