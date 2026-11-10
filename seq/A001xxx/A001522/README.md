# A001522

> Number of n-stacks with strictly receding walls, or the number of Type A partitions of n in the sense of Auluck (1951).
> — [OEIS A001522](https://oeis.org/A001522)

Offset 0: 1, 1, 1, 1, 2, 3, 5, 7, 10, 14, 19, 26, 35, 47, 62, 82, 107, 139, …

### Python 3 — 114 bytes

```python
C=[]
while 1:C+=-sum((-1)**k*sum(C[k*(1-3*k)::-2*k][:2],k*k+k==len(C))for k in range(1,len(C))),0;print(C[-2]or 1)
```

**How it works**

- A stack here is a pile of rows of coins (boards) of lengths
  r₁ > r₂ > … > r_m from the bottom up, each row starting strictly right of
  and ending strictly left of the row below, so r_{i+1} ≤ r_i − 2 and row
  i+1 can sit in r_i − r_{i+1} − 1 places. With d_i = r_i − r_{i+1}
  (r_{m+1} = 0) the size is Σ i·d_i, and summing the weights gives
  1 + Σ_{m≥1} q^(m²) / ((q;q)_{m−1}²·(1 − q^m)), the form by Arndt on the
  OEIS page (checked against the data by brute force up to n = 44).
- The program uses the other generating function on the page,
  **1 + S(q)/P(q)** with S = Σ_{k≥1} (−1)^(k+1)·q^(k(k+1)/2) and
  P = Π (1 − qᵏ). It is Auluck's formula for Type A partitions (1951);
  the same series counts partitions with positive crank (Andrews and
  Garvan, *Dyson's crank of a partition*, 1988), which is the comment by
  Jovovic on the OEIS page.
- So u = S/P satisfies P·u = S, and Euler's pentagonal theorem
  P = 1 + Σ_{k≥1} (−1)ᵏ·(q^(k(3k−1)/2) + q^(k(3k+1)/2)) turns it into
  **u(n) = s(n) + Σ_{k≥1} (−1)^(k+1)·(u(n − k(3k−1)/2) + u(n − k(3k+1)/2))**,
  where s(n) = (−1)^(k+1) if n = k(k+1)/2 and 0 otherwise.
- `C` is u(0), 0, u(1), 0, …: a zero after every term, so `len(C)` = 2n
  while u(n) is computed. The slice `C[k*(1-3*k)::-2*k]` starts
  2·k(3k−1)/2 places from the end, at u(n − k(3k−1)/2), and steps back 2k
  places, to u(n − k(3k+1)/2); `[:2]` keeps the two. When the pentagonal
  number is past n the start lies before the list and a negative step gives
  an empty slice, so k may run over all of `range(1,len(C))` with no bound
  check.
- The triangular term rides along as the start value of the inner `sum`:
  `k*k+k==len(C)` is 1 exactly when n = k(k+1)/2. The leading minus turns
  (−1)ᵏ into (−1)^(k+1). u(0) = 0 and a(n) = u(n) for n ≥ 1, so
  `print(C[-2]or 1)` prints a(0) = 1.

**Notes**

- Counting the stacks directly by the differences d_i, with a cached
  recursion as in [A001524](../A001524/), is 126 bytes.
- Without the zero padding (`L+=x,`) the slices would need `//2` and n kept
  apart, 118 bytes.
- Exact integer arithmetic, so the program is right for every n, given the
  generating function above. a(n) has about 1.1·√n digits, far from the
  4300-digit int-to-str limit.
- Term n costs 2n cheap loop steps: 4000 terms take about 9 reference
  seconds, and in 60 s it gets to about 9800 of the 10001 terms of the
  b-file. The bar is 5000 terms in 60 s (about 15 reference seconds).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001522), CC BY-SA 4.0.
