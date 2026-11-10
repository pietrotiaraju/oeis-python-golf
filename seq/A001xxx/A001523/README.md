# A001523

> Number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n.
> — [OEIS A001523](https://oeis.org/A001523)

Offset 0: 1, 1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512, 784, 1183, 1765, …

### Python 3 — 140 bytes

```python
C=[]
f=lambda:-sum((-1)**k*sum(C[k*(1-3*k)::-2*k][:2],k*k+k==len(C))for k in range(1,len(C)))
while 1:C+=f(),;C+=C[-1]+f(),;print(C[-1]or 1)
```

**How it works**

- A stack is a pile of boards of lengths r₁ ≥ r₂ ≥ … from the bottom up,
  none overhanging the one below, so board i+1 has r_i − r_{i+1} + 1
  places; reading the column heights gives the weakly unimodal
  compositions. With d_i = r_i − r_{i+1} ≥ 0 this sums to
  1 + Σ_{m≥1} q^m / ((q;q)_{m−1}²·(1 − q^m)) (Arndt's form on the OEIS
  page; checked against the data by brute force up to n = 44).
- The program uses the generating function
  **1 + S(q)/P(q)²**, with S = Σ_{k≥1} (−1)^(k+1)·q^(k(k+1)/2) and
  P = Π (1 − qᵏ), the theorem of Auluck (1951) and Wright on stacks (see
  Stanley, *Enumerative Combinatorics* 1, Section 2.5, cited on the OEIS
  page). Dividing once by P gives u = S/P = [A001522](../A001522/) − 1,
  dividing again gives w = u/P = a − 1.
- Each division is Euler's pentagonal recurrence: P·w = u means
  w(n) = u(n) + Σ_{k≥1} (−1)^(k+1)·(w(n − k(3k−1)/2) + w(n − k(3k+1)/2)),
  and the same with S in place of u for the first division.
- `C` interleaves the two series: u(0), w(0), u(1), w(1), …. While u(n) is
  computed `len(C)` = 2n, while w(n) is computed it is 2n+1, and in both
  cases the slice `C[k*(1-3*k)::-2*k][:2]` (start 2·k(3k−1)/2 from the end,
  step back 2k) picks the two pentagonal lags of the right series. Slices
  past the start of the list are empty, so k runs over `range(1,len(C))`
  unchecked.
- The term of S is the start value `k*k+k==len(C)` of the inner sum; it
  can only fire at even length, so the same `f` serves both divisions, and
  the second one adds u(n) = `C[-1]` itself. a(0) = w(0) + 1 = 1 comes from
  `or 1`.

**Notes**

- The cached recursion over the differences d_i (as in
  [A001524](../A001524/)) is shorter, but with d_i = 0 allowed it nests n
  levels deep and keeps n² values: it stops near n = 1000.
- Exact integer arithmetic, so the program is right for every n, given the
  generating function above. a(n) has about 1.6·√n digits, far from the
  4300-digit int-to-str limit.
- Term n costs about 4n cheap loop steps: 3000 terms take about 8.5
  reference seconds, and in 60 s it gets to about 7800 terms. The bar is
  3500 terms in 60 s (about 12 reference seconds).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 140 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001523), CC BY-SA 4.0.
