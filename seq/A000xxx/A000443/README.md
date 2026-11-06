# A000443

> Numbers that are the sum of 2 squares in exactly 3 ways.
> — [OEIS A000443](https://oeis.org/A000443)

Offset 1: 325, 425, 625, 650, 725, 845, 850, 925, 1025, 1250, …

### Python 3 — 118 bytes

```python
n=k=0;s=[];d={}
while 1:
 if n==k*k:
  s+=[n];k+=1
  for x in s:d[n+x]=d.get(n+x,0)+1
 if d.get(n,0)==3:print(n)
 n+=1
```

**How it works**

- Representations use **nonnegative** roots, ignoring their order and
  signs: a pair is counted once as x²+y² with 0≤x≤y. Zero is
  allowed here, unlike in [A000404](../A000404/).
- `n` scans candidate integers and k tracks the next square root.
  At `n==k*k`, append the new largest square n to the increasing
  list s, then pair it with every x in s. Each unordered pair is
  encountered exactly once, when its larger square becomes available.
- `d[n+x]=d.get(n+x,0)+1` increments its sum's representation
  count. Inserting n into s first includes the equal pair n+n;
  the initial n=k=0 includes the zero square as well.
- At the final test for n, every possible summand of a representation
  of n is at most n and has been inserted. The counter is complete,
  even though d also contains partial counts for larger integers.
  Print exactly when `d.get(n,0)==3`.

**Notes**

- For the first term, 325=1²+18²=6²+17²=10²+15².
  The later term 625 also counts 0²+25², alongside 7²+24² and
  15²+20²: omitting zero would change the sequence.
- Exact integer counting. The scan prints a value once, independently
  of the three pairs that caused its counter to reach 3.
- Through candidate N there are O(N) unordered pairs of square roots
  to insert. Their sums are at most 2N, so the dictionary uses O(N)
  entries; the square list has only O(√N) entries.
- [A000437](../A000437/) extends this largest-square construction
  to triples and asks for the smallest value at each exact count.
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000443), CC BY-SA 4.0.
