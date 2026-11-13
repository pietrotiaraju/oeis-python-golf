# A001564

> 2nd differences of factorial numbers.
> — [OEIS A001564](https://oeis.org/A001564)

Offset 0: 1, 3, 14, 78, 504, 3720, 30960, 287280, 2943360, 33022080, …

### Python 3 — 39 bytes

```python
f=n=1
while[print(f+f*n*~-n)]:f*=n;n+=1
```

**How it works**

- The second difference of k! is
  (k + 2)! − 2(k + 1)! + k! = k!·((k + 2)(k + 1) − 2(k + 1) + 1)
  = k!·(k² + k + 1).
- The loop is the factorial loop of [A000142](../../A000xxx/A000142/): on the
  pass with counter n, `f` holds (n − 1)!, so with k = n − 1 the term is
  f·((n − 1)² + (n − 1) + 1) = f·(n(n − 1) + 1), printed as `f+f*n*~-n`
  (`~-n` is n − 1). The first pass prints a(0) = 1.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- `f*(n*n-n+1)` is 2 bytes longer. With f = n! and k = n (`f=1;n=0`, body
  `n+=1;f*=n`) the term `f-f*n*~n` is a byte shorter but the start costs
  two more: 40 bytes. Moving the update into a walrus,
  `while[print(f+(f:=f*n)*~-n)]:n+=1`, ties at 39.
- Exact integers, so every term is right; a(1557) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 101 terms (a(0) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.
- Differences of factorials: [A001563](../A001563/), [A001564](../A001564/), [A001565](../A001565/); the factorials themselves: [A000142](../../A000xxx/A000142/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001564), CC BY-SA 4.0.
