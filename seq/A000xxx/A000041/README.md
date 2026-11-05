# A000041

> a(n) is the number of partitions of n (the partition numbers).
> — [OEIS A000041](https://oeis.org/A000041)

Offset 0: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, …

### Python 3 — 79 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- Taking the log derivative of Π 1/(1 − xᵏ) gives the recurrence on the OEIS
  page, **N·a(N) = Σ σ(k)·a(N − k)** for k = 1…N, where σ is the sum of
  divisors. Writing σ(k) as the sum of its divisors d and grouping by d
  turns it into **N·a(N) = Σ_d d·Σ_j a(N − dj)** over d = 1…N and j ≥ 1
  with dj ≤ N, so no divisors are ever computed.
- `a` is [a(0), …, a(N − 1)] and `n` is −N, so `d` runs over −N…−1. The
  slice `a[d::d]` starts |d| places from the end and steps back by |d|:
  exactly a(N − |d|), a(N − 2|d|), …. Summing `d*sum(…)` gives −N·a(N), and
  `//n` divides by −N. The division is exact.
- Negative `d` is what makes this short: it indexes from the end of the list
  for free, and `range(n,0)` and `//n` need no minus signs.
- `*a,n=1,0` sets a = [1] and n = 0 in 8 bytes. `while[print(...)]:` prints
  in the loop condition (`[None]` is true), and `n-=1` steps n before the
  term is computed.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.1·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 1.5·10⁷, far beyond what the program gets to.
- Term N costs N Python steps plus about N·ln N additions inside the slice
  sums. The whole b-file (10 001 terms) prints in 30 to 40 s here and 5000
  terms in about 8 s; the bar is 5000 terms in 60 s, which leaves room for
  slower machines.
- Counting n up instead (`a=[n:=1]`, `range(-n,0)`, `//-n`, `;n+=1`) is
  81 bytes.
- Euler's pentagonal-number recurrence is faster, but its signs and the
  missing negative indices make it longer: a dict with `a.get(…,0)` over
  k = −n…n − 1 is 99 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000041), CC BY-SA 4.0.
