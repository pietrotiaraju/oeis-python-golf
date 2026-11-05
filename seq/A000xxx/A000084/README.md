# A000084

> Number of series-parallel networks with n unlabeled edges. Also called yoke-chains by Cayley and MacMahon.
> — [OEIS A000084](https://oeis.org/A000084)

Offset 1: 1, 2, 4, 10, 24, 66, 180, 522, 1532, 4624, 14136, 43930, 137908, 437502, 1399068, 4507352, …

### Python 3 — 91 bytes

```python
A=[1,n:=1]
while[print(A[n])]:n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
```

**How it works**

- The formula from the OEIS page: 1 + Σ a(n)·xⁿ = Π_k (1 − x^k)^(−b(k)),
  where b is [A000669](https://oeis.org/A000669) (series-reduced planted
  trees), with b(1) = 1 and a(n) = 2·b(n) for n > 1. So 1 + A(x) is the
  Euler transform of b.
- The Euler transform recurrence, with a(0) = 1, is
  **n·a(n) = Σ_d d·b(d)·Σ_{j≥1} a(n − jd)**, summed over 1 ≤ d ≤ n. The
  d = n term is n·b(n)·a(0) = n·a(n)/2, so moving it to the left gives
  **n·a(n) = Σ_{d<n} 2d·b(d)·Σ_{j≥1} a(n − jd)**.
- For d ≥ 2 the weight 2d·b(d) is d·a(d). For d = 1 it is 2 = 2·1·a(1),
  so the d = 1 term simply counts twice: `d` runs over the tuple
  `(1,*range(1,n))` = 1, 1, 2, …, n − 1. That is 3 bytes shorter than
  doubling it with a shift, `…*d*A[d]<<1//d for d in range(1,n)`.
- `A` holds a(0) … a(n − 1) when a(n) is computed, so `A[-d]` is a(n − d)
  and the slice `A[-d::-d]` walks down to index 0 in steps of d: the
  inner sum Σ_{j≥1} a(n − jd).
- `A=[1,n:=1]` sets a(0) = a(1) = 1 and n = 1 in one statement, a byte
  shorter than `A=[1,1];n=1`. `while[print(…)]` prints and loops forever
  because `[None]` is a non-empty list; `A+=…,` appends a one-tuple.

**Notes**

- Exact integer arithmetic, so the program is right for every n: the sum
  is n·a(n), so `//n` is exact.
- Each term costs O(n log n) big-integer additions, so the whole b-file
  (1001 terms) prints in about half a second and about 4000 terms print
  in 60 s. The bar is the whole b-file in 60 s.
- a(n) ~ C·dⁿ·n^(−3/2) with d = 3.5608… (Riordan, Shannon, Moon), so from
  about n = 7808 its decimal form passes Python's 4300-digit int-to-str
  limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000084), CC BY-SA 4.0.
