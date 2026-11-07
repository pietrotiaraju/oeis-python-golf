# A000443

> Numbers that are the sum of 2 squares in exactly 3 ways.
> — [OEIS A000443](https://oeis.org/A000443)

Offset 1: 325, 425, 625, 650, 725, 845, 850, 925, 1025, 1250, …

The ways are unordered and may use 0: m = x² + y² with x ≥ y ≥ 0. The first
term is 325 = 18² + 1² = 17² + 6² = 15² + 10², and 625 = 25² + 0² = 24² + 7²
= 20² + 15² shows that 0 counts.

### Python 3 — 99 bytes

```python
c=[k:=0]
while 1:
 for x in range(k-~k):c[x*x+k*k]+=x<=k;c[m:=k*k+x]==3==print(m)
 k+=1;c+=[0]*10*k
```

**How it works**

- `c[s]` counts the ways s = k² + x² with k ≥ x ≥ 0, added in rounds
  k = 0, 1, 2, …: round k adds the ways whose larger square is k².
- The same round tests the numbers m = k² + x for x = 0, …, 2k
  (`range(k-~k)` is range(2k + 1)), that is every m with
  k² ≤ m < (k + 1)². Their ways have larger part at most k. Those with a
  smaller larger part came in earlier rounds, and the way m = k² + a² is
  added in iteration x = a, before m is tested in iteration x = a² ≥ a
  (for a = 0 and 1 that is the same iteration, and the write comes
  first). So each m is tested once, with its final count, in increasing
  order.
- `c[x*x+k*k]+=x<=k` adds 1 for x ≤ k and False = 0 for the x > k that
  the loop also visits. `c[m:=k*k+x]==3==print(m)` is
  `c[m]==3 and 3==print(m)`: m is printed exactly when its count is 3.
- Room: the largest index is (2k)² + k² = 5k², from a write of 0. c
  starts as [0] and gains 10k zeros when the counter becomes k, so in
  round k it has 1 + 5k(k + 1) entries. `c=[k:=0]` sets k inside the list.

**Notes**

- `c=[0];k=0` costs one byte more (100). The previous dictionary scan,
  which added the pairs when it reached their larger square, was 118.
- Counting is exact, so the program is right for every term.
- The whole b-file prints in about 1.6 s here (3.2 s with the PC busy),
  and about 46700 terms (up to about 7.9 million) in 10 s. The list holds
  about 5k² entries while scanning up to k², roughly 40 bytes per number
  scanned: about 0.3 GB after 10 s, and on the order of 2 GB in a minute.
- [A000437](../A000437/) counts sums of three squares in the same rounds.
- The b-file has 10000 terms (up to a(10000) = 1253682); the bar is the
  whole b-file in 60 s.
- The terms grow about linearly, far from the 4300-digit int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 118 | first entry |
| 2026-11-07 | Python 3 | 99 | one pass per largest square: count and test in the same loop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000443), CC BY-SA 4.0.
