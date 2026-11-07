# A000437

> Smallest nonnegative number that is the sum of 3 squares in exactly n ways.
> — [OEIS A000437](https://oeis.org/A000437)

Offset 1: 0, 9, 41, 81, 146, 194, 306, 369, 425, 594, …

The ways are unordered and may use 0: m = x² + y² + z² with x ≥ y ≥ z ≥ 0.
So 0 = 0² + 0² + 0² has one way, and 9 = 3² + 0² + 0² = 2² + 2² + 1² is the
first number with two.

### Python 3 — 135 bytes

```python
n=1;c=[k:=0]
while 1:
 for x in range(k+1):
  for y in range(x+1):c[x*x+y*y+k*k]+=1
 k+=1;c+=[0]*6*k;n+=n in c[:k*k]!=print(c.index(n))
```

**How it works**

- `c[m]` counts the ways m = k² + x² + y² with k ≥ x ≥ y ≥ 0, filled in
  rounds k = 0, 1, 2, …: round k adds the ways whose largest square is k²
  (the two loops run over x ≤ k and y ≤ x).
- After round k − 1, when `k+=1` has made the counter k, every m < k² is
  final: the largest square in a way of writing m is at most m < k², so it
  is one of 0², …, (k−1)², and all of those rounds are done. So `c[:k*k]`
  holds true counts.
- If n occurs in that prefix, its first occurrence in c lies there and
  every earlier entry is a final count other than n, so `c.index(n)` is
  a(n). The chain `n in c[:k*k]!=print(c.index(n))` means
  `n in c[:k*k] and c[:k*k]!=print(…)`: print runs only when the test
  holds, its `None` makes the second comparison true, and `n+=` adds
  True = 1 (on to the next n) or False = 0.
- At most one term is printed per round, so the output can lag behind
  what is already known; but once a(n) < k² it stays in the final prefix
  and comes out in a later round, so the terms appear in order.
- Room: c starts as [0] and gains 6k zeros when the counter becomes k, so
  in round k it has 1 + 3k(k+1) entries, more than the largest index 3k²
  written there. `c=[k:=0]` sets k inside the list.

**Notes**

- Measured alternatives: growing c by `c+=0,0;` in the inner loop instead
  of `c+=[0]*6*k`, 131 bytes, but that ties the room to the number of
  triples, about k³/3 entries by round k, and needs several GB within a
  minute; a separate line `while n in c[:k*k]:print(c.index(n));n+=1`
  that prints every ready term at once, 147. The previous dictionary
  sieve was 197.
- Counting is exact, so the program is right for every n. If no number
  had exactly n ways, a(n) would not exist and the program would wait
  there forever.
- Recording the first m with at least n ways instead gives
  [A000451](../A000451/); [A000443](../A000443/) counts sums of two
  squares in the same rounds.
- The whole b-file prints in about 0.3 s here, and about 327 terms in
  60 s. The b-file has 43 terms (up to a(43)); the bar is the whole
  b-file in 60 s.
- The values are small (a(43) = 8774), far from the 4300-digit
  int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 197 | first entry |
| 2026-11-07 | Python 3 | 135 | count rounds by largest square in a list, print the first final index |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000437), CC BY-SA 4.0.
