# A000387

> Rencontres numbers: number of permutations of [n] with exactly two fixed points.
> — [OEIS A000387](https://oeis.org/A000387)

Offset 0: 0, 0, 1, 0, 6, 20, 135, 924, 7420, 66744, 667485, …

### Python 3 — 41 bytes

```python
e=n=0
while[print(e*n>>1)]:e=(e^1)*n;n+=1
```

**How it works**

- Choose the two fixed points and derange the rest:
  a(n) = C(n, 2)·D(n−2), where D = [A000166](../A000166/) are the
  derangement numbers. The program keeps e = (n−1)·D(n−2), so
  a(n) = n·e/2 is `e*n>>1` (n·e = n(n−1)·D(n−2) is even, so the shift is
  exact).
- From D(n−1) = (n−1)·D(n−2) + (−1)^(n−1) we get e = D(n−1) + (−1)ⁿ.
  D(k) is odd exactly when k is even (D(k) = k·D(k−1) + (−1)^k, by
  induction), so adding (−1)ⁿ to D(n−1) only flips its last bit:
  e = D(n−1) xor 1, and back, D(n−1) = e xor 1.
- The next value is then n·D(n−1) = n·(e xor 1), the update
  `e=(e^1)*n`. With e = n = 0 the first two passes print 0 and leave
  e = 0 = 0·D(−1) and then e = 1 = 1·D(0), so no seed is needed.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (201 terms, n = 0 to 200) prints at once; the program stops after
  a(1558), when the next term passes the 4300-digit int-to-str limit of
  Python 3.11+. The bar is the whole b-file in 60 s.
- Keeping D(n−1) itself, `d=n=0` /
  `while[print((d^1)*n>>1)]:d=d*n^1;n+=1`, is 43 bytes, and D(n−2) with
  `print(d*n*~-n//2)` and `d=d*~-n^1` is 45. Starting one step early
  (update inside `print`) needs n = −1 and is 47.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000387), CC BY-SA 4.0.
