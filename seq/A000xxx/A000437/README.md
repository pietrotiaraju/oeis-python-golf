# A000437

> Smallest nonnegative number that is the sum of 3 squares in exactly n ways.
> — [OEIS A000437](https://oeis.org/A000437)

Offset 1: 0, 9, 41, 81, 146, 194, 306, 369, 425, 594, …

### Python 3 — 197 bytes

```python
n=k=0;s=[];d={};a={};t=1
while 1:
 if n==k*k:
  s+=[n];k+=1
  for i,x in enumerate(s):
   for y in s[:i+1]:d[n+x+y]=d.get(n+x+y,0)+1
 a.setdefault(d.get(n,0),n)
 while t in a:print(a[t]);t+=1
 n+=1
```

**How it works**

- Count representations x²+y²+z² with 0≤x≤y≤z: zero is
  allowed, and permutations or choices of signs do not create
  extra representations. The increasing list s contains squares.
- When `n==k*k`, append the new largest square n. For each
  `i,x` in s, `s[:i+1]` supplies y≤x. Thus every triple is
  inserted once, with n as its largest square, including triples
  having repeated or zero squares.
- The dictionary d counts triples by their sum. At candidate n
  all triples summing to n have already been inserted, because
  no summand can exceed n. `d.get(n,0)` is therefore its final
  count; dictionary entries for larger values can still grow.

- `a.setdefault(d.get(n,0),n)` saves the first candidate seen
  for each exact representation count, never overwriting it.
  This makes each stored answer a minimum by construction.
- t is the next required count. Print `a[t]` only once it has
  been discovered, then drain any consecutive counts already in a.
  A minimum for a larger count can be discovered before a smaller
  count's minimum, so discovery order is not output order.

**Notes**

- Initially (0,0,0) is the unique representation of 0, giving
  a(1)=0. At 9 the two triples (0,0,3) and (1,2,2) give a(2)=9.
- The dictionary a is indexed by counts, not candidate integers.
  Recording just successive count records would instead give
  the “at least” sequence [A000451](../A000451/).

- Exact integer counting, with no cutoff on the number of roots.
  Through candidate N the construction inserts O(N^(3/2)) triples;
  their sums are at most 3N, so d has O(N) possible keys. The
  temporary slices also contribute to the running time.
- The b-file has 43 terms (indices 1 through 43). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 197 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000437), CC BY-SA 4.0.
