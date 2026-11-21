# A002133

> Number of partitions of n with exactly two part sizes.
> — [OEIS A002133](https://oeis.org/A002133)

Offset 1: 0, 0, 1, 2, 5, 6, 11, 13, 17, 22, 27, 29, …

### Python 3 — 92 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum((n-u)%j<1for i in r for u in range(i,n,i)for j in r[i:]))
```

**How it works**

- A partition of n with exactly two part sizes i < j uses i some x ≥ 1
  times and j some y ≥ 1 times, with x·i + y·j = n. So a(n) counts the
  triples (i, j, u) with i < j, u = x·i a positive multiple of i below n,
  and j dividing n − u.
- `r` is the list being looped over, and each pass appends n+1 to it, so
  the `for` never ends and r holds 1, …, n+1 (the loop of
  [A000203](../../A000xxx/A000203/)). `r[i:]` is i+1, …, n+1, the sizes
  j > i; n − u ≥ 1, so `(n-u)%j<1` holds only for divisors j ≤ n − u.
- Every partition is counted once, by its two sizes and the part of n
  they each take.

**Notes**

- Integer arithmetic only, so it is correct for every n.
- A term costs about n²·ln n steps. The b-file has 10000 terms; the bar
  is 370 terms in 60 s, about 20 s here. The entry's g.f.
  (G(x)² − H(x))/2 gives a(n) = (Σ τ(k)τ(n−k) − σ(n) + τ(n))/2 in O(n)
  steps a term, but costs about 35 bytes more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002133), CC BY-SA 4.0.
