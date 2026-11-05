# A300001

> Side length of the smallest equilateral triangle that can be dissected into
> n equilateral triangles with integer sides, or 0 if no such triangle exists.
> — [OEIS A300001](https://oeis.org/A300001)

Offset 1: 1, 0, 0, 2, 0, 3, 4, 4, 3, 4, 5, 6, 4, 5, 6, 4, …

### Python 3 — 71 bytes

```python
n=0
while 1:
 n+=1;s=0
 while(9399<<n)+~(44>>n&1)>>s*s&1:s+=1
 print(s)
```

**The rule**

> a(n) is the smallest s with s² ≥ n and s² − n not in {1, 2, 4, 5, 7, 10, 13},
> except a(2) = a(3) = a(5) = 0.

- **No smaller side works (any n).** Areas add up: s² = Σkᵢ² over the n
  pieces, so s² − n = Σ(kᵢ² − 1). Each kᵢ² − 1 is 0, 3, 8, 15, 24, …, and
  every sum of those is a sum of 3s and 8s. The numbers that are *not* of the
  form 3x + 8y are exactly 1, 2, 4, 5, 7, 10, 13 (the Frobenius number of 3
  and 8 is 3·8 − 3 − 8 = 13).
- **That side is enough (n ≥ 82).** Write s² − n = 3a + 8b with b ≤ 2, put the
  a triangles of side 2 in the two bottom strips of height 2, the side-3
  triangles in the top triangle of side s − 4, and fill the rest with unit
  triangles. This fits whenever s ≥ 10;
  [`construction_check.py`](construction_check.py) checks it for every n up to
  200 000, and the argument (a ≤ 4s/3 < 2s − 6) is general.
- **n ≤ 100** matches the OEIS terms, which come from exhaustive enumeration.
  Together with the two bounds, the rule holds for every n.
- n = 2, 3, 5 pass the arithmetic test but are impossible geometrically, so
  they are the only hard-coded cases.

Peter Munn's formula on the OEIS entry (ceiling(√n), or one more) holds for
n > 23; at n = 12, 15, 23 the answer is two more, which "smallest s" covers.

**Golf tricks**

- `9398` has bits 1, 2, 4, 5, 7, 10, 13 set: the forbidden values of s² − n.
- `(9399<<n)-1` is `9398<<n` with n one-bits below it, so bit s² answers
  "s² < n *or* s² − n is forbidden" in one shift, with no `or` and no negative
  shift.
- `44` has bits 2, 3, 5 set. Adding `~(44>>n&1)` gives −1 normally and −2 for
  the exceptions; −2 clears bit 0, so the loop stops at s = 0 and prints 0.
- Other shapes tried (`min(...)`, `next(...)`, a single-line loop) came out
  at 74–88 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A300001), CC BY-SA 4.0.
