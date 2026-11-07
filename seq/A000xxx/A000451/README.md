# A000451

> Smallest number that is the sum of 3 squares in at least n ways.
> — [OEIS A000451](https://oeis.org/A000451)

Offset 1: 0, 9, 41, 81, 146, 194, 306, 369, 425, 594, …

Representations m = x² + y² + z² are counted with 0 ≤ x ≤ y ≤ z (zeros
allowed, order and signs ignored); a(n) is the least m with at least n of
them.

### Python 3 — 145 bytes

```python
P=[];c=[0];n=k=t=0
while 1:
 if n==k*k:
  P+=[n+j*j for j in range(k+1)];c+=[0]*9*k;k+=1
  for p in P:c[n+p]+=1
 while t<c[n]:print(n);t+=1
 n+=1
```

**How it works**

- **Counting by the largest square.** `c[m]` counts the triples with sum
  m found so far, and `P` is the multiset of pair sums x² + y² with
  x ≤ y ≤ the current square. When n reaches the square k², the pairs
  (j², k²) for j ≤ k join P, and every triple whose largest square is k²
  is k² + p for one p in P, so `c[n+p]+=1` adds each such triple exactly
  once.
- **When a count is final.** Every square in a triple with sum n is at
  most n, so by the time the scan reaches n all its triples are in, and
  `c[n]` is its number of representations (larger sums can still grow).
- **Printing.** t is the number of thresholds already answered. If n has
  c[n] > t representations, it is the least number for every threshold
  t+1, …, c[n] not answered yet, so it is printed that many times (a
  record can jump several thresholds). For n = 0 the triple (0, 0, 0)
  gives a(1) = 0.
- **The count list.** `c+=[0]*9*k` keeps c long enough: after the square
  k², c has 1 + 9·k(k+1)/2 ≥ 3k² + 1 entries, and the largest new sum is
  3k².

**Notes**

- Other versions that print the same terms: a dict and the pairs
  rebuilt from a list of squares for each new square, with a threshold
  counter `t=1` and `<=`, the first version: 168 bytes and 3.5 times
  slower.
- Exact integer arithmetic, so the program is right for every n.
- About 520 terms in 60 s here; the b-file's 200 terms (up to 162686)
  take 3 s. Up to N the program handles about N^(3/2)/6 triples. The
  b-file has 200 terms (up to a(200)); the bar is the whole b-file in
  60 s.
- [A000437](../A000437/) asks for exactly n representations instead.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 168 | first entry |
| 2026-11-07 | Python 3 | 145 | multiset of pair sums and a count list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000451), CC BY-SA 4.0.
