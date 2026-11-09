# A001237

> Differences of reciprocals of unity.
> — [OEIS A001237](https://oeis.org/A001237)

Offset 1: 31, 3661, 1217776, 929081776, 1413470290176, 3878864920694016, 17810567950611972096, 129089983180418186674176, …

### Python 3 — 81 bytes

```python
g=[1]*4;f=1;N=2
while 1:s=t=1;g=[s:=(t:=t*N)*x+f*s for x in g];print(s);f*=N;N+=1
```

**How it works**

- With N = n + 1 the term is N!⁴·h₄(1, 1/2, …, 1/N), the sum of 1/(ijkl)
  over N ≥ i ≥ j ≥ k ≥ l ≥ 1 (OEIS formula).
- Adding the variable 1/N gives hᵣ(N) = hᵣ(N−1) + hᵣ₋₁(N)/N, so with
  gᵣ = N!ʳ·hᵣ: gᵣ(N) = Nʳ·gᵣ(N−1) + (N−1)!·gᵣ₋₁(N), with g₀ = 1.
- `g` holds g₁…g₄ and `f` is (N−1)!. The comprehension walks r = 1…4 with
  `t` = Nʳ and `s` = the new gᵣ₋₁ (starting from g₀ = 1), so its last `s`
  is g₄. All gᵣ(1) are 1.

**Notes**

- The whole b-file (12 terms) prints at once.
- The nested-walrus chain of [A001236](../A001236/) is 89 bytes here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001237), CC BY-SA 4.0.
