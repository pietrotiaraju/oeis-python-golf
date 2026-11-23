# A002212

> Number of restricted hexagonal polyominoes with n cells.
> — [OEIS A002212](https://oeis.org/A002212)

Offset 0: 1, 1, 3, 10, 36, 137, 543, 2219, 9285, 39587, 171369, 751236, …

### Python 3 — 61 bytes

```python
x=y=n=1
while[print(x)]:n+=1;x,y=y,((6*n-3)*y-5*(n-2)*x)//-~n
```

**How it works**

- **Generating function.** The entry's g.f. is
  A(x) = (1 − x − S)/(2x) with S = √((1 − x)(1 − 5x)), the root of
  xA² − (1 − x)A + (1 − x) = 0 with A(0) = 1 (Harary and Read's count of
  these polyhexes; the same numbers count 3-Motzkin paths, skew Dyck paths
  and the other objects in the entry's comments).
- **Recurrence.** S² = 1 − 6x + 5x², so (1 − 6x + 5x²)S′ = (5x − 3)S.
  Comparing coefficients of xᵐ gives
  (m + 1)sₘ₊₁ = (6m − 3)sₘ − (5m − 10)sₘ₋₁, and since 2x·A = 1 − x − S,
  sₖ = −2a(k − 1) for k ≥ 2. Shifting the index:
  (n + 1)·a(n) = 3(2n − 1)·a(n − 1) − 5(n − 2)·a(n − 2) for n ≥ 2 (at
  n = 2 the a(0) term has coefficient 0, so it holds there too). This is
  the D-finite recurrence in the entry.
- **The loop.** `x`, `y` hold a(n − 2), a(n − 1); each pass prints `x`,
  steps n and slides the pair on. The division is exact because the
  left side is (n + 1)·a(n); `//-~n` divides by n + 1.

**Notes**

- Exact integers: right for every n. The whole b-file (201 terms, n = 0 to
  200) takes a few hundredths of a second; the bar is all of it in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002212), CC BY-SA 4.0.
