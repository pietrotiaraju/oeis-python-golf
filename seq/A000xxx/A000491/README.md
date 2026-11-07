# A000491

> Number of bipartite partitions of n white objects and 5 black ones.
> — [OEIS A000491](https://oeis.org/A000491)

Offset 0: 7, 19, 47, 97, 189, 339, 589, 975, 1576, 2472, …

a(n) is the number of multiset partitions of the multiset {wⁿ, b⁵}, or the
number of ways to factor pⁿq⁵ for distinct primes p, q.

### Python 3 — 171 bytes

```python
*a,n=1,0;Q=[k*[0]for k in range(1,6)]
while t:=a[-1]:
 for L in Q:L+=(t:=t+L.pop(0)),
 print(sum(sum(Q[:4]+Q[1:3],[t])));n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- A part is a pair (i, j) ≠ (0, 0) of white and black counts, so the
  bivariate g.f. is Π 1/(1 − xⁱyʲ). The parts with j = 0 give
  P(x) = Π 1/(1 − xⁱ). For the others, a partition λ of 5 with m_j parts
  equal to j contributes Π_j 1/D_{m_j}(x), where D_m = (1 − x)…(1 − x^m)
  counts multisets of m white counts (Euler's q-binomial identity). The seven
  partitions of 5 give
  a(n) = [xⁿ] P·(1/D₁ + 2/D₁² + 2/(D₁D₂) + 1/(D₁D₃) + 1/D₅).
- With Uₖ = 1/(1 − xᵏ) and hᵣ = P/Dᵣ = Uᵣh_{r−1} (h₀ = P) this is
  a(n) = [xⁿ] (U₁h₀ + 2U₁h₁ + 2U₁h₂ + U₁h₃ + h₅).
- `Q` is a chain of five filters, the k-th a queue of length k that divides
  its input stream by 1 − xᵏ: the output is the input plus the output k steps
  earlier, popped from the front, and the new output is appended. Fed
  p(m), the stages output h₁(m), …, h₅(m), and `t` ends as h₅(m).
- After the appends, queue k holds the last k outputs of its stage, and
  their sum is [xᵐ](1 + x + … + x^(k−1))·Uₖ(input) = [xᵐ] U₁(input), because
  (1 + … + x^(k−1))/(1 − xᵏ) = 1/(1 − x). So the sums of queues 1, 2, 3, 4
  are U₁h₀, U₁h₁, U₁h₂, U₁h₃, and `sum(Q[:4]+Q[1:3],[t])` flattens queues
  1–4, queues 2–3 a second time and h₅ into one list: the sum is a(m).
- The partition numbers come from the [A000041](../A000041/) program:
  m·p(m) = Σ_k σ(k)·p(m−k) as `sum(d*sum(a[d::d])…)//n` with n = −m and
  d = −k. `while t:=a[-1]:` reads the newest p(m), which is never 0.

**Notes**

- Other versions: one comprehension that stores the five outputs and an
  extra running sum for the U₁ part, 193 bytes; the same with the weights
  2, 2, 1, 0, 0 as `2>>len(L)**2//8` inside the chain, 188 bytes.
- Exact integer arithmetic, so the program is right for every n. A direct
  count of the multiset partitions agrees for n ≤ 9.
- About 8000 terms in 60 s here. The b-file has 1001 terms (up to a(1000));
  the bar is the whole b-file in 60 s, which takes about 1 s.
- a(n) has about 1.1√n digits, so the 4300-digit int-to-str limit is out of
  reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 296 | first entry |
| 2026-11-06 | Python 3 | 284 | use sumprod on padded coefficient history and combine queue updates |
| 2026-11-06 | Python 3 | 193 | accumulate the five black-partition filters directly |
| 2026-11-07 | Python 3 | 171 | read the U₁ terms off the queue sums |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000491), CC BY-SA 4.0.
