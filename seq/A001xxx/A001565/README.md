# A001565

> 3rd differences of factorial numbers.
> — [OEIS A001565](https://oeis.org/A001565)

Offset 0: 2, 11, 64, 426, 3216, 27240, 256320, 2656080, 30078720, 369774720, …

### Python 3 — 43 bytes

```python
f=n=1
while[print(f*n*(n*n+2)-f)]:f*=n;n+=1
```

**How it works**

- The third difference of k! is
  (k + 3)! − 3(k + 2)! + 3(k + 1)! − k! = k!·(k³ + 3k² + 5k + 2).
- With n = k + 1 the cubic becomes n³ + 2n − 1, so
  a(k) = (n − 1)!·(n³ + 2n − 1) = n!·(n² + 2) − (n − 1)!.
- The loop is the factorial loop of [A000142](../../A000xxx/A000142/): on the
  pass with counter n, `f` holds (n − 1)!, so the term is `f*n*(n*n+2)-f`.
  The first pass (n = 1) prints a(0) = 2.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- `f*(n**3+2*n-1)` is a byte longer; the walrus form
  `while[print(-f+(f:=f*n)*(n*n+2))]:n+=1` is 44 bytes.
- Exact integers, so every term is right; a(1556) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 101 terms (a(0) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.
- Differences of factorials: [A001563](../A001563/), [A001564](../A001564/), [A001565](../A001565/); the factorials themselves: [A000142](../../A000xxx/A000142/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001565), CC BY-SA 4.0.
