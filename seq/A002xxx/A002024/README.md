# A002024

> k appears k times; a(n) = floor(sqrt(2n) + 1/2).
> — [OEIS A002024](https://oeis.org/A002024)

Offset 1: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, …

### Python 3 — 35 bytes

```python
k=1
while[exec('print(k);'*k)]:k+=1
```

**How it works**

- For k = 1, 2, 3, … the string `'print(k);'*k` is the statement
  `print(k);` written k times, and `exec` runs it: k is printed k times.
- `exec` returns None, so `[exec(…)]` is the one-element list [None],
  which is true, and the loop body `k+=1` moves on.

**Notes**

- `print(*[k]*k,sep='\n')` is three bytes longer, a comprehension
  `[print(k)for _ in[0]*k]` two bytes longer, and the closed form
  ⌊√(2n) + 1/2⌋ = (isqrt(8n) + 1)//2 longer still.
- The b-file has 5050 terms (k up to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002024), CC BY-SA 4.0.
