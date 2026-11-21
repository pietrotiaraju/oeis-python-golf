# A002134

> Generalized divisor function. Number of partitions of n with exactly three part sizes.
> — [OEIS A002134](https://oeis.org/A002134)

Offset 6: 1, 2, 5, 10, 15, 25, 37, 52, 67, 97, 117, 154, …

### Python 3 — 123 bytes

```python
f=lambda n,k=3,j=1:sum(f(n-e,k-1,i+1)for i in range(j,n+1)for e in range(i,n+1,i))if k else n<1
n=6
while[print(f(n))]:n+=1
```

**How it works**

- `f(n,k,j)` counts the ways to write n with exactly k part sizes, all at
  least j, each used at least once: the smallest size i ≥ j takes
  e = i, 2i, 3i, … ≤ n, and the rest is n − e with k − 1 sizes above i.
  With k = 0 only n = 0 is left, which `n<1` counts (n − e is never
  negative).
- So `f(n)` = f(n, 3, 1) is the number of partitions of n with exactly
  three part sizes, which is also MacMahon's generalized divisor function
  Σ_{0<i<j<l} q^(i+j+l)/((1−q^i)(1−q^j)(1−q^l)) of the entry's g.f.
- The loop starts at the offset, n = 6 = 1 + 2 + 3; `while[print(…)]:`
  prints before each step.

**Notes**

- Integer arithmetic only, so it is correct for every n; the recursion is
  only three levels deep.
- A term costs about (n·ln n)³/6 calls. The b-file has 9995 terms; the
  bar is 95 terms in 60 s, about 20 s here. Memoizing `f` with
  `functools.cache` (30 bytes more) reaches several hundred terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 123 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002134), CC BY-SA 4.0.
