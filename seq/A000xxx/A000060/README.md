# A000060

> Number of signed trees with n nodes.
> — [OEIS A000060](https://oeis.org/A000060)

Offset 1: 1, 2, 3, 10, 27, 98, 350, 1402, 5743, 24742, 108968, 492638, …

A signed tree is an unlabeled tree with a sign (+ or −) on each edge.

### Python 3 — 131 bytes

```python
a=[-1,n:=1]
while[print(sum(a[i]*((2*i==n)-a[~i])for i in range(n)))]:a+=2*sum(d*a[-d]*sum(a[d:0:d])for d in range(-n,0))//-n,;n+=1
```

**How it works**

- `a[k]` for k ≥ 1 counts rooted signed trees with k nodes
  ([A000151](https://oeis.org/A000151)). Each branch of the root hangs from
  an edge of one of two signs, so S = x·∏ (1 − xᵏ)^(−2aₖ), an Euler
  transform with weight 2.
- The Euler-transform recurrence is n·aₙ₊₁ = 2·Σₖ k·aₖ·Σⱼ aₙ₊₁₋ₖⱼ, over
  1 ≤ k ≤ n and j ≥ 1. The code runs d = −k over `range(-n,0)`: `a[-d]` is
  aₖ, and since the list holds a₀ … aₙ, the slice `a[d:0:d]` is aₙ₊₁₋ₖ,
  aₙ₊₁₋₂ₖ, … and stops before index 0. With d negative the sum comes out as
  −n·aₙ₊₁/2, so `2*…//-n` is an exact division that also fixes the sign.
- The unrooted count is Pab Ter's formula from the OEIS entry,
  **S(x) − S(x)² + S(x²)**. It follows from Otter's dissimilarity theorem
  (node classes − edge classes + symmetric edge = 1): trees rooted at a node
  give S. Trees rooted at an edge give S² + S(x²): the edge has one of 2
  signs and cuts the tree into an unordered pair of rooted trees. The
  symmetric edges, with two equal halves, give 2·S(x²).
- In coefficients this is aₙ − Σ aᵢ·aₙ₋ᵢ + aₙ/₂, with i from 1 to n − 1 and
  the last term only for even n. The printed sum is
  Σ aᵢ·([2i = n] − aₙ₋ᵢ) over i < n. `a[~i]` is aₙ₋ᵢ because the list has
  n + 1 entries, and `(2*i==n)` adds aₙ/₂.
- `a[0]` is −1 rather than 0, so the i = 0 term is −1·(0 − aₙ) = aₙ and the
  S term needs no code of its own. That is why the slice stops at `:0`.
- `while[print(…)]` prints a(n) and loops forever, because `[None]` is a
  non-empty list. `a+=…,` appends aₙ₊₁ as a one-tuple.

**Notes**

- Every step is exact integer arithmetic, and the division is always exact.
- Each term costs about n log n steps. The whole b-file (500 terms) prints
  in about 0.2 s, 1000 terms in about 1.3 s and 2000 in about 15 s. The bar
  is the whole b-file in 60 s.
- a(n) grows about 5.6ⁿ, so from about n = 5700 its decimal form passes
  Python's 4300-digit int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 131 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000060), CC BY-SA 4.0.
