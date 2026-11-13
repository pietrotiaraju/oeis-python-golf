# A001560

> Numbers with an even number of partitions.
> — [OEIS A001560](https://oeis.org/A001560)

Offset 1: 2, 8, 9, 10, 11, 15, 19, 21, 22, 25, 26, 27, 28, 30, 31, 34, 40, 42, 45, 46, …

### Python 3 — 86 bytes

```python
*a,n=1,0
while[a[-1]%2or print(-n)]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- The partition numbers p(N) come from the recurrence of the
  [A000041](../../A000xxx/A000041/) record, **N·p(N) = Σ σ(k)·p(N − k)**
  for k = 1…N, with σ(k) written as the sum of its divisors d:
  N·p(N) = Σ_d d·Σ_j p(N − dj). `a` holds p(0), …, p(N − 1) and `n` is −N,
  so the slice `a[d::d]` with d = −1…−N walks back from p(N − |d|) in steps
  of |d|, and `//n` divides the (negative) sum by −N exactly.
- The loop condition tests the newest term instead of printing it:
  `a[-1]%2` is 1 for an odd p(N), and only for an even one does
  `or print(-n)` print N. The first test sees p(0) = 1, so 0 is never
  printed; the first output is 2, since p(2) = 2.
- The answer is the parity of p(N), but the division by N in the
  recurrence needs the full value, so the terms are kept as exact integers.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file ends at a(1000) = 2024; p(2024) has 46 digits and the whole
  b-file prints in about 2.5 s here. The bar is the whole b-file.
- Euler's pentagonal recurrence works modulo 2 (the signs drop out:
  p(N) ≡ Σ p(N − g) over the generalized pentagonal numbers g ≤ N), but
  generating those g costs more bytes than the divisor-sum recurrence.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001560), CC BY-SA 4.0.
