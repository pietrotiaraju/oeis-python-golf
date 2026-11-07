# A000561

> Number of discordant permutations.
> — [OEIS A000561](https://oeis.org/A000561)

Offset 3: 6, 44, 145, 336, 644, 1096, 1719, 2540, 3586, 4884, …

a(n) is the number of ways to put 3 non-attacking rooks on the n × n board
whose cells are (i, j) with j − i ≡ 0, 1 or 2 (mod n): three cyclic
diagonals. Call this r_k(n) for k rooks; [A000562](../A000562/),
[A000563](../A000563/), [A000564](../A000564/) and [A000565](../A000565/) are
r_4, …, r_7. By inclusion–exclusion, Σ_k (−1)^k·r_k(n)·(n − k)! counts the
permutations p with p(i) − i ≢ 0, 1, 2 (mod n), the discordant permutations
of the name (Riordan 1954).

### Python 3 — 40 bytes

```python
w=4
while[print((w**3-17*w+40)//6)]:w+=3
```

**How it works**

- **A cubic.** For n ≥ 3, a(n) = n·(9n² − 45n + 58)/2, the OEIS formula
  (Margolius 2001). The proof below shows that r_k(n) is a polynomial of
  degree ≤ k in n for n ≥ 2k + 1; for k = 3 the cubic fitted at n = 7, …, 10
  matches the b-file terms a(3), …, a(6) as well.
- **A monic cubic.** With w = 3n − 5, (3n − 5)³ − 17·(3n − 5) + 40 =
  27n³ − 135n² + 174n = 6·a(n). The leading coefficient of 6·a(n) is 27, so
  in w = 3n − s it is monic for any s; s = 5 also removes the w² term. So
  `(w**3-17*w+40)//6` is a(n), and the division is exact because the
  numerator is 6·a(n). `w=4` is n = 3 and `w+=3` steps n.
- `while[print(…)]:` loops forever: print returns None and `[None]` is
  truthy.

**Why r_k(n) is a polynomial**

- **Conflicts.** A rook in row i at offset a ∈ {0, 1, 2} sits in column
  i + a. Two rooks in different rows i, i′ share a column only if
  i′ − i ≡ a − a′ ∈ {−2, …, 2} (mod n). For n ≥ 5 these five residues are
  distinct, so only rooks at cyclic row distance 1 or 2 can clash, and which
  offset pairs clash depends only on that signed distance.
- **Gaps.** List the rooks in cyclic row order from a marked one: a start
  row, gaps g_1, …, g_k ≥ 1 with sum n, and offsets. This is a bijection with
  (placement, marked rook) pairs, so k·r_k(n) = n·Σ_g V(g), where V(g) counts
  the clash-free offset vectors. A distance between two rooks is a sum of
  consecutive gaps, and whether it is ≤ 2 (and its value then) depends only
  on the truncated gaps h_j = min(g_j, 3). So V(g) = V(h).
- **Counting gap sequences.** Fix h ∈ {1, 2, 3}^k with t entries equal to 3
  and the others summing to c. The g with that truncation are compositions of
  n − c into t parts ≥ 3; there are C(n − c − 2t − 1, t − 1) of them when
  t ≥ 1, and the binomial, read as a polynomial of degree t − 1 in n, gives
  this count (possibly 0) whenever n ≥ c + 2t + 1. As c ≤ 2(k − t), this
  holds for all h once n ≥ 2k + 1, and then t = 0 is impossible (it needs
  n = c ≤ 2k). So for n ≥ 2k + 1,

  r_k(n) = (n/k)·Σ_h V(h)·C(n − c − 2t − 1, t − 1),

  a polynomial of degree ≤ k; the t = k term gives the leading coefficient
  3^k/k!. It is fixed by the k + 1 values at n = 2k + 1, …, 3k + 1. A
  brute-force rook count agrees with the b-files of A000561–A000565 for
  n ≤ 4k + 5, so those values are confirmed independently.
- **Small n.** For k ≤ n ≤ 2k the polynomial and the b-file agree, except
  at n = k for k = 4 (a(4) = 9, polynomial 7) and k = 6 (a(6) = 20,
  polynomial 18); [A000562](../A000562/) and [A000564](../A000564/) add the
  difference with a term that vanishes from n = k + 1 on.

**Notes**

- Other versions: `while 1:print(…);w+=3` is 41 bytes; the first entry, the
  cubic in n as `n*(9*n*(n-5)+58)//2`, was 43.
- Exact integer arithmetic and the proof above, so the program is right for
  every n.
- The whole b-file prints in under 0.1 s here. a(n) has about 3·log₁₀ n
  digits, so the 4300-digit int-to-str limit is out of reach.
- The b-file has 998 terms (up to a(1000)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 43 | first entry |
| 2026-11-07 | Python 3 | 40 | monic cubic in w = 3n − 5 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000561), CC BY-SA 4.0.
