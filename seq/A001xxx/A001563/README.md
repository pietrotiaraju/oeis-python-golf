# A001563

> a(n) = n*n! = (n+1)! - n!.
> — [OEIS A001563](https://oeis.org/A001563)

Offset 0: 0, 1, 4, 18, 96, 600, 4320, 35280, 322560, 3265920, 36288000, …

### Python 3 — 35 bytes

```python
f=n=1
while[print(f*n-f)]:f*=n;n+=1
```

**How it works**

- a(n) = n·n! = (n + 1)! − n!. The loop is the factorial loop of
  [A000142](../../A000xxx/A000142/): on the pass with counter n, `f` holds
  (n − 1)!, and the body multiplies it by n and steps n.
- So `f*n-f` is n! − (n − 1)! = (n − 1)·(n − 1)!, the term a(n − 1): the
  first pass (n = 1, f = 0! = 1) prints a(0) = 0, the next a(1) = 1, and so on.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- Ties and near misses: `f=1;n=0` / `while[print(n*f)]:n+=1;f*=n` (f = n!
  with the same n) is also 35 bytes; the difference with a walrus,
  `while[print(-f+(f:=f*n))]:n+=1`, is 36.
- Exact integers, so every term is right; a(1558) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 101 terms (a(0) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.
- Differences of factorials: [A001563](../A001563/), [A001564](../A001564/), [A001565](../A001565/); the factorials themselves: [A000142](../../A000xxx/A000142/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001563), CC BY-SA 4.0.
