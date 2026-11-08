# A000929

> Dimension of the n-th graded piece of the mod-2 Steenrod algebra A_2.
> — [OEIS A000929](https://oeis.org/A000929)

Offset 0: 1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 11, 12, 13, 15, 16, …

### Python 3 — 77 bytes

```python
f=lambda n,k=1:n>=k and f(n-k,k)+f(n,k-~k)or n<1
n=0
while[print(+f(n))]:n+=1
```

**How it works**

- The g.f. ∏ 1/(1 − x^(2^k−1)) counts partitions of n into parts 1, 3,
  7, 15, …, the numbers 2^k − 1 (the Milnor basis elements Sq(r₁, r₂, …)
  of degree Σ rᵢ(2^i − 1)).
- `f(n,k)` counts partitions of n into parts from k, 2k + 1, 4k + 3, …
  (all of the form 2^i − 1 when k is): either one part is k, or k is not
  used and the smallest allowed part becomes 2k + 1, written `k-~k`. This
  is Zumkeller's formula in the entry.
- When k > n the only partition left is the empty one, so the value is
  n = 0, the `or n<1`. If the sum is 0 for some n ≥ k, the `or` gives
  `False` = 0 too, which is right. The top call f(0) is `True`, printed
  as 1 by `+f(n)`.

**Notes**

- Exact integers, but the recursion has one leaf per partition (and a
  few dead ends per part size), so the time grows like a(n) itself:
  267 terms in 60 s here, a(266) = 51636. The b-file has 10001 terms; the
  bar is 210.
- The Euler-transform recurrence of [A000041](../A000041/) with the
  parts filtered by k & (k + 1) = 0 prints the whole b-file in about 15 s
  but is 89 bytes:
  `*a,n=1,0` / `while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0)if-d&1-d<1)//n,`
  (d = −k, so `-d&1-d` is k & (k + 1)).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000929), CC BY-SA 4.0.
