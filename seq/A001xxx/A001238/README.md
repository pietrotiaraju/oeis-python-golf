# A001238

> Differences of reciprocals of unity.
> — [OEIS A001238](https://oeis.org/A001238)

Offset 1: 63, 22631, 30480800, 117550462624, 1083688832185344, 21006340945438768128, 778101042571221893382144, …

### Python 3 — 81 bytes

```python
g=[1]*5;f=1;N=2
while 1:s=t=1;g=[s:=(t:=t*N)*x+f*s for x in g];print(s);f*=N;N+=1
```

**How it works**

- With N = n + 1 the term is N!⁵·h₅(1, 1/2, …, 1/N), the sum of
  1/(i₁⋯i₅) over N ≥ i₁ ≥ ⋯ ≥ i₅ ≥ 1, which equals the OEIS formula
  N!⁵·Σ (−1)^(k+1)·C(N,k)/k⁵.
- Adding the variable 1/N gives hᵣ(N) = hᵣ(N−1) + hᵣ₋₁(N)/N, so with
  gᵣ = N!ʳ·hᵣ: gᵣ(N) = Nʳ·gᵣ(N−1) + (N−1)!·gᵣ₋₁(N), with g₀ = 1.
- `g` holds g₁…g₅ and `f` is (N−1)!. The comprehension walks r = 1…5 with
  `t` = Nʳ and `s` = the new gᵣ₋₁ (starting from g₀ = 1), so its last `s`
  is g₅. All gᵣ(1) are 1.

**Notes**

- The whole b-file (10 terms) prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001238), CC BY-SA 4.0.
