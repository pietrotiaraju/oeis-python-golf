# A000196

> Integer part of square root of n. Or, number of positive squares <= n. Or, n appears 2n+1 times.
> — [OEIS A000196](https://oeis.org/A000196)

Offset 0: 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, …

### Python 3 — 38 bytes

```python
n=k=0
while[print(k)]:n+=1;k+=~k*~k<=n
```

**How it works**

- `k` holds ⌊√n⌋. When n goes up by one, the floor root goes up by at most
  one, and it does so exactly when n reaches the next square (k+1)².
- `~k` is −(k+1), so `~k*~k` is (k+1)²: 5 bytes, one under `k*k+2*k<n` and
  three under `(k+1)**2<=n`. Unary `~` binds tighter than `*`, and `*`
  tighter than `<=`, so no parentheses are needed.
- The comparison is a bool, and `k+=` adds it as 0 or 1.
- `while[print(k)]:` loops forever (a one-element list is truthy) and is a
  byte under `while 1:print(k);`.

**Notes**

- Integer arithmetic only, no `math.isqrt` and no floats, so it is correct
  for every n. It prints the whole b-file (10001 terms) at once; the bar is
  the whole b-file in 60 s.
- The other routes tried: `exec("print(k);"*(k-~k))` once per k (each k
  appears 2k+1 times) and the walrus form `print(k:=k+(~k*~k<=n))` both
  come to 40 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000196), CC BY-SA 4.0.
