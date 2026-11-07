# A000716

> Number of partitions of n into parts of 3 kinds.
> — [OEIS A000716](https://oeis.org/A000716)

Offset 0: 1, 3, 9, 22, 51, 108, 221, 429, 810, 1479, 2640, 4599, 7868, 13209, 21843, …

### Python 3 — 81 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=3*sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- The g.f. is Π 1/(1 − xᵏ)³, the Euler transform of b = [3, 3, 3, …]. Its
  log derivative gives **N·a(N) = 3·Σ_d d·Σ_j a(N − dj)** over d = 1…N
  and j ≥ 1 with dj ≤ N (the OEIS formula a(N) = (3/N)·Σ σ(k)·a(N − k)
  with the divisor sum grouped by d).
- This is the [A000041](../A000041/) program with `3*` in front of the sum,
  as [A000712](../A000712/) has `2*`. `n` is −N, `d` runs over −N…−1, and
  the slice `a[d::d]` is a(N − |d|), a(N − 2|d|), …; `//n` divides −N·a(N)
  by −N, and the division is exact.
- Jacobi's identity Π(1 − xᵏ)³ = Σ (−1)ᵏ(2k + 1)·x^(k(k+1)/2) gives a
  sparse recurrence that is much faster, but stopping its sum at the
  triangular numbers ≤ N costs more than it saves.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.93·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 5·10⁶.
- Term N costs N Python steps plus about N·ln N additions inside the slice
  sums: 8300–8700 terms in 60 s here. The b-file has 10 001 terms; the bar is
  6500 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000716), CC BY-SA 4.0.
