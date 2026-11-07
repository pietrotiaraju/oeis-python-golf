# A000992

> "Half-Catalan numbers": a(n) = Sum_{k=1..floor(n/2)} a(k)*a(n-k) with a(1) = 1.
> — [OEIS A000992](https://oeis.org/A000992)

Offset 1: 1, 1, 1, 2, 3, 6, 11, 24, 47, 103, 214, 481, 1030, 2337, 5131, 11813, …

### Python 3 — 72 bytes

```python
L=[1]
while[print(L[-1])]:L+=sum(L[i]*L[~i]for i in range(-~len(L)//2)),
```

**How it works**

- Straight from the definition. `L` holds a(1), …, a(n−1), so for the
  next index n = len(L) + 1 the pairs are a(k)·a(n−k), k = 1 … ⌊n/2⌋.
  With i = k − 1, a(k) is `L[i]` and a(n−k) is `L[~i]` (= L[len−1−i]),
  and ⌊n/2⌋ = ⌊(len + 1)/2⌋ is `-~len(L)//2`.
- `print(L[-1])` in the loop condition prints the newest term (the
  [A000007](../A000007/) loop), starting with a(1) = 1.

**Notes**

- Exact integers, about n/2 multiplications per term. The b-file has 2500
  terms (up to about 990 digits) and prints in about 4 s; the bar is the
  whole b-file.
- `sum(map(int.__mul__,L,L[:-len(L)//2-1:-1]))` (the reversed half as one
  slice; map stops at the shorter list) is 2 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 72 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000992), CC BY-SA 4.0.
