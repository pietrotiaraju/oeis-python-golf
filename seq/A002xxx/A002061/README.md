# A002061

> Central polygonal numbers: a(n) = n^2 - n + 1.
> — [OEIS A002061](https://oeis.org/A002061)

Offset 0: 1, 1, 3, 7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, …

### Python 3 — 30 bytes

```python
n=0
while[print(n*n-n+1)]:n+=1
```

**How it works**

- a(n) = n² − n + 1 is evaluated directly, from n = 0 (a(0) = a(1) = 1).
- `while[print(…)]:` prints the term; the list `[None]` is true, so the
  loop never ends, and the body steps n.

**Notes**

- Stepping the value instead, with a(n+1) − a(n) = 2n
  (`a=1;n=0` / `while[print(a)]:a+=n;n+=2`), is 33 bytes; `n*~-n+1` is the
  same length as `n*n-n+1`, and (k² + 3)/4 over the odd k = 2n − 1
  (`k=-1`, `k*k+3>>2`, `k+=2`) is 33 bytes.
- Exact integer arithmetic, right for every n. The b-file has 10001 terms
  (n = 0 to 10000); the bar is the whole b-file in 60 s, which takes a
  fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002061), CC BY-SA 4.0.
