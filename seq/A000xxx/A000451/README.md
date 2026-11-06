# A000451

> Smallest number that is the sum of 3 squares in at least n ways.
> — [OEIS A000451](https://oeis.org/A000451)

Offset 1: 0, 9, 41, 81, 146, 194, 306, 369, 425, 594, …

### Python 3 — 168 bytes

```python
n=k=0;s=[];d={};t=1
while 1:
 if n==k*k:
  s+=[n];k+=1
  for i,x in enumerate(s):
   for y in s[:i+1]:d[n+x+y]=d.get(n+x+y,0)+1
 while t<=d.get(n,0):print(n);t+=1
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

- t is the next requested minimum number of representations.
  If the current n has c≥t representations, n is the smallest
  qualifying value for every as-yet-unprinted threshold through c.
  `while t<=d.get(n,0)` prints n for all those thresholds.
- If a new count record jumps over several thresholds, repeating n
  is necessary. Once printed, a threshold needs no stored answer:
  the scan will never find a smaller candidate later.

**Notes**

- This is the “at least” counterpart of [A000437](../A000437/).
  Its outputs are nondecreasing; requiring exactly t ways can have
  a different minimum and does not have that monotonicity guarantee.
- The initial triple (0,0,0) gives a(1)=0. The next threshold
  is reached at 9=0²+0²+3²=1²+2²+2², giving a(2)=9.

- Exact integer counting, with no cutoff on the number of roots.
  Through candidate N the construction inserts O(N^(3/2)) triples;
  their sums are at most 3N, so d has O(N) possible keys. The
  temporary slices also contribute to the running time.
- The b-file has 200 terms (indices 1 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 168 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000451), CC BY-SA 4.0.
